# provider(from:in:compatibleWith:priority:)

**Framework**: Speech  
**Kind**: method

Returns an input sequence provider that reads from an audio capture device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
static func provider(from captureDevice: AVCaptureDevice, in session: AVCaptureSession, compatibleWith modules: [any SpeechModule], priority: TaskPriority? = nil) async throws -> CaptureInputSequenceProvider
```

#### Return Value

An instance of this class.

#### Discussion

This method also creates an `AVCaptureAudioDataOutput` object suitable for adding to an existing `AVCaptureSession`. It does not reconfigure or alter the session.

Use the [`captureAudioDataOutput`](captureinputsequenceprovider/captureaudiodataoutput.md) property to access the output object and add it to your session.

## Parameters

- `captureDevice`: The capture device to use.
- `session`: The capture session that manages the audio capture operation.
- `modules`: The speech modules that will analyze the audio.
- `priority`: The desired priority of the audio-capture task.

## See Also

- [static func providerWithSession(from: AVCaptureDevice, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from an audio capture device, and configures a new audio capture session with that device.
- [init(session: AVCaptureSession, analyzerFormat: AVAudioFormat, priority: TaskPriority?) throws](captureinputsequenceprovider/init(session:analyzerformat:priority:).md)
  Creates an input sequence provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/provider(from:in:compatiblewith:priority:))*