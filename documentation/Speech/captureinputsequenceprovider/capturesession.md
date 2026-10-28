# captureSession

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The underlying capture session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var captureSession: AVCaptureSession { get }
```

## Discussion

This property’s value is the new capture session created by [`providerWithSession(from:compatibleWith:priority:)`](./providerwithsession%28from,compatiblewith,priority%29.md) or the existing capture session passed to [`provider(from:in:compatibleWith:priority:)`](./provider%28from,in,compatiblewith,priority%29.md) or the initializer.

Use the methods of `AVCaptureSession` to start, stop, or manage the capture session.

## See Also

### Working with a capture session
- [var captureAudioDataOutput: AVCaptureAudioDataOutput](./captureaudiodataoutput.md)
  An audio data output that routes and converts captured audio buffers to async sequences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/captureinputsequenceprovider/capturesession)*