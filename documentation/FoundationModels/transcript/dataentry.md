# Transcript.DataEntry

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A top-level transcript entry payload in a serialized, portable format.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct DataEntry
```

#### Overview

A [`Transcript.DataEntry`](./dataentry.md) records the bytes and identifier of a value that a [`LanguageModel`](../languagemodel.md) implementation opted into via [`supportsDataEntryType(_:)`](../languagemodel/supportsdataentrytype%28_%29.md). It’s what a [`DataEntryRepresentable`](../dataentryrepresentable.md)-conforming type produces from its [`transcriptRepresentation`](../dataentryrepresentable/transcriptrepresentation.md), and it round-trips through the transcript’s `Codable` conformance so the transcript remains portable even in environments where the declaring package isn’t installed.

## Topics

### Initializers
- [init(id: String, contentType: UTType, content: Data, metadata: GeneratedContent)](./dataentry/init%28id,contenttype,content,metadata%29.md)
  Creates a data entry with the content type, content, and metadata you provide.
### Instance Properties
- [var content: Data](./dataentry/content.md)
  A raw binary representation of the entry.
- [var contentType: UTType](./dataentry/contenttype.md)
  A `UTType` identifying how to interpret [`content`](./dataentry/content.md).
- [var metadata: GeneratedContent](./dataentry/metadata.md)
  Metadata pertinent to this entry.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataentry)*