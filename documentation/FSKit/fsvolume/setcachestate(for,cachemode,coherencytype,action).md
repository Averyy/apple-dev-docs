# setCacheState(for:cacheMode:coherencyType:action:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Sends a synchronous cache state update request from the module to the kernel.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func setCacheState(for item: FSItem, cacheMode: FSVolume.DataCacheMode, coherencyType: FSVolume.KernelCacheCoherencyType, action: FSVolume.KernelCacheCoherencyAction) -> (any Error)?
```

```objc
- (NSError *) setCacheStateForItem:(FSItem *) item cacheMode:(FSDataCacheMode) cacheMode coherencyType:(FSKernelCacheCoherencyType) coherencyType coherencyAction:(FSKernelCacheCoherencyAction) action;
```

#### Return Value

An error if the kernel was unable to complete the requested cache state change, or `nil` on success.

#### Discussion

Volumes conforming to [`FSVolume.DataCacheHandler`](./datacachehandler.md) call this method to proactively notify the kernel about cache policy changes that need to be applied immediately. This allows module-initiated updates outside the normal open/close/upgrade/downgrade flow.

When downgrading coherency type, the action must be [`FSVolume.KernelCacheCoherencyAction.push`](./kernelcachecoherencyaction/push.md), [`FSVolume.KernelCacheCoherencyAction.pushInvalidate`](./kernelcachecoherencyaction/pushinvalidate.md), or [`FSVolume.KernelCacheCoherencyAction.invalidate`](./kernelcachecoherencyaction/invalidate.md) to instruct the kernel how to handle cached data. If the action fails, the cache state remains unchanged and the method returns an error.

> ❗ **Important**: This method must be called without holding any module-internal locks. The kernel may issue additional operations back into the module to satisfy cache state changes, which could result in deadlock if locks are held.

> **Note**: This method is only functional for volumes that conform to [`FSVolume.DataCacheHandler`](./datacachehandler.md). For volumes that don’t conform to the protocol, this method returns `ENOTSUP`.

## Parameters

- `item`: The item for which to update the cache state.
- `cacheMode`: The new cache mode to apply.
- `coherencyType`: The new coherency type to apply.
- `action`: The action for the kernel to perform on cached data (push, invalidate, update, or revoke).

## See Also

### Managing caching behavior
- [class FSItem](../fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [FSVolume.DataCacheMode](./datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [FSVolume.KernelCacheCoherencyType](./kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.
- [FSVolume.KernelCacheCoherencyAction](./kernelcachecoherencyaction.md)
  A type that defines actions for cache state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/setcachestate(for:cachemode:coherencytype:action:))*