# LinkMetadata.Attachment

**Framework**: Link Presentation  
**Kind**: struct

Describes a kind of attachment to the metadata.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
struct Attachment
```

## Topics

### Type Properties
- [static var icon: LinkMetadata.Attachment](linkmetadata/attachment/icon.md)
  The descriptor for an icon attachment. The corresponding media type must support the content type of the metadata’s icon data.
- [static var image: LinkMetadata.Attachment](linkmetadata/attachment/image.md)
  The descriptor for an image attachment. The corresponding media type must support the content type of the metadata’s image data.
- [static var video: LinkMetadata.Attachment](linkmetadata/attachment/video.md)
  The descriptor for a local video attachment. The corresponding media type must support the content type of the metadata’s local video data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/linkmetadata/attachment)*