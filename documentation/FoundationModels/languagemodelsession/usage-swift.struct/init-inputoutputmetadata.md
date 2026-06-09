# init(input:output:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates a usage value with the given token counts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(input: LanguageModelSession.Usage.Input, output: LanguageModelSession.Usage.Output, metadata: [String : any Sendable & Codable & Equatable] = [:])
```

## Parameters

- `input`: Token counts for the transcript.
- `output`: Token counts for the response.
- `metadata`: Additional usage statistics from the language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/init(input:output:metadata:))*