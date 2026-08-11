# Arguments

**Framework**: Foundation Models  
**Kind**: associatedtype  
**Required**: Yes

The arguments that this tool should accept.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Arguments : ConvertibleFromGeneratedContent
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Discussion

Typically arguments are either a [`Generable`](generable.md) type or [`GeneratedContent`](generatedcontent.md).

## See Also

- [func call(arguments: Self.Arguments) async throws -> Self.Output](tool/call(arguments:).md)
  Performs the tool’s action when a language model wants to use this tool.
- [associatedtype Output : PromptRepresentable](tool/output.md)
  The output that this tool produces for the language model to reason about in subsequent interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/arguments)*