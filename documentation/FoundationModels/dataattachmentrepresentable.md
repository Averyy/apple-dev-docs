# DataAttachmentRepresentable

**Framework**: Foundation Models  
**Kind**: protocol

A type that you use as the content of a data attachment.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
protocol DataAttachmentRepresentable : Sendable
```

#### Overview

Conform to this protocol to describe how a value serializes into — and deserializes back from — a [`Transcript.DataAttachment`](transcript/dataattachment.md). The serialized form is a portable `Data` blob identified by a content type identifier, which is what gets persisted when a [`Transcript`](transcript.md) is encoded, so a transcript remains readable even in environments where the declaring package isn’t installed.

A [`LanguageModel`](languagemodel.md) advertises which content types it accepts through [`supportsDataAttachmentType(_:)`](languagemodel/supportsdataattachmenttype(_:).md); the framework validates each data attachment’s [`contentType`](transcript/dataattachment/contenttype.md) against that predicate before dispatching to the executor.

## Topics

### Initializers
- [init(Transcript.DataAttachment) throws](dataattachmentrepresentable/init(_:).md)
  Rehydrates this content from its transcript representation.
### Instance Properties
- [var transcriptRepresentation: Transcript.DataAttachment](dataattachmentrepresentable/transcriptrepresentation.md)
  The transcript representation of this content.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dataattachmentrepresentable)*