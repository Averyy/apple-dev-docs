# isFocusRectOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isFocusRectOfInterestSupported) BOOL focusRectOfInterestSupported;
```

#### Discussion

You may only set the device’s [`focusRectOfInterest`](./focusrectofinterest.md) property if this property returns `true`.

## See Also

### Setting a focus rectangle of interest
- [var focusRectOfInterest: CGRect](./focusrectofinterest.md)
  The device’s current focus rectangle of interest, if it has one.
- [var minFocusRectOfInterestSize: CGSize](./minfocusrectofinterestsize.md)
  The minimum size you may use when specifying a rectangle of interest.
- [func defaultRectForFocusPoint(ofInterest: CGPoint) -> CGRect](./defaultrectforfocuspoint%28ofinterest%29.md)
  The default rectangle of interest used for a given focus point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfocusrectofinterestsupported)*