# isExposureRectOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property

Whether the device supports exposure rectangles of interest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isExposureRectOfInterestSupported: Bool { get }
```

#### Discussion

You may only set the device’s [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) property if this property returns `true`.

## See Also

- [var exposureRectOfInterest: CGRect](avcapturedevice/exposurerectofinterest.md)
  The device’s current exposure rectangle of interest, if it has one.
- [var minExposureRectOfInterestSize: CGSize](avcapturedevice/minexposurerectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.
- [func defaultRectForExposurePoint(ofInterest: CGPoint) -> CGRect](avcapturedevice/defaultrectforexposurepoint(ofinterest:).md)
  The default rectangle of interest used for a given exposure point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposurerectofinterestsupported)*