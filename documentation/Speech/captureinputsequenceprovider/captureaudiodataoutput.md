# captureAudioDataOutput

**Framework**: Speech  
**Kind**: property

An audio data output that routes and converts captured audio buffers to async sequences.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
final var captureAudioDataOutput: AVCaptureAudioDataOutput { get }
```

#### Discussion

Add this output to an existing capture session. Calling [`providerWithSession(from:compatibleWith:priority:)`](captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:).md) automatically adds this output to the session it creates.

Do not modify the output’s sample buffer delegate or callback queue.

## See Also

- [var captureSession: AVCaptureSession](captureinputsequenceprovider/capturesession.md)
  The underlying capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/captureaudiodataoutput)*