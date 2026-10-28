# AVCaptureSceneMonitoringStatus

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

An informative status about the scene observed by the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
struct AVCaptureSceneMonitoringStatus
```

```c
typedef NSString * AVCaptureSceneMonitoringStatus;
```

## Overview

Some features have certain requirements on the scene (lighting condition for Cinematic Video, for example) to produce optimal results; these [`AVCaptureSceneMonitoringStatus`](./avcapturescenemonitoringstatus.md) string constants are used to represent such scene statuses for a given feature.

## Topics

### Status values
- [static let notEnoughLight: AVCaptureSceneMonitoringStatus](./avcapturescenemonitoringstatus/notenoughlight.md)
  The light level of the current scene is insufficient for the current set of features to function optimally.
### Initializers
- [init(rawValue: String)](./avcapturescenemonitoringstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring Cinematic video
- [func setCinematicVideoFixedFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./avcapturedevice/setcinematicvideofixedfocus%28at,focusmode%29.md)
  Fix focus at a distance.
- [func setCinematicVideoTrackingFocus(at: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./avcapturedevice/setcinematicvideotrackingfocus%28at,focusmode%29.md)
  Focus on and start tracking an object if it can be detected at the region specified by the point.
- [func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)](./avcapturedevice/setcinematicvideotrackingfocus%28detectedobjectid,focusmode%29.md)
  Focus on and start tracking a detected object.
- [AVCaptureDevice.CinematicVideoFocusMode](./avcapturedevice/cinematicvideofocusmode.md)
  Constants indicating the focus behavior when recording a Cinematic Video.
- [static let notEnoughLight: AVCaptureSceneMonitoringStatus](./avcapturescenemonitoringstatus/notenoughlight.md)
  The light level of the current scene is insufficient for the current set of features to function optimally.
- [var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus>](./avcapturedevice/cinematicvideocapturescenemonitoringstatuses.md)
  The current scene monitoring statuses related to Cinematic Video capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescenemonitoringstatus)*