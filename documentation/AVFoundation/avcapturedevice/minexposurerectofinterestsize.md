# minExposureRectOfInterestSize

**Framework**: AVFoundation  
**Kind**: property

The minimum size you may use when specifying a rectangle of interest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var minExposureRectOfInterestSize: CGSize { get }
```

#### Discussion

The size returned is in normalized coordinates, and depends on the current [`activeFormat`](avcapturedevice/activeformat.md). If [`isExposureRectOfInterestSupported`](avcapturedevice/isexposurerectofinterestsupported.md) returns `false`, this property returns { 0, 0 }.

## See Also

- [var isExposureRectOfInterestSupported: Bool](avcapturedevice/isexposurerectofinterestsupported.md)
  Whether the device supports exposure rectangles of interest.
- [var exposureRectOfInterest: CGRect](avcapturedevice/exposurerectofinterest.md)
  The device’s current exposure rectangle of interest, if it has one.
- [func defaultRectForExposurePoint(ofInterest: CGPoint) -> CGRect](avcapturedevice/defaultrectforexposurepoint(ofinterest:).md)
  The default rectangle of interest used for a given exposure point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minexposurerectofinterestsize)*