# maxMagnification

**Framework**: AppKit  
**Kind**: property

The maximum value to which the content can be magnified.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var maxMagnification: CGFloat { get set }
```

#### Discussion

This value must be greater than or equal to the minimum magnification. The default value is `4.0`.

## See Also

- [var allowsMagnification: Bool](nsscrollview/allowsmagnification.md)
  Allows the user to magnify the scroll view.
- [var magnification: CGFloat](nsscrollview/magnification.md)
  The amount by which the content is currently scaled.
- [func magnify(toFit: NSRect)](nsscrollview/magnify(tofit:).md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var minMagnification: CGFloat](nsscrollview/minmagnification.md)
  The minimum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](nsscrollview/setmagnification(_:centeredat:).md)
  Magnify the content by the given amount and center the result on the given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/maxmagnification)*