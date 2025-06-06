# captureReadiness

**Framework**: AVFoundation  
**Kind**: property

A value that indicates whether the coordinator’s photo output is ready to respond to new capture requests in a timely manner.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var captureReadiness: AVCapturePhotoOutput.CaptureReadiness { get }
```

#### Discussion

The value incorporates the photo output’s [`captureReadiness`](avcapturephotooutput/capturereadiness-swift.property.md) property value and any requests registered by calling the [`startTrackingCaptureRequest(using:)`](avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using:).md) method. The system updates this value before calling the [`readinessCoordinator(_:captureReadinessDidChange:)`](avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(_:capturereadinessdidchange:).md) method.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/capturereadiness)*