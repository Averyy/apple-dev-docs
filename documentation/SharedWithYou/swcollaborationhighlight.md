# SWCollaborationHighlight

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

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

```objc
@interface SWCollaborationHighlight : SWHighlight
```

## Mentions

- [Adding custom collaboration to your app](./adding-custom-collaboration-to-your-app.md)
- [Adding shared content collaboration to your app](./adding-shared-content-collaboration-to-your-app.md)

## Topics

### Accessing collaboration attributes
- [var collaborationIdentifier: String](./swcollaborationhighlight/collaborationidentifier.md)
  A unique identifier that the app hosting the collaboration provides.
- [var contentType: UTType](./swcollaborationhighlight/contenttype.md)
  The UTI type for this collaboration highlight.
- [var creationDate: Date](./swcollaborationhighlight/creationdate.md)
  The date the system creates this file.
- [var title: String?](./swcollaborationhighlight/title.md)
  The title of the collaboration highlight.

## Relationships

### Inherits From
- [SWHighlight](./swhighlight.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Collaboration attributes
- [class SWCollaborationMetadata](../SharedWithYouCore/swcollaborationmetadata.md)
  A model object for conveying data during a collaboration.
- [struct SWCollaborationIdentifier](../SharedWithYouCore/swcollaborationidentifier.md)
  A unique identifier for a collaboration.
- [struct SWLocalCollaborationIdentifier](../SharedWithYouCore/swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let SWCollaborationMetadataTypeIdentifier: String](./swcollaborationmetadatatypeidentifier.md)
  A string constant for the metadata type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationhighlight)*