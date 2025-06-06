# readinessCoordinator(_:captureReadinessDidChange:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that the capture readiness state of a photo output changed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func readinessCoordinator(_ coordinator: AVCapturePhotoOutputReadinessCoordinator, captureReadinessDidChange captureReadiness: AVCapturePhotoOutput.CaptureReadiness)
```

#### Discussion

The system always performs this call on the main queue, so you can use it to update your user interface’s shutter button availability and appearance.

## Parameters

- `coordinator`: The delegate’s coordinator object.
- `captureReadiness`: An updated capture readiness value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(_:capturereadinessdidchange:))*