# FSDirectoryVerifier

**Framework**: FSKit  
**Kind**: struct

A tool to detect whether the directory contents changed since the last call to enumerate a directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSDirectoryVerifier
```

#### Overview

Your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:replyHandler:)`](fsvolume/operations/enumeratedirectory(_:startingat:verifier:attributes:packer:replyhandler:).md) defines the semantics of this value; it’s opaque to FSKit.

## Topics

### Initializing a verifier
- [init(UInt64)](fsdirectoryverifier/init(_:).md)
- [init(rawValue: UInt64)](fsdirectoryverifier/init(rawvalue:).md)
### Using defined verifier values
- [static let initial: FSDirectoryVerifier](fsdirectoryverifier/initial.md)
  The constant initial value for the directory-enumeration verifier.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, context: FSContext, replyHandler: (FSEnumerateDirectoryResult?, (any Error)?) -> Void)](fsvolume/handler/enumeratedirectory(_:startingat:verifier:attributes:packer:context:replyhandler:).md)
  Enumerates the contents of the given directory.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [class FSDirectoryEntryPacker](fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.
- [class FSEnumerateDirectoryResult](fsenumeratedirectoryresult.md)
  The result of an enumerate-directory call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdirectoryverifier)*