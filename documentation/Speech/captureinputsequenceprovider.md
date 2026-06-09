# CaptureInputSequenceProvider

**Framework**: Speech  
**Kind**: class

Reads from an AV capture device such as a microphone, providing the captured audio in a format suitable for analysis by a speech analyzer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class CaptureInputSequenceProvider
```

## Topics

### Creating a provider
- [static func providerWithSession(from: AVCaptureDevice, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from an audio capture device, and configures a new audio capture session with that device.
- [static func provider(from: AVCaptureDevice, in: AVCaptureSession, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](captureinputsequenceprovider/provider(from:in:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from an audio capture device.
- [init(session: AVCaptureSession, analyzerFormat: AVAudioFormat, priority: TaskPriority?) throws](captureinputsequenceprovider/init(session:analyzerformat:priority:).md)
  Creates an input sequence provider.
### Obtaining an input sequence
- [var analyzerInputs: some Sendable & AsyncSequence<AnalyzerInput, any Error>](captureinputsequenceprovider/analyzerinputs.md)
  A new sequence of speech analyzer input objects containing captured audio.
### Working with a capture session
- [var captureSession: AVCaptureSession](captureinputsequenceprovider/capturesession.md)
  The underlying capture session.
- [var captureAudioDataOutput: AVCaptureAudioDataOutput](captureinputsequenceprovider/captureaudiodataoutput.md)
  An audio data output that routes and converts captured audio buffers to async sequences.

## See Also

- [class AssetInputSequenceProvider](assetinputsequenceprovider.md)
  Reads from an audio file or asset, providing its audio in a format suitable for analysis by a speech analyzer.
- [class AnalyzerInputConverter](analyzerinputconverter.md)
  Converts audio buffers to a format suitable for analysis by a speech analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider)*