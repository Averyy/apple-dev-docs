# captureSession

**Framework**: Speech  
**Kind**: property

The underlying capture session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var captureSession: AVCaptureSession { get }
```

#### Discussion

This property’s value is the new capture session created by [`providerWithSession(from:compatibleWith:priority:)`](captureinputsequenceprovider/providerwithsession(from:compatiblewith:priority:).md) or the existing capture session passed to [`provider(from:in:compatibleWith:priority:)`](captureinputsequenceprovider/provider(from:in:compatiblewith:priority:).md) or the initializer.

Use the methods of `AVCaptureSession` to start, stop, or manage the capture session.

## See Also

- [var captureAudioDataOutput: AVCaptureAudioDataOutput](captureinputsequenceprovider/captureaudiodataoutput.md)
  An audio data output that routes and converts captured audio buffers to async sequences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/capturesession)*