# defaultRectForFocusPoint(ofInterest:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

The default rectangle of interest used for a given focus point of interest.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func defaultRectForFocusPoint(ofInterest pointOfInterest: CGPoint) -> CGRect
```

```objc
- (CGRect) defaultRectForFocusPointOfInterest:(CGPoint) pointOfInterest;
```

#### Discussion

For example, pass `(0.5, 0.5)` to get the focus rectangle of interest used for the default focus point of interest at `(0.5, 0.5)`.

> **Note**: The particular default rectangle returned depends on the current focus mode.

This method returns `CGRectNull` if [`isFocusRectOfInterestSupported`](./isfocusrectofinterestsupported.md) returns `false`.

## Parameters

- `pointOfInterest`: The point of interest for which you want the default rectangle of interest.

## See Also

### Setting a focus rectangle of interest
- [var isFocusRectOfInterestSupported: Bool](./isfocusrectofinterestsupported.md)
  Whether the receiver supports focus rectangles of interest.
- [var focusRectOfInterest: CGRect](./focusrectofinterest.md)
  The device’s current focus rectangle of interest, if it has one.
- [var minFocusRectOfInterestSize: CGSize](./minfocusrectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/defaultrectforfocuspoint(ofinterest:))*