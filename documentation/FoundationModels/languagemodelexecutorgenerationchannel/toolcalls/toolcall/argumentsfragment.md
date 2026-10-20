# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Argument text appended to this tool call.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ArgumentsFragment
```

#### Overview

The first event for a given id opens the tool call (using `name` from the enclosing [`LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall`](../toolcall.md)); subsequent events append additional argument text.

## Topics

### Handling the arguments fragment
- [var content: String](./argumentsfragment/content.md)
  The argument text to append to the tool call.
- [var tokenCount: Int](./argumentsfragment/tokencount.md)
  The number of tokens the argument text carries.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Handling a tool call
- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./action-swift.property.md)
  The action to perform.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](./action-swift.struct.md)
  An operation that can be performed on a tool call.
- [var id: String](./id.md)
  The identifier for the tool call.
- [var name: String](./name.md)
  The name of the tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/argumentsfragment)*