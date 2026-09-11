# init(analyzerFormat:configurationHandler:)

**Framework**: Speech  
**Kind**: init

Creates an audio input converter.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(analyzerFormat: AVAudioFormat, configurationHandler: ((AVAudioConverter) -> Void)? = nil)
```

## Parameters

- `analyzerFormat`: The audio format to convert the audio samples to. The audio format should be one supported by the speech analyzer’s modules.
- `configurationHandler`: A closure called to customize the instances of `AVAudioConverter` that this converter creates as needed. The closure takes the following parameter: - **audioConverter**: A newly-created instance of `AVAudioConverter`.

## See Also

- [static func converter(compatibleWith: [any SpeechModule]) async throws -> AnalyzerInputConverter](analyzerinputconverter/converter(compatiblewith:).md)
  Returns an audio input converter compatible with the given modules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinputconverter/init(analyzerformat:configurationhandler:))*