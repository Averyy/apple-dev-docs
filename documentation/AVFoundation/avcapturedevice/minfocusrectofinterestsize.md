# minFocusRectOfInterestSize

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
var minFocusRectOfInterestSize: CGSize { get }
```

#### Discussion

The size returned is in normalized coordinates, and depends on the current [`activeFormat`](avcapturedevice/activeformat.md). If [`isFocusRectOfInterestSupported`](avcapturedevice/isfocusrectofinterestsupported.md) returns `false`, this property returns { 0, 0 }.

## See Also

- [var isFocusRectOfInterestSupported: Bool](avcapturedevice/isfocusrectofinterestsupported.md)
  Whether the receiver supports focus rectangles of interest.
- [var focusRectOfInterest: CGRect](avcapturedevice/focusrectofinterest.md)
  The device’s current focus rectangle of interest, if it has one.
- [func defaultRectForFocusPoint(ofInterest: CGPoint) -> CGRect](avcapturedevice/defaultrectforfocuspoint(ofinterest:).md)
  The default rectangle of interest used for a given focus point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minfocusrectofinterestsize)*