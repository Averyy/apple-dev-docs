# defaultRectForExposurePoint(ofInterest:)

**Framework**: AVFoundation  
**Kind**: method

The default rectangle of interest used for a given exposure point of interest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func defaultRectForExposurePoint(ofInterest pointOfInterest: CGPoint) -> CGRect
```

#### Discussion

For example, pass `(0.5, 0.5)` to get the exposure rectangle of interest used for the default exposure point of interest at `(0.5, 0.5)`.

This method returns `CGRectNull` if [`isExposureRectOfInterestSupported`](avcapturedevice/isexposurerectofinterestsupported.md) returns `false`.

## Parameters

- `pointOfInterest`: The point of interest for which you want the default rectangle of interest.

## See Also

- [var isExposureRectOfInterestSupported: Bool](avcapturedevice/isexposurerectofinterestsupported.md)
  Whether the device supports exposure rectangles of interest.
- [var exposureRectOfInterest: CGRect](avcapturedevice/exposurerectofinterest.md)
  The device’s current exposure rectangle of interest, if it has one.
- [var minExposureRectOfInterestSize: CGSize](avcapturedevice/minexposurerectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/defaultrectforexposurepoint(ofinterest:))*