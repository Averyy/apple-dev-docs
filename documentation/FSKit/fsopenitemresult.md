# FSOpenItemResult

**Framework**: FSKit  
**Kind**: class

The result of an open-item call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSOpenItemResult
```

#### Overview

Use this type in your implementation of [`open(_:modes:cacheMode:context:replyHandler:)`](fsvolume/datacachehandler/open(_:modes:cachemode:context:replyhandler:).md).

## Topics

### Creating an open-item result
- [init(grantedCoherency: FSVolume.KernelCacheCoherencyType)](fsopenitemresult/init(grantedcoherency:).md)
  Creates an open-item result.
- [FSVolume.KernelCacheCoherencyType](fsvolume/kernelcachecoherencytype.md)
  A type that defines how the kernel caches data.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func open(FSItem, modes: FSVolume.OpenModes, cacheMode: FSVolume.DataCacheMode, context: FSContext, replyHandler: (FSOpenItemResult?, (any Error)?) -> Void)](fsvolume/datacachehandler/open(_:modes:cachemode:context:replyhandler:).md)
  Opens an item with cache mode negotiation.
- [func close(FSItem, context: FSContext, replyHandler: () -> Void)](fsvolume/datacachehandler/close(_:context:replyhandler:).md)
  Closes an item and releases associated cache resources.
- [FSVolume.DataCacheMode](fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.
- [class FSContext](fscontext.md)
  A context object that provides information about the initiator of a file system operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsopenitemresult)*