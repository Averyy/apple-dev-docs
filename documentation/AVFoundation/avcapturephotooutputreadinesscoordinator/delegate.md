# delegate

**Framework**: AVFoundation  
**Kind**: property

The coordinator’s delegate object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
weak var delegate: (any AVCapturePhotoOutputReadinessCoordinatorDelegate)? { get set }
```

#### Discussion

The capture delegate receives callbacks when the photo output’s captureReadiness changes. It calls its delegate on the main queue, which allows you to perform user interface updates directly from the delegate’s [`readinessCoordinator(_:captureReadinessDidChange:)`](avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(_:capturereadinessdidchange:).md) method.

The coordinator provides an initial value to the delegate when you first set it on this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/delegate)*