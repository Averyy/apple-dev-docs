# notEnoughLight

**Framework**: AVFoundation  
**Kind**: property

The light level of the current scene is insufficient for the current set of features to function optimally.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
static let notEnoughLight: AVCaptureSceneMonitoringStatus
```

## See Also

- [func setCinematicVideoFixedFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](avcapturedevice/setcinematicvideofixedfocus(at:focusmode:).md)
  Fix focus at a distance.
- [func setCinematicVideoTrackingFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](avcapturedevice/setcinematicvideotrackingfocus(at:focusmode:).md)
  Focus on and start tracking an object if it can be detected at the region specified by the point.
- [func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid:focusmode:).md)
  Focus on and start tracking a detected object.
- [AVCaptureDevice.CinematicVideoFocusMode](avcapturedevice/cinematicvideofocusmode.md)
  Constants indicating the focus behavior when recording a Cinematic Video.
- [struct AVCaptureSceneMonitoringStatus](avcapturescenemonitoringstatus.md)
  An informative status about the scene observed by the device.
- [var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus>](avcapturedevice/cinematicvideocapturescenemonitoringstatuses.md)
  The current scene monitoring statuses related to Cinematic Video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescenemonitoringstatus/notenoughlight)*