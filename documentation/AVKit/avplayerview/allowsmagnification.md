# allowsMagnification

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var allowsMagnification: Bool { get set }
```

```objc
@property (nonatomic, setter=setAllowsMagnification:) BOOL allowsMagnification;
```

## Discussion

The default value is `false`. This property only affects whether the magnify gesture triggers magnification. Your app can still programmatically change magnification even when the value of this is `false`, which matches the behavior of [`NSScrollView`](../../AppKit/nsscrollview.md).

## See Also

### Magnifying video
- [var magnification: CGFloat](./magnification.md)
  The factor by which the video’s view is currently scaled.
- [func setMagnification(CGFloat, centeredAt: CGPoint)](./setmagnification%28_,centeredat%29.md)
  Scales the video’s view by a specified factor, and centers the result on a specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/allowsmagnification)*