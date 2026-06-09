# mountSingleVolume(resource:bundleID:options:completionHandler:)

**Framework**: FSKit  
**Kind**: method

Asynchronously mounts a single volume file system with a given resource.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func mountSingleVolume(resource: FSResource, bundleID: String, options: [String]) async throws -> URL
```

#### Discussion

`::::: Swift ::::::::::`

- completionHandler: A block or closure to indicate success or failure. If mount fails, the first parameter is nil and second parameter contains an error. If mount succeeds, the first parameter contains the URL of the mount path, and second parameter is `nil`.

`::::::::::::::::::::`

`::::: ObjC ::::::::::`

- mountPath: A block or closure to indicate success or failure. If mount fails, the first parameter is nil and second parameter contains an error. If mount succeeds, the first parameter contains the URL of the mount path, and second parameter is `nil`.

`::::::::::::::::::::`

#### Discussion

This method allows a client with the `com.apple.developer.fskit.mount` entitlement to mount a single-volume file system. Calling this method performs the complete workflow of resource loading, volume activation, mount point creation, and actual mounting. The system mounts the volume within the `/Volumes/` directory.

The caller can only mount modules that are visible to them.

## Parameters

- `resource`: The resource to mount.
- `bundleID`: The bundle identifier of the file system extension.
- `options`: An array of strings containing the `mount_XXX` mount options

## See Also

- [class FSResource](fsresource.md)
  An abstract resource a file system uses to provide data for a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsclient/mountsinglevolume(resource:bundleid:options:completionhandler:))*