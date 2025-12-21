# allowsMagnification

**Framework**: AppKit  
**Kind**: property

Allows the user to magnify the scroll view.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var allowsMagnification: Bool { get set }
```

#### Discussion

This property does not prevent the developer from manually adjusting the magnification value. If magnification exceeds either the maximum or minimum limits for magnification, and [`allowsMagnification`](nsscrollview/allowsmagnification.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the scroll view temporarily animates the content magnification just past those limits before returning to them. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var magnification: CGFloat](nsscrollview/magnification.md)
  The amount by which the content is currently scaled.
- [func magnify(toFit: NSRect)](nsscrollview/magnify(tofit:).md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var maxMagnification: CGFloat](nsscrollview/maxmagnification.md)
  The maximum value to which the content can be magnified.
- [var minMagnification: CGFloat](nsscrollview/minmagnification.md)
  The minimum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](nsscrollview/setmagnification(_:centeredat:).md)
  Magnify the content by the given amount and center the result on the given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/allowsmagnification)*