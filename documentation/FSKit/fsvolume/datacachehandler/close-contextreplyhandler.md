# close(_:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Closes an item and releases associated cache resources.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func close(_ item: FSItem, context: FSContext) async
```

#### Discussion

FSKit calls this method when fully closing a file, and after the kernel finalizes all caching for the item.

Your module receives this call once per item when all references are released and the kernel has completed its cache management. The module performs any necessary cleanup operations for the item.

> **Note**:  This method doesn’t return or throw an error because the OS considers the file closed regardless of whether the module encounters any issues during cleanup.

## Parameters

- `item`: The item to close.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to call when the close operation completes.

## See Also

- [func open(FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSOpenItemResult?, (any Error)?) -> Void)](fsvolume/datacachehandler/open(_:modes:cachemode:context:replyhandler:).md)
  Opens an item with cache mode negotiation.
- [class FSOpenItemResult](fsopenitemresult.md)
  The result of an open-item call.
- [FSVolume.DataCacheMode](fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/datacachehandler/close(_:context:replyhandler:))*