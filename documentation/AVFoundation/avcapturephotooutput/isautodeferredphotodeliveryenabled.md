# isAutoDeferredPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the enabled state of automatic deferred photo delivery.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var isAutoDeferredPhotoDeliveryEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isAutoDeferredPhotoDeliveryEnabled) BOOL autoDeferredPhotoDeliveryEnabled;
```

## Discussion

Changing this value requires a lengthy reconfiguration of the capture pipeline, so you should set this property before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md) on the capture session.

Setting this property to [`true`](../../Swift/true.md) throws an invalid argument exception the value of [`isAutoDeferredPhotoDeliverySupported`](./isautodeferredphotodeliverysupported.md) is [`false`](../../Swift/false.md).

## See Also

### Managing responsive capture
- [var captureReadiness: AVCapturePhotoOutput.CaptureReadiness](./capturereadiness-swift.property.md)
  A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [AVCapturePhotoOutput.CaptureReadiness](./capturereadiness-swift.enum.md)
  Constants that indicate whether the output is ready to receive capture requests.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isautodeferredphotodeliveryenabled)*