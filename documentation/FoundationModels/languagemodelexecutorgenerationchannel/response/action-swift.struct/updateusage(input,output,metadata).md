# updateUsage(input:output:metadata:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates an action that replaces the entry’s token-usage totals.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> LanguageModelExecutorGenerationChannel.Response.Action
```

## Parameters

- `input`: The token counts for the transcript submitted to the model.
- `output`: The token counts for the response the model produces.
- `metadata`: Additional metadata to record alongside the token counts.

## See Also

### Response action constants
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](./appendtext%28_,segmentid,tokencount%29.md)
  Creates an action that appends text to the entry’s current text segment.
- [static func removeAttachmentSegment(id: String) -> LanguageModelExecutorGenerationChannel.Response.Action](./removeattachmentsegment%28id%29.md)
  Creates an action that removes an attachment segment from the entry.
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](./replacetextsegment%28_,segmentid,tokencount%29.md)
  Creates an action that replaces the entry’s current text segment.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action](./updatemetadata%28_%29.md)
  Creates an action that replaces the entry’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.struct/updateusage(input:output:metadata:))*