# isCinematicVideoCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A BOOL value specifying whether the Cinematic Video effect is being applied to any movie file output, video data output, metadata output, or video preview layer added to the capture session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isCinematicVideoCaptureEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isCinematicVideoCaptureEnabled) BOOL cinematicVideoCaptureEnabled;
```

#### Discussion

Default is `false`. Set to `true` to enable support for Cinematic Video capture.

When you set this property to `true`, your input’s associated [`focusMode`](../avcapturedevice/focusmode-swift.property.md) changes to `AVCaptureFocusModeContinuousAutoFocus`. While Cinematic Video capture is enabled, you are not permitted to change your device’s focus mode, and any attempt to do so results in an `NSInvalidArgumentException`. You may only set this property to `true` if [`isCinematicVideoCaptureSupported`](./iscinematicvideocapturesupported.md) is `true`.

> **Note**: Enabling Cinematic Video capture requires a lengthy reconfiguration of the capture render pipeline, so if you intend to capture Cinematic Video, you should set this property to `true` before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md) or within [`beginConfiguration()`](../avcapturesession/beginconfiguration%28%29.md) and [`commitConfiguration()`](../avcapturesession/commitconfiguration%28%29.md) while running.

## See Also

### Configuring Cinematic video capture
- [var isCinematicVideoCaptureSupported: Bool](./iscinematicvideocapturesupported.md)
  A BOOL value specifying whether Cinematic Video capture is supported.
- [var simulatedAperture: Float](./simulatedaperture.md)
  Shallow depth of field simulated aperture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/iscinematicvideocaptureenabled)*