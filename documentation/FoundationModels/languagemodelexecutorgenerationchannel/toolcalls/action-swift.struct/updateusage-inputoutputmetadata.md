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
static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action
```

## See Also

- [static func toolCall(id: String, name: String, action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/toolcall(id:name:action:).md)
- [static func removeToolCall(id: String) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/removetoolcall(id:).md)
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/updatemetadata(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/updateusage(input:output:metadata:))*