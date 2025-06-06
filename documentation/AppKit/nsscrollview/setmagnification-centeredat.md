# setMagnification(_:centeredAt:)

**Framework**: AppKit  
**Kind**: method

Magnify the content by the given amount and center the result on the given point.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func setMagnification(_ magnification: CGFloat, centeredAt point: NSPoint)
```

#### Discussion

This method scales the content view such that the passed in point (in content view space) remains at the same screen location once the scaling is completed. The resulting magnification value is clipped to the [`minMagnification`](nsscrollview/minmagnification.md) and [`maxMagnification`](nsscrollview/maxmagnification.md) values. To animate the magnification, use the object’s animator.

## Parameters

- `magnification`: The amount by which to magnify the content.
- `point`: The point (in content view space) on which to center magnification.

## See Also

- [var allowsMagnification: Bool](nsscrollview/allowsmagnification.md)
  Allows the user to magnify the scroll view.
- [var magnification: CGFloat](nsscrollview/magnification.md)
  The amount by which the content is currently scaled.
- [func magnify(toFit: NSRect)](nsscrollview/magnify(tofit:).md)
  Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.
- [var maxMagnification: CGFloat](nsscrollview/maxmagnification.md)
  The maximum value to which the content can be magnified.
- [var minMagnification: CGFloat](nsscrollview/minmagnification.md)
  The minimum value to which the content can be magnified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/setmagnification(_:centeredat:))*