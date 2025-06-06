# magnification

**Framework**: AppKit  
**Kind**: property

The amount by which the content is currently scaled.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var magnification: CGFloat { get set }
```

#### Discussion

To animate the magnification, use the object’s animator. The default value is `1.0`.

## See Also

- [var allowsMagnification: Bool](nsscrollview/allowsmagnification.md)
  Allows the user to magnify the scroll view.
- [func magnify(toFit: NSRect)](nsscrollview/magnify(tofit:).md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var maxMagnification: CGFloat](nsscrollview/maxmagnification.md)
  The maximum value to which the content can be magnified.
- [var minMagnification: CGFloat](nsscrollview/minmagnification.md)
  The minimum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](nsscrollview/setmagnification(_:centeredat:).md)
  Magnify the content by the given amount and center the result on the given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/magnification)*