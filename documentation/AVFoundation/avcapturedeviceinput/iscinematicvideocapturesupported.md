# isCinematicVideoCaptureSupported

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
var isCinematicVideoCaptureSupported: Bool { get }
```

#### Discussion

A BOOL value specifying whether Cinematic Video capture is supported.

With Cinematic Video capture, you get a simulated depth-of-field effect that keeps your subjects—people, pets, and more—in sharp focus while applying a pleasing blur to the background (or foreground). Depending on the focus mode (see `AVCaptureCinematicVideoFocusMode` for detail), the camera either uses machine learning to automatically detect and focus on subjects in the scene, or it fixes focus on a subject until it exits the scene. Cinematic Videos can be played back and edited using the Cinematic framework.

The simulated aperture can be adjusted before the recording starts using the simulatedAperture property. Focus transitions can be dynamically controlled using the Cinematic Video specific focus methods on AVCaptureDevice.

The resulted movie file can be played back and edited with the Cinematic framework.

This property returns YES if the session’s current configuration allows Cinematic Video capture. When switching cameras or formats this property may change. When this property changes from YES to NO, cinematicVideoCaptureEnabled also reverts to NO. If you’ve previously opted in for Cinematic Video capture and then change configurations, you may need to set cinematicVideoCaptureEnabled = YES again. This property is key-value observable.

AVCaptureDepthDataOutput is not supported when cinematicVideoCaptureEnabled is set to true. Running an AVCaptureSession with both of these features throws an NSInvalidArgumentException.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/iscinematicvideocapturesupported)*