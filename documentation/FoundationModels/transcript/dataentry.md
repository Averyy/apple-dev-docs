# Transcript.DataEntry

**Framework**: Foundation Models  
**Kind**: struct

A top-level transcript entry payload in a serialized, portable format.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
struct DataEntry
```

#### Overview

A [`Transcript.DataEntry`](transcript/dataentry.md) records the bytes and identifier of a value that a [`LanguageModel`](languagemodel.md) implementation opted into via [`supportsDataEntryType(_:)`](languagemodel/supportsdataentrytype(_:).md). It’s what a [`DataEntryRepresentable`](dataentryrepresentable.md)-conforming type produces from its [`transcriptRepresentation`](dataentryrepresentable/transcriptrepresentation.md), and it round-trips through the transcript’s `Codable` conformance so the transcript remains portable even in environments where the declaring package isn’t installed.

## Topics

### Initializers
- [init(id: String, contentType: UTType, content: Data, metadata: GeneratedContent)](transcript/dataentry/init(id:contenttype:content:metadata:).md)
  Creates a data entry with the content type, content, and metadata you provide.
### Instance Properties
- [var content: Data](transcript/dataentry/content.md)
  A raw binary representation of the entry.
- [var contentType: UTType](transcript/dataentry/contenttype.md)
  A `UTType` identifying how to interpret [`content`](transcript/dataentry/content.md).
- [var metadata: GeneratedContent](transcript/dataentry/metadata.md)
  Metadata pertinent to this entry.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataentry)*