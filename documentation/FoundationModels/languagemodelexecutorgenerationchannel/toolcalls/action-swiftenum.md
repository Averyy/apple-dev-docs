# LanguageModelExecutorGenerationChannel.ToolCalls.Action

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

### Tool calling for action cases
- [LanguageModelExecutorGenerationChannel.ToolCalls.Action.removeToolCall(id:)](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/removetoolcall(id:).md)
- [case toolCall(LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall)](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/toolcall(_:).md)
- [LanguageModelExecutorGenerationChannel.ToolCalls.Action.updateMetadata(_:)](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/updatemetadata(_:)-swift.enum.case.md)
- [LanguageModelExecutorGenerationChannel.ToolCalls.Action.updateUsage(_:)](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/updateusage(_:).md)
### Tool calling for action constants
- [static func toolCall(id: String, name: String, action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/toolcall(id:name:action:).md)
- [static func updateMetadata([String : any Sendable & Codable & Equatable]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/updatemetadata(_:)-swift.type.method.md)
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum/updateusage(input:output:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.property.md)
  The action to perform.
- [var entryID: String?](languagemodelexecutorgenerationchannel/toolcalls/entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall](languagemodelexecutorgenerationchannel/toolcalls/toolcall.md)
  A per-tool-call event payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/action-swift.enum)*