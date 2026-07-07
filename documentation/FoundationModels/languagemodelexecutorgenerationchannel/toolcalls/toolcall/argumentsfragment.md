# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment

**Framework**: Foundation Models  
**Kind**: struct

Append argument text to this tool call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ArgumentsFragment
```

#### Overview

The first event for a given id opens the tool call (using `name` from the enclosing [`LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall`](languagemodelexecutorgenerationchannel/toolcalls/toolcall.md)); subsequent events append additional argument text.

## Topics

### Handling the arguments fragment
- [var content: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/argumentsfragment/content.md)
- [var tokenCount: Int](languagemodelexecutorgenerationchannel/toolcalls/toolcall/argumentsfragment/tokencount.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct.md)
  An operation that can be performed on a tool call.
- [var id: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/id.md)
  The identifier for the tool call.
- [var name: String](languagemodelexecutorgenerationchannel/toolcalls/toolcall/name.md)
  The name of the tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/argumentsfragment)*