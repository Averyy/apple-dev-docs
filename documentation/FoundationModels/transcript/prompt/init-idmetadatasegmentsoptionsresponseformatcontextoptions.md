# init(id:metadata:segments:options:responseFormat:contextOptions:)

**Framework**: Foundation Models  
**Kind**: init

Creates a prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(id: String = UUID().uuidString, metadata: [String : any Codable & Sendable & Equatable] = [:], segments: [Transcript.Segment], options: GenerationOptions = GenerationOptions(), responseFormat: Transcript.ResponseFormat? = nil, contextOptions: ContextOptions = ContextOptions())
```

## Parameters

- `id`: A [`Generable`](generable.md) type to use as the response format.
- `metadata`: Metadata provided as part of this prompt.
- `segments`: An array of segments that make up the prompt.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `responseFormat`: A response format that describes the output structure.
- `contextOptions`: Settings that configure how the model is prompted

## See Also

- [init(id: String, segments: [Transcript.Segment], options: GenerationOptions, responseFormat: Transcript.ResponseFormat?)](transcript/prompt/init(id:segments:options:responseformat:).md)
  Creates a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/prompt/init(id:metadata:segments:options:responseformat:contextoptions:))*