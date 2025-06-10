# setCinematicVideoTrackingFocus(at:focusMode:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func setCinematicVideoTrackingFocus(at point: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

#### Discussion

Focus on and start tracking an object if it can be detected at the region specified by the point.

## Parameters

- `point`: A normalized point of interest (i.e., [0,1]) in the coordinate space of the device.
- `focusMode`: Specify whether to focus strongly or weakly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcinematicvideotrackingfocus(at:focusmode:))*