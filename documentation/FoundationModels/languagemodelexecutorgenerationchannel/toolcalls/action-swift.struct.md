# LanguageModelExecutorGenerationChannel.ToolCalls.Action

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An operation that can be performed on a tool-calls entry.

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

## Overview

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`toolCall(id:name:action:)`](./action-swift.struct/toolcall%28id,name,action%29.md).

## Topics

### Tool calling actions
- [static func toolCall(id: String, name: String, action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.struct/toolcall%28id,name,action%29.md)
  Creates an action that routes an event to a specific tool call within the entry.
- [static func removeToolCall(id: String) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.struct/removetoolcall%28id%29.md)
  Creates an action that removes a tool call.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.struct/updatemetadata%28_%29.md)
  Creates an action that replaces the tool call’s metadata.
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.struct/updateusage%28input,output,metadata%29.md)
  Creates an action that replaces the entry’s token-usage totals.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Handling tool calls
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.Action](./action-swift.property.md)
  The action to perform.
- [var entryID: String?](./entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall](./toolcall.md)
  A per-tool-call event payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct)*