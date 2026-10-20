# FSOpenItemResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of an open-item call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSOpenItemResult
```

```objc
@interface FSOpenItemResult : FSVolumeHandlerResult
```

#### Overview

Use this type in your implementation of [`open(_:modes:cacheMode:context:replyHandler:)`](./fsvolume/datacachehandler/open%28_,modes,cachemode,context,replyhandler%29.md).

## Topics

### Creating an open-item result
- [init(grantedCoherency: FSVolume.KernelCacheCoherencyType)](./fsopenitemresult/init%28grantedcoherency%29.md)
  Creates an open-item result.
- [FSVolume.KernelCacheCoherencyType](./fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Opening and closing items
- [func open(FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSOpenItemResult?, (any Error)?) -> Void)](./fsvolume/datacachehandler/open%28_,modes,cachemode,context,replyhandler%29.md)
  Opens an item with cache mode negotiation.
- [func close(FSItem, context: FSContext, replyHandler: () -> Void)](./fsvolume/datacachehandler/close%28_,context,replyhandler%29.md)
  Closes an item and releases associated cache resources.
- [FSVolume.DataCacheMode](./fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [class FSContext](./fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsopenitemresult)*