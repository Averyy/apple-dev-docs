# LanguageModelExecutorGenerationChannel.Response.Action

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An operation that can be performed on a response entry.

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

#### Overview

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`appendText(_:segmentID:tokenCount:)`](./action-swift.struct/appendtext%28_,segmentid,tokencount%29.md).

## Topics

### Response action cases
- [static func addAttachmentSegment(Transcript.AttachmentSegment) -> LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.struct/addattachmentsegment%28_%29.md)
  Creates an action that adds an attachment segment to the entry.
### Response action constants
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.struct/appendtext%28_,segmentid,tokencount%29.md)
  Creates an action that appends text to the entry’s current text segment.
- [static func removeAttachmentSegment(id: String) -> LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.struct/removeattachmentsegment%28id%29.md)
  Creates an action that removes an attachment segment from the entry.
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.struct/replacetextsegment%28_,segmentid,tokencount%29.md)
  Creates an action that replaces the entry’s current text segment.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.struct/updatemetadata%28_%29.md)
  Creates an action that replaces the entry’s metadata.
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.struct/updateusage%28input,output,metadata%29.md)
  Creates an action that replaces the entry’s token-usage totals.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Handling a response
- [var action: LanguageModelExecutorGenerationChannel.Response.Action](./action-swift.property.md)
  The action to perform.
- [var entryID: String?](./entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](../textsegmentreplacement.md)
  A replacement for a streaming entry’s current text segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.struct)*