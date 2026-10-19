# LanguageModelExecutorGenerationChannel.DataEntry.Update

**Framework**: Foundation Models  
**Kind**: struct

The content carried by an [`update(contentType:content:metadata:)`](languagemodelexecutorgenerationchannel/dataentry/action-swift.struct/update(contenttype:content:metadata:).md) action.

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
- [var content: Data](languagemodelexecutorgenerationchannel/dataentry/update/content.md)
  A raw binary representation of the entry.
- [var contentType: UTType](languagemodelexecutorgenerationchannel/dataentry/update/contenttype.md)
  A `UTType` identifying how to interpret [`content`](languagemodelexecutorgenerationchannel/dataentry/update/content.md).
- [var metadata: GeneratedContent](languagemodelexecutorgenerationchannel/dataentry/update/metadata.md)
  Metadata pertinent to the entry.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/dataentry/update)*