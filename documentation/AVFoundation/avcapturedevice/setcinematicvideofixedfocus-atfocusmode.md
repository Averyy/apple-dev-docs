# setCinematicVideoFixedFocus(at:focusMode:)

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
func setCinematicVideoFixedFocus(at point: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

#### Discussion

Fix focus at a distance.

The distance at which focus is set is determined internally using signals such as depth data.

## Parameters

- `point`: A normalized point of interest (i.e., [0,1]) in the coordinate space of the device.
- `focusMode`: Specify whether to focus strongly or weakly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcinematicvideofixedfocus(at:focusmode:))*