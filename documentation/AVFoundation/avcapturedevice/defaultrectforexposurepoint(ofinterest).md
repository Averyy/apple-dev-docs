# defaultRectForExposurePoint(ofInterest:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGRect) defaultRectForExposurePointOfInterest:(CGPoint) pointOfInterest;
```

#### Discussion

For example, pass `(0.5, 0.5)` to get the exposure rectangle of interest used for the default exposure point of interest at `(0.5, 0.5)`.

This method returns `CGRectNull` if [`isExposureRectOfInterestSupported`](./isexposurerectofinterestsupported.md) returns `false`.

## Parameters

- `pointOfInterest`: The point of interest for which you want the default rectangle of interest.

## See Also

### Setting an exposure rectangle of interest
- [var isExposureRectOfInterestSupported: Bool](./isexposurerectofinterestsupported.md)
  Whether the device supports exposure rectangles of interest.
- [var exposureRectOfInterest: CGRect](./exposurerectofinterest.md)
  The device’s current exposure rectangle of interest, if it has one.
- [var minExposureRectOfInterestSize: CGSize](./minexposurerectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/defaultrectforexposurepoint(ofinterest:))*