# isExposureRectOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isExposureRectOfInterestSupported) BOOL exposureRectOfInterestSupported;
```

## Discussion

You may only set the device’s [`exposureRectOfInterest`](./exposurerectofinterest.md) property if this property returns `true`.

## See Also

### Setting an exposure rectangle of interest
- [var exposureRectOfInterest: CGRect](./exposurerectofinterest.md)
  The device’s current exposure rectangle of interest, if it has one.
- [var minExposureRectOfInterestSize: CGSize](./minexposurerectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.
- [func defaultRectForExposurePoint(ofInterest: CGPoint) -> CGRect](./defaultrectforexposurepoint%28ofinterest%29.md)
  The default rectangle of interest used for a given exposure point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposurerectofinterestsupported)*