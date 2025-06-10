# isCinematicVideoCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var isCinematicVideoCaptureEnabled: Bool { get set }
```

#### Discussion

A BOOL value specifying whether the Cinematic Video effect is applied to any AVCaptureMovieFileOutput, AVCaptureVideoDataOutput, AVCaptureMetadataOutput, and AVCaptureVideoPreviewLayer added to the same capture session.

Default is NO. Set to YES to enable support for Cinematic Video capture.

When set to YES, the corresponding AVCaptureDevice’s focusMode will be updated to AVCaptureFocusModeContinuousAutoFocus. While this is property is YES any attempt to change the focus mode will result in an exception.

This property may only be set to YES if cinematicVideoCaptureSupported is YES. Enabling Cinematic Video capture requires a lengthy reconfiguration of the capture render pipeline, so if you intend to capture Cinematic Video, you should set this property to YES before calling -[AVCaptureSession startRunning] or within -[AVCaptureSession beginConfiguration] and -[AVCaptureSession commitConfiguration] while running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/iscinematicvideocaptureenabled)*