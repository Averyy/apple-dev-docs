# SystemLanguageModel.TokenUsage

**Framework**: Foundation Models  
**Kind**: struct

Token usage information for a prompt or transcript.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
struct TokenUsage
```

#### Overview

Provides the total number of tokens used.

## Topics

### Getting the token count
- [var tokenCount: Int](systemlanguagemodel/tokenusage/tokencount.md)
  The total token count.

## See Also

- [func tokenUsage(for:)](systemlanguagemodel/tokenusage(for:).md)
  Returns token usage information for the specified prompt.
- [func tokenUsage(for: Instructions, tools: [any Tool]) async throws -> SystemLanguageModel.TokenUsage](systemlanguagemodel/tokenusage(for:tools:).md)
  Returns token usage information for the specified instructions and tools.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/tokenusage)*