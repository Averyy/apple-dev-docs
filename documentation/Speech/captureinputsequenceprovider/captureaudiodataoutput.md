# captureAudioDataOutput

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

An audio data output that routes and converts captured audio buffers to async sequences.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
final var captureAudioDataOutput: AVCaptureAudioDataOutput { get }
```

#### Discussion

Add this output to an existing capture session. Calling [`providerWithSession(from:compatibleWith:priority:)`](./providerwithsession%28from,compatiblewith,priority%29.md) automatically adds this output to the session it creates.

Do not modify the output’s sample buffer delegate or callback queue.

## See Also

### Working with a capture session
- [var captureSession: AVCaptureSession](./capturesession.md)
  The underlying capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/captureaudiodataoutput)*