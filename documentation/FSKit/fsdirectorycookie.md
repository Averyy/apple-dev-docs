# FSDirectoryCookie

**Framework**: FSKit  
**Kind**: struct

A value that indicates a location in a directory from which to enumerate.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSDirectoryCookie
```

#### Overview

Your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:context:replyHandler:)`](fsvolume/handler/enumeratedirectory(_:startingat:verifier:attributes:packer:context:replyhandler:).md) defines the semantics of this value; it’s opaque to FSKit.

A value that indicates a location in a directory from which to enumerate.

Your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:replyHandler:)`](fsvolume/operations/enumeratedirectory(_:startingat:verifier:attributes:packer:replyhandler:).md) defines the semantics of this value; it’s opaque to FSKit.

## Topics

### Initializing a cookie
- [init(UInt64)](fsdirectorycookie/init(_:).md)
- [init(rawValue: UInt64)](fsdirectorycookie/init(rawvalue:).md)
### Using defined cookie values
- [static let initial: FSDirectoryCookie](fsdirectorycookie/initial.md)
  The constant initial value for the directory-enumeration cookie.

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
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [class FSDirectoryEntryPacker](fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.
- [class FSEnumerateDirectoryResult](fsenumeratedirectoryresult.md)
  The result of an enumerate-directory call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdirectorycookie)*