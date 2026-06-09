# LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action

**Framework**: Foundation Models  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Action
```

## Topics

### Tool call action cases
- [case appendArguments(LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.ArgumentsFragment)](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.enum/appendarguments(_:).md)
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action.updateMetadata(_:)](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.enum/updatemetadata(_:)-swift.enum.case.md)
### Tool call action constants
- [static func appendArguments(String, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.enum/appendarguments(_:tokencount:).md)
- [static func updateMetadata([String : any Sendable & Codable & Equatable]) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.enum/updatemetadata(_:)-swift.type.method.md)

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
  Append argument text to this tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.enum)*