# updateMetadata(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates an action that replaces the entry’s metadata.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func updateMetadata(_ values: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action
```

## Parameters

- `values`: The key-value pairs that replace the entry’s current metadata.

## See Also

### Response action constants
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](./appendtext%28_,segmentid,tokencount%29.md)
  Creates an action that appends text to the entry’s current text segment.
- [static func removeAttachmentSegment(id: String) -> LanguageModelExecutorGenerationChannel.Response.Action](./removeattachmentsegment%28id%29.md)
  Creates an action that removes an attachment segment from the entry.
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](./replacetextsegment%28_,segmentid,tokencount%29.md)
  Creates an action that replaces the entry’s current text segment.
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action](./updateusage%28input,output,metadata%29.md)
  Creates an action that replaces the entry’s token-usage totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.struct/updatemetadata(_:))*