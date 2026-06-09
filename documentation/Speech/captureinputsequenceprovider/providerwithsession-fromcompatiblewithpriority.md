# providerWithSession(from:compatibleWith:priority:)

**Framework**: Speech  
**Kind**: method

Returns an input sequence provider that reads from an audio capture device, and configures a new audio capture session with that device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func providerWithSession(from captureDevice: AVCaptureDevice, compatibleWith modules: [any SpeechModule], priority: TaskPriority? = nil) async throws -> CaptureInputSequenceProvider
```

#### Return Value

An instance of this class.

#### Discussion

This method also creates and configures a new `AVCaptureSession` with default settings. Initializing a session can take some time; you should call this method in a background task.

Use the [`captureSession`](captureinputsequenceprovider/capturesession.md) property to start, stop, or otherwise manage the capture session.

> **Note**: On iOS, tvOS, visionOS, and watchOS platforms, this method automatically configures your application’s default `AVAudioSession`. To avoid this behavior, call [`provider(from:in:compatibleWith:priority:)`](captureinputsequenceprovider/provider(from:in:compatiblewith:priority:).md) instead.

## Parameters

- `captureDevice`: The capture device to use.
- `modules`: The speech modules that will analyze the audio.
- `priority`: The desired priority of the audio-capture task.

## See Also

- [static func provider(from: AVCaptureDevice, in: AVCaptureSession, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> CaptureInputSequenceProvider](captureinputsequenceprovider/provider(from:in:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from an audio capture device.
- [init(session: AVCaptureSession, analyzerFormat: AVAudioFormat, priority: TaskPriority?) throws](captureinputsequenceprovider/init(session:analyzerformat:priority:).md)
  Creates an input sequence provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:))*