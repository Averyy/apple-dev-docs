# LanguageModelExecutorGenerationChannel.DataEntry.Update

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

The content carried by an [`update(contentType:content:metadata:)`](./action-swift.struct/update%28contenttype,content,metadata%29.md) action.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct Update
```

## Topics

### Instance Properties
- [var content: Data](./update/content.md)
  A raw binary representation of the entry.
- [var contentType: UTType](./update/contenttype.md)
  A `UTType` identifying how to interpret [`content`](./update/content.md).
- [var metadata: GeneratedContent](./update/metadata.md)
  Metadata pertinent to the entry.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/dataentry/update)*