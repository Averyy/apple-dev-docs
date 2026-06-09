# AssetInputSequenceProvider

**Framework**: Speech  
**Kind**: class

Reads from an audio file or asset, providing its audio in a format suitable for analysis by a speech analyzer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class AssetInputSequenceProvider
```

## Topics

### Creating a provider
- [static func provider(from: AVAsset, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](assetinputsequenceprovider/provider(from:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from the first track of an asset or file.
- [static func provider(from: AVAsset, track: AVAssetTrack, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](assetinputsequenceprovider/provider(from:track:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from a track of an asset.
- [init(asset: AVAsset, track: AVAssetTrack, analyzerFormat: AVAudioFormat, priority: TaskPriority?)](assetinputsequenceprovider/init(asset:track:analyzerformat:priority:).md)
  Creates an input sequence provider.
### Obtaining an input sequence
- [var analyzerInputs: some Sendable & AsyncSequence<AnalyzerInput, any Error>](assetinputsequenceprovider/analyzerinputs.md)
  A new sequence of speech analyzer input objects containing audio from the asset or file.

## See Also

- [class CaptureInputSequenceProvider](captureinputsequenceprovider.md)
  Reads from an AV capture device such as a microphone, providing the captured audio in a format suitable for analysis by a speech analyzer.
- [class AnalyzerInputConverter](analyzerinputconverter.md)
  Converts audio buffers to a format suitable for analysis by a speech analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider)*