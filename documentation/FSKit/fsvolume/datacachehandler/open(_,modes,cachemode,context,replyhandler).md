# open(_:modes:cacheMode:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Opens an item with cache mode negotiation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func open(_ item: FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler reply: @escaping @Sendable (FSOpenItemResult?, (any Error)?) -> Void)
```

```swift
func open(_ item: FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext) async throws -> FSOpenItemResult
```

```objc
- (void) openItem:(FSItem *) item modes:(FSVolumeOpenModes) modes cacheMode:(FSDataCacheMode) cacheMode context:(FSContext *) context replyHandler:(void (^)(FSOpenItemResult *result, NSError *error)) reply;
```

#### Discussion

FSKit calls this method when opening a file, providing the requested cache mode. The module implementation determines what level of caching it can support for this item, considering factors such as server lease availability, file locking state, or other coherency requirements.

The granted coherency type must be compatible with the requested cache mode, as defined by the cache-mode-to-coherency-type mappings documented in the discussion of the [`FSVolume.DataCacheHandler`](../datacachehandler.md) protocol. If the module grants a coherency type that exceeds the cache mode’s permissions, the kernel downgrades to a valid coherency type.

## Parameters

- `item`: The item to open.
- `modes`: The open modes, such as read and write.
- `cacheMode`: The requested cache mode, indicating what data is eligible for caching.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If opening succeeds, pass an instance of [`FSOpenItemResult`](../../fsopenitemresult.md) containing the granted [`FSVolume.KernelCacheCoherencyType`](../kernelcachecoherencytype.md), along with a `nil` error. If opening fails, pass the relevant error as the second parameter; FSKit ignores the [`FSOpenItemResult`](../../fsopenitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

### Opening and closing items
- [class FSOpenItemResult](../../fsopenitemresult.md)
  The result of an open-item call.
- [func close(FSItem, context: FSContext, replyHandler: () -> Void)](./close%28_,context,replyhandler%29.md)
  Closes an item and releases associated cache resources.
- [FSVolume.DataCacheMode](../datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [class FSContext](../../fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler/open(_:modes:cachemode:context:replyhandler:))*