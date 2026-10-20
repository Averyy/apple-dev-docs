# setCinematicVideoTrackingFocus(detectedObjectID:focusMode:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Focus on and start tracking a detected object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

```objc
- (void) setCinematicVideoTrackingFocusWithDetectedObjectID:(NSInteger) detectedObjectID focusMode:(AVCaptureCinematicVideoFocusMode) focusMode;
```

## Parameters

- `detectedObjectID`: The ID of the detected object.
- `focusMode`: Specify whether to focus strongly or weakly.

## See Also

### Configuring Cinematic video
- [func setCinematicVideoFixedFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./setcinematicvideofixedfocus%28at,focusmode%29.md)
  Fix focus at a distance.
- [func setCinematicVideoTrackingFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./setcinematicvideotrackingfocus%28at,focusmode%29.md)
  Focus on and start tracking an object if it can be detected at the region specified by the point.
- [AVCaptureDevice.CinematicVideoFocusMode](./cinematicvideofocusmode.md)
  Constants indicating the focus behavior when recording a Cinematic Video.
- [struct AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus.md)
  An informative status about the scene observed by the device.
- [static let notEnoughLight: AVCaptureSceneMonitoringStatus](../avcapturescenemonitoringstatus/notenoughlight.md)
  The light level of the current scene is insufficient for the current set of features to function optimally.
- [var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus>](./cinematicvideocapturescenemonitoringstatuses.md)
  The current scene monitoring statuses related to Cinematic Video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid:focusmode:))*