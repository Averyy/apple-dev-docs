# AVCaptureDevice.CinematicVideoFocusMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the focus behavior when recording a Cinematic Video.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
enum CinematicVideoFocusMode
```

```c
enum AVCaptureCinematicVideoFocusMode : NSInteger;
```

## Topics

### Focus modes
- [AVCaptureDevice.CinematicVideoFocusMode.none](./cinematicvideofocusmode/none.md)
  Indicates that no focus mode is specified, in which case weak focus is used as default.
- [AVCaptureDevice.CinematicVideoFocusMode.strong](./cinematicvideofocusmode/strong.md)
  Indicates that the subject should remain in focus until it exits the scene.
- [AVCaptureDevice.CinematicVideoFocusMode.weak](./cinematicvideofocusmode/weak.md)
  Indicates that the Cinematic Video algorithm should automatically adjust focus according to the prominence of the subjects in the scene.
### Initializers
- [init?(rawValue: Int)](./cinematicvideofocusmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring Cinematic video
- [func setCinematicVideoFixedFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./setcinematicvideofixedfocus%28at,focusmode%29.md)
  Fix focus at a distance.
- [func setCinematicVideoTrackingFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./setcinematicvideotrackingfocus%28at,focusmode%29.md)
  Focus on and start tracking an object if it can be detected at the region specified by the point.
- [func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./setcinematicvideotrackingfocus%28detectedobjectid,focusmode%29.md)
  Focus on and start tracking a detected object.
- [struct AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md)
  An informative status about the scene observed by the device.
- [static let notEnoughLight: AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus/notenoughlight.md)
  The light level of the current scene is insufficient for the current set of features to function optimally.
- [var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus>](./cinematicvideocapturescenemonitoringstatuses.md)
  The current scene monitoring statuses related to Cinematic Video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cinematicvideofocusmode)*