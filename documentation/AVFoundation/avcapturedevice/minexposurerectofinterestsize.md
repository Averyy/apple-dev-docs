# minExposureRectOfInterestSize

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
var minExposureRectOfInterestSize: CGSize { get }
```

#### Discussion

Returns the minimum size that can be used when specifying a rectangle of interest.

The size returned is in normalized coordinates, and will depend on the current active format. If isExposureRectOfInterestSupported returns NO, this property will return { 0, 0 }.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minexposurerectofinterestsize)*