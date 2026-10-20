# converter(compatibleWith:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Returns an audio input converter compatible with the given modules.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func converter(compatibleWith modules: [any SpeechModule]) async throws -> AnalyzerInputConverter
```

#### Return Value

An instance of this class.

## Parameters

- `modules`: The speech modules that will analyze the audio.

## See Also

### Creating a converter
- [init(analyzerFormat: AVAudioFormat, configurationHandler: ((AVAudioConverter) -> Void)?)](./init%28analyzerformat,configurationhandler%29.md)
  Creates an audio input converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinputconverter/converter(compatiblewith:))*