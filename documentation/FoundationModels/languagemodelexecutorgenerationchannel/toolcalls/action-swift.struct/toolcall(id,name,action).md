# toolCall(id:name:action:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates an action that routes an event to a specific tool call within the entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func toolCall(id: String, name: String, action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action
```

## Parameters

- `id`: The identifier of the tool call the event targets.
- `name`: The name of the tool being called.
- `action`: The operation to perform on the tool call.

## See Also

### Tool calling actions
- [static func removeToolCall(id: String) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./removetoolcall%28id%29.md)
  Creates an action that removes a tool call.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./updatemetadata%28_%29.md)
  Creates an action that replaces the tool call’s metadata.
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./updateusage%28input,output,metadata%29.md)
  Creates an action that replaces the entry’s token-usage totals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/toolcall(id:name:action:))*