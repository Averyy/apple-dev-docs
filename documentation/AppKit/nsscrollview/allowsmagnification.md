# allowsMagnification

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Allows the user to magnify the scroll view.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var allowsMagnification: Bool { get set }
```

```objc
@property BOOL allowsMagnification;
```

#### Discussion

This property does not prevent the developer from manually adjusting the magnification value. If magnification exceeds either the maximum or minimum limits for magnification, and [`allowsMagnification`](./allowsmagnification.md) is [`true`](../../Swift/true.md), the scroll view temporarily animates the content magnification just past those limits before returning to them. The default value is [`false`](../../Swift/false.md).

## See Also

### Zooming the Scroll View
- [var magnification: CGFloat](./magnification.md)
  The amount by which the content is currently scaled.
- [func magnify(toFit: NSRect)](./magnify%28tofit%29.md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var maxMagnification: CGFloat](./maxmagnification.md)
  The maximum value to which the content can be magnified.
- [var minMagnification: CGFloat](./minmagnification.md)
  The minimum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](./setmagnification%28_,centeredat%29.md)
  Magnify the content by the given amount and center the result on the given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/allowsmagnification)*