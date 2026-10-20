# FSContext

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A context object that provides information about the initiator of a file system operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSContext
```

```objc
@interface FSContext : NSObject
```

#### Overview

This object contains the user ID and group ID of the process that initiated the file system operation, allowing file systems to make authorization decisions based on the caller’s identity. Use this context in handler methods that provide the context as a parameter.

## Topics

### Accessing context properties
- [var realUserID: Int](./fscontext/realuserid.md)
  The caller’s real user ID.
- [var effectiveUserID: Int](./fscontext/effectiveuserid.md)
  The caller’s effective user ID.
- [var realGroupID: Int](./fscontext/realgroupid.md)
  The caller’s real group ID.
- [var effectiveGroupID: Int](./fscontext/effectivegroupid.md)
  The caller’s effective group ID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [class FSOpenItemResult](./fsopenitemresult.md)
  The result of an open-item call.
- [func close(FSItem, context: FSContext, replyHandler: () -> Void)](./fsvolume/datacachehandler/close%28_,context,replyhandler%29.md)
  Closes an item and releases associated cache resources.
- [FSVolume.DataCacheMode](./fsvolume/datacachemode.md)
  A type that defines the cache mode requested by the kernel for data operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontext)*