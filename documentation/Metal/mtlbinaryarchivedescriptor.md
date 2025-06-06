# MTLBinaryArchiveDescriptor

**Framework**: Metal  
**Kind**: class

A description of a binary shader archive that you want to create.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MTLBinaryArchiveDescriptor
```

## Mentions

- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

## Topics

### Choosing an Archive File
- [var url: URL?](mtlbinaryarchivedescriptor/url.md)
  A URL to a Metal binary archive file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func makeBinaryArchive(descriptor: MTLBinaryArchiveDescriptor) throws -> any MTLBinaryArchive](mtldevice/makebinaryarchive(descriptor:).md)
  Creates a Metal binary archive instance.
- [MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/code.md)
  Error codes when creating binary archives of compiled shader code.
- [let MTLBinaryArchiveDomain: String](mtlbinaryarchivedomain.md)
  The domain for Metal binary archive errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchivedescriptor)*