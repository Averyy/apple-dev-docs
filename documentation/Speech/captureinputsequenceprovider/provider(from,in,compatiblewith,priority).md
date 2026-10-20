# provider(from:in:compatibleWith:priority:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Returns an input sequence provider that reads from an audio capture device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
static func provider(from captureDevice: AVCaptureDevice, in session: AVCaptureSession, compatibleWith modules: [any SpeechModule], priority: TaskPriority? = nil) async throws -> CaptureInputSequenceProvider
```

#### Return Value

An instance of this class.

#### Discussion

This method also creates an `AVCaptureAudioDataOutput` object suitable for adding to an existing `AVCaptureSession`. It does not reconfigure or alter the session.

Use the [`captureAudioDataOutput`](./captureaudiodataoutput.md) property to access the output object and add it to your session.

## Parameters

- `captureDevice`: The capture device to use.
- `session`: The capture session that manages the audio capture operation.
- `modules`: The speech modules that will analyze the audio.
- `priority`: The desired priority of the audio-capture task.

## See Also

### Creating a provider
- [static func providerWithSession(from: AVCaptureDevice, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](./providerwithsession%28from,compatiblewith,priority%29.md)
  Returns an input sequence provider that reads from an audio capture device, and configures a new audio capture session with that device.
- [init(session: AVCaptureSession, analyzerFormat: AVAudioFormat, priority: TaskPriority?) throws](./init%28session,analyzerformat,priority%29.md)
  Creates an input sequence provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/provider(from:in:compatiblewith:priority:))*