# FSVolume.DataCacheHandler

**Framework**: FSKit  
**Kind**: protocol

Methods and properties implemented by volumes that coordinate kernel-level data caching.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
protocol DataCacheHandler : NSObjectProtocol
```

#### Overview

A volume that conforms to this protocol enables kernel data caching for improved I/O performance. This protocol allows filesystem modules to negotiate cache modes with the kernel and manage cache coherency.

When a file opens, the module receives the requested [`FSVolume.DataCacheMode`](fsvolume/datacachemode.md) and returns a [`FSVolume.KernelCacheCoherencyType`](fsvolume/kernelcachecoherencytype.md) indicating the kind of caching behavior it can support. The kernel then caches data according to the granted coherency type. The module can dynamically upgrade or downgrade cache modes as conditions change.

The kernel requests a caching mode expressed as a [`FSVolume.DataCacheMode`](fsvolume/datacachemode.md) value, which indicates what the kernel would like to cache (read-only data, read-write data, or no caching). The module then replies with a specific [`FSVolume.KernelCacheCoherencyType`](fsvolume/kernelcachecoherencytype.md) value, which defines how the kernel should cache the data (no caching, read-only caching, write-through caching, or write-back caching). When the module detects an asynchronous condition requiring a change in caching mode (such as an lease break), the module uses a value from [`FSVolume.KernelCacheCoherencyAction`](fsvolume/kernelcachecoherencyaction.md) to instruct the kernel how to handle any cached data (push dirty pages, invalidate cache, or update coherency mode).

The protocol supports deferred closing, where the kernel maintains cache state even after a file is closed, enabling improved performance for frequently accessed files. The [`FSVolume.KernelCacheCoherencyType.readCache`](fsvolume/kernelcachecoherencytype/readcache.md), [`FSVolume.KernelCacheCoherencyType.writeThrough`](fsvolume/kernelcachecoherencytype/writethrough.md), and [`FSVolume.KernelCacheCoherencyType.writeBack`](fsvolume/kernelcachecoherencytype/writeback.md) modes support deferred closing.

The following table shows the mapping of cache modes to supported coherency types.

| Cache mode | Coherency type |
| --- | --- |
| [`FSVolume.DataCacheMode.none`](fsvolume/datacachemode/none.md) | [`FSVolume.KernelCacheCoherencyType.noCache`](fsvolume/kernelcachecoherencytype/nocache.md) |
| [`FSVolume.DataCacheMode.readWithCache`](fsvolume/datacachemode/readwithcache.md) | [`FSVolume.KernelCacheCoherencyType.noCache`](fsvolume/kernelcachecoherencytype/nocache.md) or [`FSVolume.KernelCacheCoherencyType.readCache`](fsvolume/kernelcachecoherencytype/readcache.md) |
| [`FSVolume.DataCacheMode.readWriteWithCache`](fsvolume/datacachemode/readwritewithcache.md) | [`FSVolume.KernelCacheCoherencyType.noCache`](fsvolume/kernelcachecoherencytype/nocache.md), [`FSVolume.KernelCacheCoherencyType.readCache`](fsvolume/kernelcachecoherencytype/readcache.md), [`FSVolume.KernelCacheCoherencyType.writeBack`](fsvolume/kernelcachecoherencytype/writeback.md) or [`FSVolume.KernelCacheCoherencyType.writeThrough`](fsvolume/kernelcachecoherencytype/writethrough.md) |

##### Supporting Coherency Transitions

Transitioning between coherency types requires different behaviors from your volume implementation, depending on whether the new type is more or less permissive than its current value. The following table expresses the permissiveness of the coherency types.

| Coherency type | Permissiveness |
| --- | --- |
| [`FSVolume.KernelCacheCoherencyType.noCache`](fsvolume/kernelcachecoherencytype/nocache.md) | Least permissive |
| [`FSVolume.KernelCacheCoherencyType.readCache`](fsvolume/kernelcachecoherencytype/readcache.md) |  |
| [`FSVolume.KernelCacheCoherencyType.writeBack`](fsvolume/kernelcachecoherencytype/writeback.md) |  |
| [`FSVolume.KernelCacheCoherencyType.writeThrough`](fsvolume/kernelcachecoherencytype/writethrough.md) | Most permissive |

When transitioning to more permissive caching, kernel performs an “upgrade” by calling [`upgrade(_:cacheMode:context:replyHandler:)`](fsvolume/datacachehandler/upgrade(_:cachemode:context:replyhandler:).md). Your volume doesn’t need to perform a flush or purge when upgrading to a more permissive coherency type.

Transitioning to a less permissive coherency type is considered a “downgrade”. Your module initiates this process by calling [`setCacheState(for:cacheMode:coherencyType:action:)`](fsvolume/setcachestate(for:cachemode:coherencytype:action:).md) when conditions change. In this scenario, set the `action` to [`FSVolume.KernelCacheCoherencyAction.push`](fsvolume/kernelcachecoherencyaction/push.md), [`FSVolume.KernelCacheCoherencyAction.pushInvalidate`](fsvolume/kernelcachecoherencyaction/pushinvalidate.md), or [`FSVolume.KernelCacheCoherencyAction.invalidate`](fsvolume/kernelcachecoherencyaction/invalidate.md). Handle any dirty data by flushing or purging it before downgrading with this method call.

> ❗ **Important**: If a file system doesn’t conform to this protocol, the kernel may still cache it. However, such a file system has no control over caching behavior; the kernel caches data as it sees fit.

## Topics

### Opening and closing items
- [func open(FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSOpenItemResult?, (any Error)?) -> Void)](fsvolume/datacachehandler/open(_:modes:cachemode:context:replyhandler:).md)
  Opens an item with cache mode negotiation.
- [class FSOpenItemResult](fsopenitemresult.md)
  The result of an open-item call.
- [func close(FSItem, context: FSContext, replyHandler: () -> Void)](fsvolume/datacachehandler/close(_:context:replyhandler:).md)
  Closes an item and releases associated cache resources.
- [FSVolume.DataCacheMode](fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.
### Changing cache behavior
- [func upgrade(FSItem, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSUpgradeItemResult?, (any Error)?) -> Void)](fsvolume/datacachehandler/upgrade(_:cachemode:context:replyhandler:).md)
  Upgrades the item cache mode to a less restrictive level, allowing more caching.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSUpgradeItemResult](fsupgradeitemresult.md)
  The result of an upgrade-item call.
### Inspecting cache behavior
- [var isDataCacheInhibited: Bool](fsvolume/datacachehandler/isdatacacheinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [FSVolume.OpenCloseHandler](fsvolume/openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](fsvolume/readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckHandler](fsvolume/accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameHandler](fsvolume/renamehandler.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateHandler](fsvolume/preallocatehandler.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrHandler](fsvolume/xattrhandler.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivationHandler](fsvolume/itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.KernelOffloadedIOHandler](fsvolume/kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.SeekRegionHandler](fsvolume/seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler)*