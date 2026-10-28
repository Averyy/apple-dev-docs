# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An operation that can be performed on a tool call.

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

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`appendArguments(_:tokenCount:)`](./action-swift.struct/appendarguments%28_,tokencount%29.md).

## Topics

### Tool call actions
- [static func appendArguments(String, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./action-swift.struct/appendarguments%28_,tokencount%29.md)
  Creates an action that appends argument text to the tool call.
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./action-swift.struct/updatemetadata%28_%29.md)
  Creates an action that replaces the metadata for a tool call.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Handling a tool call
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./action-swift.property.md)
  The action to perform.
- [var id: String](./id.md)
  The identifier for the tool call.
- [var name: String](./name.md)
  The name of the tool call.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment](./argumentsfragment.md)
  Argument text appended to this tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct)*