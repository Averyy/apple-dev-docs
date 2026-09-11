# updateUsage(input:output:metadata:)

**Framework**: Foundation Models  
**Kind**: method

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

## See Also

- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/appendtext(_:segmentid:tokencount:).md)
- [static func removeAttachmentSegment(id: String) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/removeattachmentsegment(id:).md)
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/replacetextsegment(_:segmentid:tokencount:).md)
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Response.Action](languagemodelexecutorgenerationchannel/response/action-swift.struct/updatemetadata(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/response/action-swift.struct/updateusage(input:output:metadata:))*