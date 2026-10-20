# AVCapturePhotoOutput.CaptureReadiness.notReadyMomentarily

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

Indicates that the output isn’t ready to receive requests, but may be ready shortly.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
case notReadyMomentarily
```

```c
AVCapturePhotoOutputCaptureReadinessNotReadyMomentarily
```

## See Also

### Readiness states
- [AVCapturePhotoOutput.CaptureReadiness.sessionNotRunning](./sessionnotrunning.md)
  Indicates that the session isn’t running and the output isn’t ready to receive requests.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForCapture](./notreadywaitingforcapture.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForProcessing](./notreadywaitingforprocessing.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.
- [AVCapturePhotoOutput.CaptureReadiness.ready](./ready.md)
  Indicates that the output is ready to receive new requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/notreadymomentarily)*