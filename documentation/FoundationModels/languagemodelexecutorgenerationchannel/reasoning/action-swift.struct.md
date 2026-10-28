# LanguageModelExecutorGenerationChannel.Reasoning.Action

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An operation that can be performed on a reasoning entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Action
```

## Overview

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`appendText(_:segmentID:tokenCount:)`](./action-swift.struct/appendtext%28_,segmentid,tokencount%29.md).

## Topics

### Reasoning actions
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./action-swift.struct/appendtext%28_,segmentid,tokencount%29.md)
  Creates an action that appends text to the entry’s current text segment.
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./action-swift.struct/replacetextsegment%28_,segmentid,tokencount%29.md)
  Creates an action that replaces the entry’s current text segment.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./action-swift.struct/updatemetadata%28_%29.md)
  Creates an action that replaces the entry’s metadata.
- [static func updateSignature(Data, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./action-swift.struct/updatesignature%28_,tokencount%29.md)
  Creates an action that replaces the reasoning entry’s signature.
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./action-swift.struct/updateusage%28input,output,metadata%29.md)
  Creates an action that replaces the entry’s token-usage totals.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Handling reasoning
- [var action: LanguageModelExecutorGenerationChannel.Reasoning.Action](./action-swift.property.md)
  The action to perform.
- [var entryID: String?](./entryid.md)
  The identifier for the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoning/action-swift.struct)*