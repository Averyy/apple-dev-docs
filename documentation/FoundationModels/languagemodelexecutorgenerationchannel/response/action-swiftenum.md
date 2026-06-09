# LanguageModelExecutorGenerationChannel.Response.Action

**Framework**: Foundation Models  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Action
```

## Topics

### Response action cases
- [LanguageModelExecutorGenerationChannel.Response.Action.appendText(_:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/appendtext(_:).md)
- [case replaceTextSegment(LanguageModelExecutorGenerationChannel.TextSegmentReplacement)](languagemodelexecutorgenerationchannel/response/action-swift.enum/replacetextsegment(_:).md)
- [LanguageModelExecutorGenerationChannel.Response.Action.addAttachmentSegment(_:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/addattachmentsegment(_:).md)
- [LanguageModelExecutorGenerationChannel.Response.Action.updateCustomSegment(_:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/updatecustomsegment(_:).md)
- [LanguageModelExecutorGenerationChannel.Response.Action.updateMetadata(_:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/updatemetadata(_:)-swift.enum.case.md)
- [LanguageModelExecutorGenerationChannel.Response.Action.updateUsage(_:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/updateusage(_:).md)
### Response action constants
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/appendtext(_:segmentid:tokencount:).md)
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/replacetextsegment(_:segmentid:tokencount:).md)
- [LanguageModelExecutorGenerationChannel.Response.Action.removeAttachmentSegment(id:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/removeattachmentsegment(id:).md)
- [static func updateMetadata([String : any Sendable & Codable & Equatable]) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/updatemetadata(_:)-swift.type.method.md)
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/updateusage(input:output:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.property.md)
  The action to perform.
- [var entryID: String?](languagemodelexecutorgenerationchannel/response/entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](languagemodelexecutorgenerationchannel/textsegmentreplacement.md)
  Replace a streaming entry’s current text segment with `content`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.enum)*