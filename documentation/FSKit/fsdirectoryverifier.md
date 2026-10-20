# FSDirectoryVerifier

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

A tool to detect whether the directory contents changed since the last call to enumerate a directory.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSDirectoryVerifier
```

```c
typedef uint64_t FSDirectoryVerifier;
```

#### Overview

Your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:replyHandler:)`](./fsvolume/operations/enumeratedirectory%28_,startingat,verifier,attributes,packer,replyhandler%29.md) defines the semantics of this value; it’s opaque to FSKit.

## Topics

### Initializing a verifier
- [init(UInt64)](./fsdirectoryverifier/init%28_%29.md)
- [init(rawValue: UInt64)](./fsdirectoryverifier/init%28rawvalue%29.md)
### Using defined verifier values
- [static let initial: FSDirectoryVerifier](./fsdirectoryverifier/initial.md)
  The constant initial value for the directory-enumeration verifier.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting directory contents
- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, context: FSContext, replyHandler: (FSEnumerateDirectoryResult?, (any Error)?) -> Void)](./fsvolume/handler/enumeratedirectory%28_,startingat,verifier,attributes,packer,context,replyhandler%29.md)
  Enumerates the contents of the given directory.
- [struct FSDirectoryCookie](./fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](./fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [class FSDirectoryEntryPacker](./fsdirectoryentrypacker.md)
  An object used to provide items during a directory enumeration.
- [class FSEnumerateDirectoryResult](./fsenumeratedirectoryresult.md)
  The result of an enumerate-directory call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdirectoryverifier)*