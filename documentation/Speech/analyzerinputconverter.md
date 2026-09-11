# AnalyzerInputConverter

**Framework**: Speech  
**Kind**: class

Converts audio buffers to a format suitable for analysis by a speech analyzer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class AnalyzerInputConverter
```

## Topics

### Creating a converter
- [static func converter(compatibleWith: [any SpeechModule]) async throws -> AnalyzerInputConverter](analyzerinputconverter/converter(compatiblewith:).md)
  Returns an audio input converter compatible with the given modules.
- [init(analyzerFormat: AVAudioFormat, configurationHandler: ((AVAudioConverter) -> Void)?)](analyzerinputconverter/init(analyzerformat:configurationhandler:).md)
  Creates an audio input converter.
### Converting a buffer
- [func convert(AVAudioBuffer, at: AVAudioTime?) throws -> [AnalyzerInput]](analyzerinputconverter/convert(_:at:).md)
  Converts an audio buffer.
- [func flush() throws -> [AnalyzerInput]](analyzerinputconverter/flush.md)
  Completes pending audio conversions.

## See Also

- [class AssetInputSequenceProvider](assetinputsequenceprovider.md)
  Reads from an audio file or asset, providing its audio in a format suitable for analysis by a speech analyzer.
- [class CaptureInputSequenceProvider](captureinputsequenceprovider.md)
  Reads from an AV capture device such as a microphone, providing the captured audio in a format suitable for analysis by a speech analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinputconverter)*