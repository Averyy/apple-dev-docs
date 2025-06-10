# init(id:segments:options:responseFormat:)

**Framework**: Foundation Models  
**Kind**: init

Creates a prompt.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(id: String = UUID().uuidString, segments: [Transcript.Segment], options: GenerationOptions = GenerationOptions(), responseFormat: Transcript.ResponseFormat? = nil)
```

## Parameters

- `id`: A   type to use as the response format.
- `segments`: An array of segments that make up the prompt.
- `options`: Options that control how tokens are sampled from the distribution the model produces.
- `responseFormat`: A response format that describes the output structure.

## See Also

- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/prompt/init(id:segments:options:responseformat:))*