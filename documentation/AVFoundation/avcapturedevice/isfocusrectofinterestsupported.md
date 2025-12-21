# isFocusRectOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property

Whether the receiver supports focus rectangles of interest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isFocusRectOfInterestSupported: Bool { get }
```

#### Discussion

You may only set the device’s [`focusRectOfInterest`](avcapturedevice/focusrectofinterest.md) property if this property returns `true`.

## See Also

- [var focusRectOfInterest: CGRect](avcapturedevice/focusrectofinterest.md)
  The device’s current focus rectangle of interest, if it has one.
- [var minFocusRectOfInterestSize: CGSize](avcapturedevice/minfocusrectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.
- [func defaultRectForFocusPoint(ofInterest: CGPoint) -> CGRect](avcapturedevice/defaultrectforfocuspoint(ofinterest:).md)
  The default rectangle of interest used for a given focus point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfocusrectofinterestsupported)*