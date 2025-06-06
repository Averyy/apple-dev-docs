# AVVideoScalingModeFit

**Framework**: AVFoundation  
**Kind**: var

The string identifier for scaling a video to fit the surrounding view’s dimensions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let AVVideoScalingModeFit: String
```

#### Discussion

This mode crops the video to remove the edge processing region, preserving the aspect ratio of the cropped source by reducing the specified width or height, if necessary. It doesn’t scale a small source up to larger dimensions.

## See Also

- [let AVVideoScalingModeKey: String](avvideoscalingmodekey.md)
  A key to retrieve the video scaling mode from a dictionary.
- [let AVVideoScalingModeResize: String](avvideoscalingmoderesize.md)
  The string identifier for resizing a video to fit the surrounding view’s dimensions.
- [let AVVideoScalingModeResizeAspect: String](avvideoscalingmoderesizeaspect.md)
  The string identifier for resizing a video to its surrounding view’s shorter dimension while preserving its aspect ratio.
- [let AVVideoScalingModeResizeAspectFill: String](avvideoscalingmoderesizeaspectfill.md)
  The string identifier for resizing a video to fit the surrounding view’s longer dimension while preserving aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoscalingmodefit)*