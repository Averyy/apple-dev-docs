# init(input:output:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates a usage update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent] = [:])
```

## Parameters

- `input`: Token counts for the transcript.
- `output`: Token counts for the response.
- `metadata`: Additional metadata to record alongside the token counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage/init(input:output:metadata:))*