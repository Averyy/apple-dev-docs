# tokenUsage(for:)

**Framework**: Foundation Models  
**Kind**: method

Returns token usage information for the specified prompt.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func tokenUsage(for prompt: some PromptRepresentable) async throws -> SystemLanguageModel.TokenUsage
```

#### Return Value

A summary of token usage for the prompt.

## Parameters

- `prompt`: A prompt to calculate token usage for.

## See Also

- [func tokenUsage(for: Instructions, tools: [any Tool]) async throws -> SystemLanguageModel.TokenUsage](systemlanguagemodel/tokenusage(for:tools:).md)
  Returns token usage information for the specified instructions and tools.
- [SystemLanguageModel.TokenUsage](systemlanguagemodel/tokenusage.md)
  Token usage information for a prompt or transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/tokenusage(for:))*