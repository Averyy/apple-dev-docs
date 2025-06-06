# AVCapturePhotoOutput.CaptureReadiness.ready

**Framework**: AVFoundation  
**Kind**: case

Indicates that the output is ready to receive new requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
case ready
```

## See Also

- [AVCapturePhotoOutput.CaptureReadiness.sessionNotRunning](avcapturephotooutput/capturereadiness-swift.enum/sessionnotrunning.md)
  Indicates that the session isn’t running and the output isn’t ready to receive requests.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyMomentarily](avcapturephotooutput/capturereadiness-swift.enum/notreadymomentarily.md)
  Indicates that the output isn’t ready to receive requests, but may be ready shortly.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForCapture](avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforcapture.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForProcessing](avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforprocessing.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/ready)*