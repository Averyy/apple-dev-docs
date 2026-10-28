# minMagnification

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum value to which the content can be magnified.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var minMagnification: CGFloat { get set }
```

```objc
@property CGFloat minMagnification;
```

## Discussion

The default value is `0.25`.

## See Also

### Zooming the Scroll View
- [var allowsMagnification: Bool](./allowsmagnification.md)
  Allows the user to magnify the scroll view.
- [var magnification: CGFloat](./magnification.md)
  The amount by which the content is currently scaled.
- [func magnify(toFit: NSRect)](./magnify%28tofit%29.md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var maxMagnification: CGFloat](./maxmagnification.md)
  The maximum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](./setmagnification%28_,centeredat%29.md)
  Magnify the content by the given amount and center the result on the given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/minmagnification)*