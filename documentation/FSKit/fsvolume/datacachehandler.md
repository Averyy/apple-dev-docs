# FSVolume.DataCacheHandler

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Methods and properties implemented by volumes that coordinate kernel-level data caching.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol DataCacheHandler : NSObjectProtocol
```

```objc
@protocol FSVolumeDataCacheHandler <NSObject>
```

## Overview

A volume that conforms to this protocol enables kernel data caching for improved I/O performance. This protocol allows filesystem modules to negotiate cache modes with the kernel and manage cache coherency.

> **Note**: This protocol handles the complete open and close lifecycle for items. When a volume conforms to `FSVolumeDataCacheHandler`, FSKit routes every open and close operation through this protocol’s [`open(_:modes:cacheMode:context:replyHandler:)`](./datacachehandler/open%28_,modes,cachemode,context,replyhandler%29.md) and [`close(_:context:replyHandler:)`](./datacachehandler/close%28_,context,replyhandler%29.md) methods. A volume that adopts this protocol doesn’t need to also conform to [`FSVolume.OpenCloseHandler`](./openclosehandler.md).

When a file opens, the module receives the requested [`FSVolume.DataCacheMode`](./datacachemode.md) and returns a [`FSVolume.KernelCacheCoherencyType`](./kernelcachecoherencytype.md) indicating the kind of caching behavior it can support. The kernel then caches data according to the granted coherency type. The module can dynamically upgrade or downgrade cache modes as conditions change.

The kernel requests a caching mode expressed as a [`FSVolume.DataCacheMode`](./datacachemode.md) value, which indicates what the kernel would like to cache (read-only data, read-write data, or no caching). The module then replies with a specific [`FSVolume.KernelCacheCoherencyType`](./kernelcachecoherencytype.md) value, which defines how the kernel should cache the data (no caching, read-only caching, write-through caching, or write-back caching). When the module detects an asynchronous condition requiring a change in caching mode (such as an lease break), the module uses a value from [`FSVolume.KernelCacheCoherencyAction`](./kernelcachecoherencyaction.md) to instruct the kernel how to handle any cached data (push dirty pages, invalidate cache, or update coherency mode).

The protocol supports deferred closing, where the kernel maintains cache state even after a file is closed, enabling improved performance for frequently accessed files. The [`FSVolume.KernelCacheCoherencyType.readCache`](./kernelcachecoherencytype/readcache.md), [`FSVolume.KernelCacheCoherencyType.writeThrough`](./kernelcachecoherencytype/writethrough.md), and [`FSVolume.KernelCacheCoherencyType.writeBack`](./kernelcachecoherencytype/writeback.md) modes support deferred closing.

The following table shows the mapping of cache modes to supported coherency types.

| Cache mode | Coherency type |
| --- | --- |
| [`FSVolume.DataCacheMode.none`](./datacachemode/none.md) | [`FSVolume.KernelCacheCoherencyType.noCache`](./kernelcachecoherencytype/nocache.md) |
| [`FSVolume.DataCacheMode.readWithCache`](./datacachemode/readwithcache.md) | [`FSVolume.KernelCacheCoherencyType.noCache`](./kernelcachecoherencytype/nocache.md) or [`FSVolume.KernelCacheCoherencyType.readCache`](./kernelcachecoherencytype/readcache.md) |
| [`FSVolume.DataCacheMode.readWriteWithCache`](./datacachemode/readwritewithcache.md) | [`FSVolume.KernelCacheCoherencyType.noCache`](./kernelcachecoherencytype/nocache.md), [`FSVolume.KernelCacheCoherencyType.readCache`](./kernelcachecoherencytype/readcache.md), [`FSVolume.KernelCacheCoherencyType.writeBack`](./kernelcachecoherencytype/writeback.md) or [`FSVolume.KernelCacheCoherencyType.writeThrough`](./kernelcachecoherencytype/writethrough.md) |

### Supporting coherency transitions

Transitioning between coherency types requires different behaviors from your volume implementation, depending on whether the new type is more or less permissive than its current value. The following table expresses the permissiveness of the coherency types.

| Coherency type | Permissiveness |
| --- | --- |
| [`FSVolume.KernelCacheCoherencyType.noCache`](./kernelcachecoherencytype/nocache.md) | Least permissive |
| [`FSVolume.KernelCacheCoherencyType.readCache`](./kernelcachecoherencytype/readcache.md) |  |
| [`FSVolume.KernelCacheCoherencyType.writeBack`](./kernelcachecoherencytype/writeback.md) |  |
| [`FSVolume.KernelCacheCoherencyType.writeThrough`](./kernelcachecoherencytype/writethrough.md) | Most permissive |

When transitioning to more permissive caching, kernel performs an “upgrade” by calling [`upgrade(_:cacheMode:context:replyHandler:)`](./datacachehandler/upgrade%28_,cachemode,context,replyhandler%29.md). Your volume doesn’t need to perform a flush or purge when upgrading to a more permissive coherency type.

Transitioning to a less permissive coherency type is considered a “downgrade”. Your module initiates this process by calling [`setCacheState(for:cacheMode:coherencyType:action:)`](./setcachestate%28for,cachemode,coherencytype,action%29.md) when conditions change. In this scenario, set the `action` to [`FSVolume.KernelCacheCoherencyAction.push`](./kernelcachecoherencyaction/push.md), [`FSVolume.KernelCacheCoherencyAction.pushInvalidate`](./kernelcachecoherencyaction/pushinvalidate.md), or [`FSVolume.KernelCacheCoherencyAction.invalidate`](./kernelcachecoherencyaction/invalidate.md). Handle any dirty data by flushing or purging it before downgrading with this method call.

> ❗ **Important**: If a file system doesn’t conform to this protocol, the kernel may still cache it. However, such a file system has no control over caching behavior; the kernel caches data as it sees fit.

## Topics

### Opening and closing items
- [func open(FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSOpenItemResult?, (any Error)?) -> Void)](./datacachehandler/open%28_,modes,cachemode,context,replyhandler%29.md)
  Opens an item with cache mode negotiation.
- [class FSOpenItemResult](../fsopenitemresult.md)
  The result of an open-item call.
- [func close(FSItem, context: FSContext, replyHandler: () -> Void)](./datacachehandler/close%28_,context,replyhandler%29.md)
  Closes an item and releases associated cache resources.
- [FSVolume.DataCacheMode](./datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [class FSContext](../fscontext.md)
  A context object that provides information about the initiator of a file system operation.
### Changing cache behavior
- [func upgrade(FSItem, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSUpgradeItemResult?, (any Error)?) -> Void)](./datacachehandler/upgrade%28_,cachemode,context,replyhandler%29.md)
  Upgrades the item cache mode to a less restrictive level, allowing more caching.
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSContext](../fscontext.md)
  A context object that provides information about the initiator of a file system operation.
- [class FSUpgradeItemResult](../fsupgradeitemresult.md)
  The result of an upgrade-item call.
### Inspecting cache behavior
- [var isDataCacheInhibited: Bool](./datacachehandler/isdatacacheinhibited.md)
  A Boolean value that instructs FSKit not to call this protocol’s methods, even if the volume conforms to it.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Implementing optional handlers
- [FSVolume.OpenCloseHandler](./openclosehandler.md)
  Methods and properties implemented by volumes that want to receive open and close calls for each item.
- [FSVolume.ReadWriteHandler](./readwritehandler.md)
  Methods implemented for read and write operations that deliver data to and from the extension.
- [FSVolume.AccessCheckHandler](./accesscheckhandler.md)
  Methods and properties implemented by volumes that want to enforce access check operations.
- [FSVolume.RenameHandler](./renamehandler.md)
  Methods and properties implemented by volumes that support renaming the volume.
- [FSVolume.PreallocateHandler](./preallocatehandler.md)
  Methods and properties implemented by volumes that want to offer preallocation functions.
- [FSVolume.XattrHandler](./xattrhandler.md)
  Methods and properties implemented by volumes that natively or partially support extended attributes.
- [FSVolume.ItemDeactivationHandler](./itemdeactivationhandler.md)
  Methods and properties implemented by volumes that support deactivating items.
- [FSVolume.KernelOffloadedIOHandler](./kerneloffloadediohandler.md)
  Methods and properties implemented by volumes that use kernel-offloaded I/O to achieve higher file transfer performance.
- [FSVolume.SeekRegionHandler](./seekregionhandler.md)
  Methods and properties implemented by volumes that support seek operations


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler)*