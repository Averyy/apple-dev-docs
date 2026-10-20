# LanguageModelExecutorGenerationChannel.DataEntry.Action

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An operation that can be performed on a data entry.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct Action
```

#### Overview

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`update(contentType:content:metadata:)`](./action-swift.struct/update%28contenttype,content,metadata%29.md).

## Topics

### Type Methods
- [static func update(contentType: UTType, content: Data, metadata: GeneratedContent) -> LanguageModelExecutorGenerationChannel.DataEntry.Action](./action-swift.struct/update%28contenttype,content,metadata%29.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/dataentry/action-swift.struct)*