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
static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action
```

## Parameters

- `input`: The token counts for the transcript submitted to the model.
- `output`: The token counts for the response the model produces.
- `metadata`: Additional metadata to record alongside the token counts.

## See Also

### Tool calling actions
- [static func toolCall(id: String, name: String, action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./toolcall%28id,name,action%29.md)
  Creates an action that routes an event to a specific tool call within the entry.
- [static func removeToolCall(id: String) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./removetoolcall%28id%29.md)
  Creates an action that removes a tool call.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./updatemetadata%28_%29.md)
  Creates an action that replaces the tool call’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/updateusage(input:output:metadata:))*