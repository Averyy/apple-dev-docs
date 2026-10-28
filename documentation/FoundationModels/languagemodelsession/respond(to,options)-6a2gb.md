# respond(to:options:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a response to a prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
nonisolated(nonsending) final func respond(to prompt: Prompt, options: GenerationOptions = GenerationOptions()) async throws -> LanguageModelSession.Response<String>
```

**Other overloads**:

```swift
@discardableResult
nonisolated(nonsending) final func respond(to prompt: String, options: GenerationOptions = GenerationOptions()) async throws -> LanguageModelSession.Response<String>
```

## Return Value

A string composed of the tokens produced by sampling model output.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `options`: Options that control how tokens are sampled from the distribution the model produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/respond(to:options:)-6a2gb)*