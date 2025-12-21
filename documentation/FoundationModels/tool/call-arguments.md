# call(arguments:)

**Framework**: Foundation Models  
**Kind**: method  
**Required**: Yes

A language model will call this method when it wants to leverage this tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func call(arguments: Self.Arguments) async throws -> Self.Output
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Discussion

If errors are throw in the body of this method, they will be wrapped in a [`LanguageModelSession.ToolCallError`](languagemodelsession/toolcallerror.md) and rethrown at the call site of [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md).

> **Note**: This method may be invoked concurrently with itself or with other tools.

## See Also

- [associatedtype Arguments : ConvertibleFromGeneratedContent](tool/arguments.md)
  The arguments that this tool should accept.
- [associatedtype Output : PromptRepresentable](tool/output.md)
  The output that this tool produces for the language model to reason about in subsequent interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/call(arguments:))*