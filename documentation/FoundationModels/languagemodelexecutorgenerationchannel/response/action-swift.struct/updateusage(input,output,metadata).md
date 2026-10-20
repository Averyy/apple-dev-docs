# updateUsage(input:output:metadata:)

**Framework**: Foundation Models  
**Kind**: method

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

- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/appendtext(_:segmentid:tokencount:).md)
  Creates an action that appends text to the entry’s current text segment.
- [static func removeAttachmentSegment(id: String) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/removeattachmentsegment(id:).md)
  Creates an action that removes an attachment segment from the entry.
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/replacetextsegment(_:segmentid:tokencount:).md)
  Creates an action that replaces the entry’s current text segment.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/updatemetadata(_:).md)
  Creates an action that replaces the entry’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.struct/updateusage(input:output:metadata:))*