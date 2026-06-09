# init(session:analyzerFormat:priority:)

**Framework**: Speech  
**Kind**: init

Creates an input sequence provider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
init(session: AVCaptureSession, analyzerFormat: AVAudioFormat, priority: TaskPriority?) throws
```

#### Discussion

This initializer also creates an `AVCaptureAudioDataOutput` object suitable for adding to the given `AVCaptureSession`. It does not reconfigure or alter the session.

Use the [`captureAudioDataOutput`](captureinputsequenceprovider/captureaudiodataoutput.md) property to access the output object and add it to your session.

## Parameters

- `session`: The capture session that manages the audio capture operation.
- `analyzerFormat`: The audio format to convert the audio samples to. The audio format should be one supported by the speech analyzer’s modules.
- `priority`: The desired priority of the audio-capture task.

## See Also

- [static func providerWithSession(from: AVCaptureDevice, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from an audio capture device, and configures a new audio capture session with that device.
- [static func provider(from: AVCaptureDevice, in: AVCaptureSession, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](captureinputsequenceprovider/provider(from:in:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from an audio capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/init(session:analyzerformat:priority:))*