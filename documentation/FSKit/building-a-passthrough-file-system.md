# Building a passthrough file system

**Framework**: FSKit

Expose an existing path as its own file system by using the FSKit framework.

**Availability**:
- macOS 26.0+
- Xcode 26.0+

#### Overview

You can use the FSKit framework to implement any kind of file system, whether based on an existing storage device or as an abstraction of the contents of a URL. To offer a simple implementation of FSKit, this sample code project serves as a passthrough file system, one which passes its file-related API calls to the underlying file system on the device. The `PassthroughFS` example reads from an existing path on your current file system and exposes it as a new file system.

##### Configure the Sample Code Project

To use the sample file system, do the following:

1. Build and run the project in Xcode. The app simply displays a window with a copyright notice because the functionality is all in the sample’s app extension.
2. In Settings > General > Login Items & Extensions, scroll to the Extensions section and click the “By Category” tab to organize the extensions.
3. In the File System Extensions cell, click the ⓘ button on the right side. This presents a scrolling list of file system extensions. Find the entry “Passthrough file system” and click the toggle on its right side to enable the extension.
4. In Terminal, use the `mkdir` command to create a directory to serve as the mount target for the passthrough file system. For example, `mkdir ~/passthrough-fs` creates a directory called `passthrough-fs` in your home directory.
5. In Terminal, use the `mount` command to mount an arbitrary directory as the source for the passthrough file system. For example, `mount -t passthrough ~/Documents ~/passthrough-fs` tells the extension to present the contents of your Documents directory as another file system, mounted at `passthrough-fs`. The `-t passthrough` flag tells `mount` that the type of the file system is `passthrough`, which sends its requests to the extension.
6. Examine the contents of the mounted directory with commands like `ls ~/passthrough-fs` to show that the contents of the source directory are indeed mounted at the target location.

##### Create an App and an Fskit Extension

To create a file system with FSKit, you create an FSKit app extension. You can do this in Xcode by adding a “File system extension” target to your project, which creates a new target with four files:

- An entitlements file with the [`com.apple.developer.fskit.fsmodule`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.fskit.fsmodule) entitlement.
- An information property list file with an `EXAppExtensionAttributes` dictionary to describe command-line interface access to the file system. For example, the `FSShortName` key in this property list provides the `passthrough` name that serves as a file system type when using the `mount` command earlier.
- An app extension implementation that conforms to the [`UnaryFileSystemExtension`](unaryfilesystemextension.md) protocol.
- A file system implementation that conforms to the [`FSUnaryFileSystem`](fsunaryfilesystem.md) and [`FSUnaryFileSystemOperations`](fsunaryfilesystemoperations.md) protocols. The app extension returns this type as the value of its [`fileSystem`](unaryfilesystemextension/filesystem-swift.property.md) property.

The sample code project already contains these items; you don’t need to create a new target. Aside from the entitlements file and the information property list, `PassthroughAppEx` defines the app extension, and `PassthroughFileSystem` is the base of the file system implementation.

##### Implement the File System Protocols

Most of the functionality of an FSKit file system actually comes from subclassing the [`FSVolume`](fsvolume.md) class as a custom type, which the [`FSUnaryFileSystem`](fsunaryfilesystem.md) implementation then instantiates and manages.

The sample project defines its volume as the `PassthroughFSVolume` type. With this type, the `PassthroughFileSystem` can implement its required [`loadResource(resource:options:replyHandler:)`](fsunaryfilesystemoperations/loadresource(resource:options:replyhandler:).md) method to set up a `PassthroughFSVolume` as follows:

1. Verify that the source resource is an [`FSPathURLResource`](fspathurlresource.md) and that the extension can access it as a security-scoped resource by calling [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/foundation/url/startaccessingsecurityscopedresource()).
2. Ignore any provided options except for `-f` (“force”), which force-loads the resource into the file system without creating a volume. If a force-loaded file system doesn’t support formatting — which `PassthroughFileSystem` doesn’t — this scenario is an error, and the file system returns the POSIX error `ENOTSUP`.
3. Call the reply handler closure with a new `PassthroughFSVolume` instance. If this results in an error, call the handler with a `nil` volume and the error instead.

```swift
public func loadResource(resource: FSResource, options: FSTaskOptions, replyHandler: @escaping (FSVolume?, (any Error)?) -> Void) {
    guard let urlResource = resource as? FSPathURLResource else {
        Logger.passthroughfs.debug("\(#function): Invalid resource type")
        return replyHandler(nil, POSIXError(.EINVAL))
    }
    guard urlResource.url.startAccessingSecurityScopedResource() else {
        Logger.passthroughfs.error("\(#function): Can't start accessing security scoped resource")
        return replyHandler(nil, POSIXError(.EACCES))
    }

    /// Handle any options present.
    for opt in options.taskOptions {
        if opt.contains("-f") {
            return replyHandler(nil, POSIXError(.ENOTSUP))
        }
    }

    self.resource = urlResource
    do {
        self.containerStatus = .ready
        return replyHandler(try PassthroughFSVolume(rootPath: urlResource.url.path), nil)
    } catch let error {
        self.resource = nil
        return replyHandler(nil, error)
    }
}
```

The implementation of the required [`unloadResource(resource:options:replyHandler:)`](fsunaryfilesystemoperations/unloadresource(resource:options:replyhandler:).md) is similar. It verifies that the source is a valid [`FSPathURLResource`](fspathurlresource.md) as before, and that a previous call to [`loadResource(resource:options:replyHandler:)`](fsunaryfilesystemoperations/loadresource(resource:options:replyhandler:).md) successfully set the local `resource` property. If so, the implementation stops accessing the security-scoped URL resource and clears the `resource` property.

