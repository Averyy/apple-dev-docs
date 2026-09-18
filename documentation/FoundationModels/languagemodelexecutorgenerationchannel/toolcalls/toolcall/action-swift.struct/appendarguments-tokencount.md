# appendArguments(_:tokenCount:)

**Framework**: Foundation Models  
**Kind**: method

Creates an action that appends argument text to the tool call.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func appendArguments(_ content: String, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action
```

## Parameters

- `content`: The argument text to append to the tool call.
- `tokenCount`: The number of the tokens the argument text carries.

## See Also

- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/updatemetadata(_:).md)
  Creates an action that replaces the metadata for a tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/appendarguments(_:tokencount:))*