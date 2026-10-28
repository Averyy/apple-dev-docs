# providerWithSession(from:compatibleWith:priority:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Returns an input sequence provider that reads from an audio capture device, and configures a new audio capture session with that device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func providerWithSession(from captureDevice: AVCaptureDevice, compatibleWith modules: [any SpeechModule], priority: TaskPriority? = nil) async throws -> CaptureInputSequenceProvider
```

## Return Value

An instance of this class.

## Discussion

This method also creates and configures a new `AVCaptureSession` with default settings. Initializing a session can take some time; you should call this method in a background task.

Use the [`captureSession`](./capturesession.md) property to start, stop, or otherwise manage the capture session.

> **Note**: On iOS, tvOS, visionOS, and watchOS platforms, this method automatically configures your application’s default `AVAudioSession`. To avoid this behavior, call [`provider(from:in:compatibleWith:priority:)`](./provider%28from,in,compatiblewith,priority%29.md) instead.

## Parameters

- `captureDevice`: The capture device to use.
- `modules`: The speech modules that will analyze the audio.
- `priority`: The desired priority of the audio-capture task.

## See Also

### Creating a provider
- [static func provider(from: AVCaptureDevice, in: AVCaptureSession, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](./provider%28from,in,compatiblewith,priority%29.md)
  Returns an input sequence provider that reads from an audio capture device.
- [init(session: AVCaptureSession, analyzerFormat: AVAudioFormat, priority: TaskPriority?) throws](./init%28session,analyzerformat,priority%29.md)
  Creates an input sequence provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:))*