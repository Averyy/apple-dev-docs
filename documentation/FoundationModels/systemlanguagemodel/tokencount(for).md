# tokenCount(for:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Returns the token count for the specified instructions.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
nonisolated(nonsending)
final func tokenCount(for instructions: Instructions) async throws -> Int
```

**Other overloads**:

```swift
nonisolated(nonsending)
final func tokenCount(for prompt: some PromptRepresentable) async throws -> Int
```

```swift
nonisolated(nonsending)
final func tokenCount(for schema: GenerationSchema) async throws -> Int
```

```swift
nonisolated(nonsending)
final func tokenCount(for tools: [any Tool]) async throws -> Int
```

```swift
nonisolated(nonsending)
final func tokenCount(for transcriptEntries: some Collection<Transcript.Entry>) async throws -> Int
```

## Mentions

- [Managing the context window](../managing-the-context-window.md)

## Return Value

The token count for the instructions.

## Parameters

- `instructions`: The instructions to calculate the token count for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/tokencount(for:))*