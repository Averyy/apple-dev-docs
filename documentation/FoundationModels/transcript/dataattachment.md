# Transcript.DataAttachment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A data attachment payload in a serialized, portable format.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct DataAttachment
```

## Overview

A [`Transcript.DataAttachment`](./dataattachment.md) records the bytes and identifier of a value that a [`LanguageModel`](../languagemodel.md) implementation opted into via [`supportsDataAttachmentType(_:)`](../languagemodel/supportsdataattachmenttype%28_%29.md). It’s what a [`DataAttachmentRepresentable`](../dataattachmentrepresentable.md)-conforming type produces from its [`transcriptRepresentation`](../dataattachmentrepresentable/transcriptrepresentation.md), and it round-trips through the transcript’s `Codable` conformance so the transcript remains portable even in environments where the declaring package isn’t installed.

## Topics

### Initializers
- [init(contentType: UTType, content: Data, metadata: GeneratedContent)](./dataattachment/init%28contenttype,content,metadata%29.md)
  Creates a data attachment with the content type, content, and metadata you provide.
### Instance Properties
- [var content: Data](./dataattachment/content.md)
  A raw binary representation of the attachment.
- [var contentType: UTType](./dataattachment/contenttype.md)
  A `UTType` identifying how to interpret [`content`](./dataattachment/content.md).
- [var metadata: GeneratedContent](./dataattachment/metadata.md)
  Metadata pertinent to this attachment.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataattachment)*