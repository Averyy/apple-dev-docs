# tokenUsage(for:tools:)

**Framework**: Foundation Models  
**Kind**: method

Returns token usage information for the specified instructions and tools.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func tokenUsage(for instructions: Instructions, tools: [any Tool] = []) async throws -> SystemLanguageModel.TokenUsage
```

#### Return Value

A summary of token usage for the instructions and tools.

#### Discussion

This method calculates the token count for a set of instructions and tool definitions. The token count includes both the instructions and the tool hints that would be included in the model’s context.

## Parameters

- `instructions`: Instructions to calculate token usage for.
- `tools`: An array of tools that will be available to the model. Defaults to an empty array if not specified.

## See Also

- [func tokenUsage(for:)](systemlanguagemodel/tokenusage(for:).md)
  Returns token usage information for the specified prompt.
- [SystemLanguageModel.TokenUsage](systemlanguagemodel/tokenusage.md)
  Token usage information for a prompt or transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/tokenusage(for:tools:))*