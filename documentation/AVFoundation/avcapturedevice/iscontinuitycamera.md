# isContinuityCamera

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device is a Continuity Camera.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var isContinuityCamera: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isContinuityCamera) BOOL continuityCamera;
```

#### Discussion

Continuity Camera enables you to use the rear camera system of iPhone as an external webcam in macOS.

## See Also

### Supporting Continuity Camera
- [class var systemPreferredCamera: AVCaptureDevice?](./systempreferredcamera.md)
  A camera the system prefers to use for video and photo capture.
- [class var userPreferredCamera: AVCaptureDevice?](./userpreferredcamera.md)
  A camera the user prefers to use for video and photo capture.
- [var companionDeskViewCamera: AVCaptureDevice?](./companiondeskviewcamera.md)
  A Desk View camera associated with a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscontinuitycamera)*