# updateMetadata(_:)

**Framework**: Foundation Models  
**Kind**: method

Creates an action that replaces the metadata for a tool call.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func updateMetadata(_ values: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action
```

## Parameters

- `values`: The key-value pairs that replace the current metadata for a tool call.

## See Also

- [static func appendArguments(String, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.ToolCalls.ToolCall.Action](languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/appendarguments(_:tokencount:).md)
  Creates an action that appends argument text to the tool call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/toolcalls/toolcall/action-swift.struct/updatemetadata(_:))*