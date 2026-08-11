# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action

**Framework**: Foundation Models  
**Kind**: struct

An operation that can be performed on a tool call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Action
```

#### Overview

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`appendArguments(_:tokenCount:)`](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/appendarguments(_:tokencount:).md).

## Topics

### Tool call actions
- [static func appendArguments(String, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/appendarguments(_:tokencount:).md)
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/updatemetadata(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.property.md)
  The action to perform.
- [var id: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/id.md)
  The identifier for the tool call.
- [var name: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/name.md)
  The name of the tool call.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment](languagemodelexecutorgenerationchannel/toolcalls/toolcall/argumentsfragment.md)
  Argument text appended to this tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct)*