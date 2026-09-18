# Transcript.DataAttachment

**Framework**: Foundation Models  
**Kind**: struct

A data attachment payload in a serialized, portable format.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
struct DataAttachment
```

#### Overview

A [`Transcript.DataAttachment`](transcript/dataattachment.md) records the bytes and identifier of a value that a [`LanguageModel`](languagemodel.md) implementation opted into via [`supportsDataAttachmentType(_:)`](languagemodel/supportsdataattachmenttype(_:).md). It’s what a [`DataAttachmentRepresentable`](dataattachmentrepresentable.md)-conforming type produces from its [`transcriptRepresentation`](dataattachmentrepresentable/transcriptrepresentation.md), and it round-trips through the transcript’s `Codable` conformance so the transcript remains portable even in environments where the declaring package isn’t installed.

## Topics

### Initializers
- [init(contentType: UTType, content: Data, metadata: GeneratedContent)](transcript/dataattachment/init(contenttype:content:metadata:).md)
  Creates a data attachment with the content type, content, and metadata you provide.
### Instance Properties
- [var content: Data](transcript/dataattachment/content.md)
  A raw binary representation of the attachment.
- [var contentType: UTType](transcript/dataattachment/contenttype.md)
  A `UTType` identifying how to interpret [`content`](transcript/dataattachment/content.md).
- [var metadata: GeneratedContent](transcript/dataattachment/metadata.md)
  Metadata pertinent to this attachment.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataattachment)*