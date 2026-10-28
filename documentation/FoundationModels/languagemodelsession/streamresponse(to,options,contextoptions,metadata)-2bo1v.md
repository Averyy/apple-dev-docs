# streamResponse(to:options:contextOptions:metadata:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Produces a response stream to a prompt.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final func streamResponse(to prompt: String, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(), metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> sending LanguageModelSession.ResponseStream<String>
```

**Other overloads**:

```swift
final func streamResponse(to prompt: Prompt, options: GenerationOptions = GenerationOptions(), contextOptions: ContextOptions = ContextOptions(), metadata: [String : any ConvertibleToGeneratedContent] = [:]) -> sending LanguageModelSession.ResponseStream<String>
```

## Return Value

A response stream that produces aggregated tokens.

## Discussion

> ❗ **Important**: If running in the background, use the non-streaming [`respond(to:options:)`](./respond%28to,options%29-6a2gb.md) method to reduce the likelihood of encountering [`LanguageModelError.rateLimited(_:)`](../languagemodelerror/ratelimited%28_%29.md) errors.

## Parameters

- `prompt`: A prompt for the model to respond to.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `contextOptions`: Settings that configure how the model is prompted.
- `metadata`: Metadata to attach to the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/streamresponse(to:options:contextoptions:metadata:)-2bo1v)*