# updateMetadata(_:)

**Framework**: Foundation Models  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func updateMetadata(_ values: [String : any Sendable & Codable & Equatable]) -> LanguageModelExecutorGenerationChannel.Response.Action
```

## See Also

- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/appendtext(_:segmentid:tokencount:).md)
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/replacetextsegment(_:segmentid:tokencount:).md)
- [LanguageModelExecutorGenerationChannel.Response.Action.removeAttachmentSegment(id:)](languagemodelexecutorgenerationchannel/response/action-swift.enum/removeattachmentsegment(id:).md)
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.enum/updateusage(input:output:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.enum/updatemetadata(_:)-swift.type.method)*