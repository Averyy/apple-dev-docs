# AVCapturePhotoOutput.CaptureReadiness

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate whether the output is ready to receive capture requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
enum CaptureReadiness
```

## Topics

### Readiness states
- [AVCapturePhotoOutput.CaptureReadiness.sessionNotRunning](avcapturephotooutput/capturereadiness-swift.enum/sessionnotrunning.md)
  Indicates that the session isn’t running and the output isn’t ready to receive requests.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyMomentarily](avcapturephotooutput/capturereadiness-swift.enum/notreadymomentarily.md)
  Indicates that the output isn’t ready to receive requests, but may be ready shortly.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForCapture](avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforcapture.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForProcessing](avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforprocessing.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.
- [AVCapturePhotoOutput.CaptureReadiness.ready](avcapturephotooutput/capturereadiness-swift.enum/ready.md)
  Indicates that the output is ready to receive new requests.
### Initializers
- [init?(rawValue: Int)](avcapturephotooutput/capturereadiness-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var captureReadiness: AVCapturePhotoOutput.CaptureReadiness](avcapturephotooutput/capturereadiness-swift.property.md)
  A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [var isAutoDeferredPhotoDeliveryEnabled: Bool](avcapturephotooutput/isautodeferredphotodeliveryenabled.md)
  A Boolean value that indicates the enabled state of automatic deferred photo delivery.
- [var isAutoDeferredPhotoDeliverySupported: Bool](avcapturephotooutput/isautodeferredphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [var isFastCapturePrioritizationSupported: Bool](avcapturephotooutput/isfastcaptureprioritizationsupported.md)
  A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [var isFastCapturePrioritizationEnabled: Bool](avcapturephotooutput/isfastcaptureprioritizationenabled.md)
  A Boolean value that indicates whether the output enables fast capture prioritization.
- [var isResponsiveCaptureSupported: Bool](avcapturephotooutput/isresponsivecapturesupported.md)
  A Boolean value that indicates whether the photo output supports responsive capture.
- [var isResponsiveCaptureEnabled: Bool](avcapturephotooutput/isresponsivecaptureenabled.md)
  A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [var isZeroShutterLagSupported: Bool](avcapturephotooutput/iszeroshutterlagsupported.md)
  A Boolean value that indicates whether the photo output supports zero shutter lag.
- [var isZeroShutterLagEnabled: Bool](avcapturephotooutput/iszeroshutterlagenabled.md)
  A Boolean value that indicates whether the photo output configuration enables zero shutter lag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum)*