```swift
public func unloadResource(resource: FSResource, options: FSTaskOptions, replyHandler reply: @escaping ((any Error)?) -> Void) {
    guard let urlResource = resource as? FSPathURLResource else {
        Logger.passthroughfs.error("\(#function): Can't cast resource")
        return reply(POSIXError(.EINVAL))
    }
    guard let loadedResource = self.resource else {
        Logger.passthroughfs.error("\(#function): No resource was loaded")
        return reply(POSIXError(.EINVAL))
    }
    guard loadedResource.url == urlResource.url else {
        Logger.passthroughfs.error("\(#function): Invalid resource was given to unload")
        return reply(POSIXError(.EINVAL))
    }
    loadedResource.url.stopAccessingSecurityScopedResource()
    self.resource = nil
    return reply(nil)
}
```

##### Implement the Volume Protocols

The sample code project uses two source files to implement the `PassthroughFSVolume` type: `PassthroughFSVolume.swift` and `PassthroughFSVolume+FSVolumeOperations.swift`. Between these two files, it implements the base [`FSVolume`](fsvolume.md) protocol along with five protocols that define sets of related operations that a file system volume may provide:

- [`FSVolume.Operations`](fsvolume/operations.md) is a required protocol that defines essential operations like mounting and unmounting, creating and deleting items, enumerating directory contents, and more. For clarity, the sample project puts this implementation in its own file, `PassthroughFSVolume+FSVolumeOperations.swift`, because it represents more code than all the other volume operations combined.
- [`FSVolume.OpenCloseOperations`](fsvolume/opencloseoperations.md) is an optional protocol that allows the volume to respond when items open and close.
- [`FSVolume.ReadWriteOperations`](fsvolume/readwriteoperations.md) is an optional protocol that provides methods to read and write file contents.
- [`FSVolume.RenameOperations`](fsvolume/renameoperations.md) is an optional protocol that supports renaming the volume.
- [`FSVolume.PreallocateOperations`](fsvolume/preallocateoperations.md) is an optional protocol that enables the volume to preallocate space for a file without writing to it yet.

The sample also subclasses the [`FSItem`](fsitem.md) class as `PassthroughFSItem`, which the `PassthroughFSVolume` code uses for FSKit methods that pass an item type as a parameter or expect it as a return value. `PassthroughFSVolume` also defines a `rootItem` property as an instance of `PassthroughFSItem`, representing the root of the virtual file system.

Given all this, `PassthroughFSVolume` implements many of its methods with calls to Darwin file system functions, using the `PassthroughFSItem`’s file descriptor with the low-level APIs. For example, the implementation of the [`FSVolume.Operations`](fsvolume/operations.md) method `FSVolume/Operations/synchronize(flags:replyHandler:)`, which flushes in-memory buffers to the storage device, is effectively a wrapper around a call to the Darwin `fsync(2)` function:

```swift
public func synchronize(flags: FSSyncFlags,
                        replyHandler reply: @escaping ((any Error)?) -> Void) {
    guard fsync(self.rootItem.fileDescriptor) == 0 else {
        let err = posixErrno
        Logger.passthroughfs.error("\(#function): Failed to synchronize with error(\(err))")
        return reply(err)
    }
    return reply(nil)
}
```

Similarly, the implementation of the [`FSVolume.ReadWriteOperations`](fsvolume/readwriteoperations.md) method [`read(from:at:length:into:replyHandler:)`](fsvolume/readwriteoperations/read(from:at:length:into:replyhandler:).md) inspects the `PassthroughFSItem` item to read from, gets its file descriptor, and calls the Darwin function `pread(2)` to read from the source file at a specific offset without modifying its file pointer. It checks the function’s return value to determine how many bytes it successfully read into the provided `buffer`, fetching the POSIX error code if `pread` returned the error value `-1`. Finally, it invokes the provided reply handler closure, passing the number of bytes read or the error code.

```swift
public func read(from item: FSItem,
                 at offset: off_t,
                 length: Int,
                 into buffer: FSMutableFileDataBuffer,
                 replyHandler: @escaping (Int, Error?) -> Void) {
    guard let ptItem = item as? PassthroughFSItem else {
        Logger.passthroughfs.error("\(#function): Can't cast item")
        return replyHandler(0, POSIXError(.EINVAL))
    }
    let oldFD = ptItem.fileDescriptor
    if oldFD < 0 {
        try? ptItem.upgradeOpenMode(mode: .readOnly)
    }
    var err: Error?
    var actuallyRead = 0
    buffer.withUnsafeMutableBytes { rawBufferPointer in
        actuallyRead = pread(ptItem.fileDescriptor, rawBufferPointer.baseAddress, length, offset)

        // Check if the read operation was successful.
        if actuallyRead == -1 {
            err = posixErrno
        }
    }

    if oldFD < 0 {
        try? ptItem.closeItem()
    }
    guard err == nil else {
        return replyHandler(0, err)
    }
    return replyHandler(actuallyRead, nil)
}
```

Your own [`FSVolume`](fsvolume.md) implementation is free to implement whichever volume operation protocols you need for your purposes, as long as you implmement the required [`FSVolume.Operations`](fsvolume/operations.md) protocol. You can omit any operation protocols you don’t need. For example, `PassthroughFSVolume` doesn’t implement [`FSVolume.XattrOperations`](fsvolume/xattroperations.md), [`FSVolume.ItemDeactivation`](fsvolume/itemdeactivation.md), or [`FSVolumeKernelOffloadedIOOperations`](fsvolumekerneloffloadediooperations.md), in order to keep the sample project small and simple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/building-a-passthrough-file-system)*