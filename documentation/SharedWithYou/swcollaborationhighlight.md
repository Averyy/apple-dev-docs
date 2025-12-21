# SWCollaborationHighlight

**Framework**: Shared with You  
**Kind**: class

A highlight object that represents an active collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationHighlight
```

## Mentions

- [Adding custom collaboration to your app](adding-custom-collaboration-to-your-app.md)
- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)

## Topics

### Accessing collaboration attributes
- [var collaborationIdentifier: String](swcollaborationhighlight/collaborationidentifier.md)
  A unique identifier that the app hosting the collaboration provides.
- [var contentType: UTType](swcollaborationhighlight/contenttype.md)
  The UTI type for this collaboration highlight.
- [var creationDate: Date](swcollaborationhighlight/creationdate.md)
  The date the system creates this file.
- [var title: String?](swcollaborationhighlight/title.md)
  The title of the collaboration highlight.

## Relationships

### Inherits From
- [SWHighlight](swhighlight.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SWCollaborationMetadata](../sharedwithyoucore/swcollaborationmetadata.md)
  A model object for conveying data during a collaboration.
- [struct SWCollaborationIdentifier](../sharedwithyoucore/swcollaborationidentifier.md)
  A unique identifier for a collaboration.
- [struct SWLocalCollaborationIdentifier](../sharedwithyoucore/swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let SWCollaborationMetadataTypeIdentifier: String](swcollaborationmetadatatypeidentifier.md)
  A string constant for the metadata type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationhighlight)*