# AVCapturePhotoOutput.CaptureReadiness

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCapturePhotoOutputCaptureReadiness : NSInteger;
```

## Topics

### Readiness states
- [AVCapturePhotoOutput.CaptureReadiness.sessionNotRunning](./capturereadiness-swift.enum/sessionnotrunning.md)
  Indicates that the session isn’t running and the output isn’t ready to receive requests.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyMomentarily](./capturereadiness-swift.enum/notreadymomentarily.md)
  Indicates that the output isn’t ready to receive requests, but may be ready shortly.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForCapture](./capturereadiness-swift.enum/notreadywaitingforcapture.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForProcessing](./capturereadiness-swift.enum/notreadywaitingforprocessing.md)
  Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.
- [AVCapturePhotoOutput.CaptureReadiness.ready](./capturereadiness-swift.enum/ready.md)
  Indicates that the output is ready to receive new requests.
### Initializers
- [init?(rawValue: Int)](./capturereadiness-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing responsive capture
- [var captureReadiness: AVCapturePhotoOutput.CaptureReadiness](./capturereadiness-swift.property.md)
  A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [var isAutoDeferredPhotoDeliveryEnabled: Bool](./isautodeferredphotodeliveryenabled.md)
  A Boolean value that indicates the enabled state of automatic deferred photo delivery.
- [var isAutoDeferredPhotoDeliverySupported: Bool](./isautodeferredphotodeliverysupported.md)
  A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [var isFastCapturePrioritizationSupported: Bool](./isfastcaptureprioritizationsupported.md)
  A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [var isFastCapturePrioritizationEnabled: Bool](./isfastcaptureprioritizationenabled.md)
  A Boolean value that indicates whether the output enables fast capture prioritization.
- [var isResponsiveCaptureSupported: Bool](./isresponsivecapturesupported.md)
  A Boolean value that indicates whether the photo output supports responsive capture.
- [var isResponsiveCaptureEnabled: Bool](./isresponsivecaptureenabled.md)
  A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [var isZeroShutterLagSupported: Bool](./iszeroshutterlagsupported.md)
  A Boolean value that indicates whether the photo output supports zero shutter lag.
- [var isZeroShutterLagEnabled: Bool](./iszeroshutterlagenabled.md)
  A Boolean value that indicates whether the photo output configuration enables zero shutter lag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum)*