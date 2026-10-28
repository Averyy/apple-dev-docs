# FSEnumerateDirectoryResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of an enumerate-directory call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSEnumerateDirectoryResult
```

```objc
@interface FSEnumerateDirectoryResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:context:replyHandler:)`](./fsvolume/handler/enumeratedirectory%28_,startingat,verifier,attributes,packer,context,replyhandler%29.md).

## Topics

### Creating an enumerate-directory result
- [init?(verifier: UInt64)](./fsenumeratedirectoryresult/init%28verifier%29.md)
  Creates a result for an directory enumeration operation.
- [struct FSDirectoryVerifier](./fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](./fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.

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

### Inspecting directory contents
- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, context: FSContext, replyHandler: (FSEnumerateDirectoryResult?, (any Error)?) -> Void)](./fsvolume/handler/enumeratedirectory%28_,startingat,verifier,attributes,packer,context,replyhandler%29.md)
  Enumerates the contents of the given directory.
- [struct FSDirectoryCookie](./fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](./fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryVerifier](./fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](./fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [class FSDirectoryEntryPacker](./fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsenumeratedirectoryresult)*