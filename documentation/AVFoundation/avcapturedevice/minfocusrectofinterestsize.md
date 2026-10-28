# minFocusRectOfInterestSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CGSize minFocusRectOfInterestSize;
```

## Discussion

The size returned is in normalized coordinates, and depends on the current [`activeFormat`](./activeformat.md). If [`isFocusRectOfInterestSupported`](./isfocusrectofinterestsupported.md) returns `false`, this property returns { 0, 0 }.

## See Also

### Setting a focus rectangle of interest
- [var isFocusRectOfInterestSupported: Bool](./isfocusrectofinterestsupported.md)
  Whether the receiver supports focus rectangles of interest.
- [var focusRectOfInterest: CGRect](./focusrectofinterest.md)
  The device’s current focus rectangle of interest, if it has one.
- [func defaultRectForFocusPoint(ofInterest: CGPoint) -> CGRect](./defaultrectforfocuspoint%28ofinterest%29.md)
  The default rectangle of interest used for a given focus point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minfocusrectofinterestsize)*