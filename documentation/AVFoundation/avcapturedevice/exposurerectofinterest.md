# exposureRectOfInterest

**Framework**: AVFoundation  
**Kind**: property

The device’s current exposure rectangle of interest, if it has one.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var exposureRectOfInterest: CGRect { get set }
```

#### Discussion

The value of this property is a `CGRect` determining the device’s exposure rectangle of interest. Use this as an alternative to setting [`exposurePointOfInterest`](avcapturedevice/exposurepointofinterest.md), as it allows you to specify both a location and size. For example, a value of `CGRectMake(0, 0, 1, 1)` tells the device to use the entire field of view when determining the exposure, while `CGRectMake(0, 0, 0.25, 0.25)` indicates the top left sixteenth, and `CGRectMake(0.75, 0.75, 0.25, 0.25)` indicates the bottom right sixteenth. Setting [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) throws an `NSInvalidArgumentException` if [`isExposureRectOfInterestSupported`](avcapturedevice/isexposurerectofinterestsupported.md) returns `false`. Setting [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) throws an `NSInvalidArgumentException` if your provided rectangle’s size is smaller than the [`minExposureRectOfInterestSize`](avcapturedevice/minexposurerectofinterestsize.md). Setting [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) throws an `NSGenericException` if you call it without first obtaining exclusive access to the device using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md). Setting [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) updates the device’s [`exposurePointOfInterest`](avcapturedevice/exposurepointofinterest.md) to the center of your provided rectangle of interest. If you later set the device’s [`exposurePointOfInterest`](avcapturedevice/exposurepointofinterest.md), the [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) resets to the default sized rectangle of interest for the new exposure point of interest. If you change your [`activeFormat`](avcapturedevice/activeformat.md), the point of interest and rectangle of interest both revert to their default values. You can observe automatic changes to the device’s [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) by key-value observing this property.

> **Note**: Setting [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md) alone does not initiate an exposure operation. After setting [`exposureRectOfInterest`](avcapturedevice/exposurerectofinterest.md), set [`exposureMode`](avcapturedevice/exposuremode-swift.property.md) to apply the new rectangle of interest.

## See Also

- [var isExposureRectOfInterestSupported: Bool](avcapturedevice/isexposurerectofinterestsupported.md)
  Whether the device supports exposure rectangles of interest.
- [var minExposureRectOfInterestSize: CGSize](avcapturedevice/minexposurerectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.
- [func defaultRectForExposurePoint(ofInterest: CGPoint) -> CGRect](avcapturedevice/defaultrectforexposurepoint(ofinterest:).md)
  The default rectangle of interest used for a given exposure point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposurerectofinterest)*