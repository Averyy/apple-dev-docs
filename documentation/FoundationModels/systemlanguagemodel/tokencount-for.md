# tokenCount(for:)

**Framework**: Foundation Models  
**Kind**: method

Returns the token count for the specified instructions.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func tokenCount(for instructions: Instructions) async throws -> Int
```

#### Return Value

The token count for the instructions.

## Parameters

- `instructions`: The instructions to calculate the token count for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/tokencount(for:))*