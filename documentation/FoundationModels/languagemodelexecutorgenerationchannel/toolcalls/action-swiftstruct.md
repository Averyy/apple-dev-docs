# LanguageModelExecutorGenerationChannel.ToolCalls.Action

**Framework**: Foundation Models  
**Kind**: struct

An operation that can be performed on a tool-calls entry.

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

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`toolCall(id:name:action:)`](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/toolcall(id:name:action:).md).

## Topics

### Tool calling actions
- [static func toolCall(id: String, name: String, action: LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/toolcall(id:name:action:).md)
- [static func removeToolCall(id: String) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/removetoolcall(id:).md)
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/updatemetadata(_:).md)
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct/updateusage(input:output:metadata:).md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.ToolCalls.Action](languagemodelexecutorgenerationchannel/toolcalls/action-swift.property.md)
  The action to perform.
- [var entryID: String?](languagemodelexecutorgenerationchannel/toolcalls/entryid.md)
  The identifier for the entry.
- [LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall](languagemodelexecutorgenerationchannel/toolcalls/toolcall.md)
  A per-tool-call event payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/action-swift.struct)*