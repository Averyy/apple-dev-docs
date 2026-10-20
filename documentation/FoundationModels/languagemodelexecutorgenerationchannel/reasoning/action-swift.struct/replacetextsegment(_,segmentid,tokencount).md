# replaceTextSegment(_:segmentID:tokenCount:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates an action that replaces the entry’s current text segment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func replaceTextSegment(_ text: String, segmentID: String? = nil, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action
```

## Parameters

- `text`: The replacement text for the segment.
- `segmentID`: The identifier of the segment to replace, or `nil` for the current segment.
- `tokenCount`: The number of the tokens the replacement text carries.

## See Also

### Reasoning actions
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./appendtext%28_,segmentid,tokencount%29.md)
  Creates an action that appends text to the entry’s current text segment.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./updatemetadata%28_%29.md)
  Creates an action that replaces the entry’s metadata.
- [static func updateSignature(Data, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./updatesignature%28_,tokencount%29.md)
  Creates an action that replaces the reasoning entry’s signature.
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](./updateusage%28input,output,metadata%29.md)
  Creates an action that replaces the entry’s token-usage totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/replacetextsegment(_:segmentid:tokencount:))*