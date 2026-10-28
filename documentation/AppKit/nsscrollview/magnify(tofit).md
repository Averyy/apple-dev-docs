# magnify(toFit:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Magnifies the content view proportionally such that the given rectangle fits centered in the scroll view.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func magnify(toFit rect: NSRect)
```

```objc
- (void) magnifyToFitRect:(NSRect) rect;
```

## Discussion

The resulting magnification value is clipped to the [`minMagnification`](./minmagnification.md) and [`maxMagnification`](./maxmagnification.md) values. To animate the magnification, use the object’s animator.

## Parameters

- `rect`: The rectangle (in content view space) to which the content view is magnified.

## See Also

### Zooming the Scroll View
- [var allowsMagnification: Bool](./allowsmagnification.md)
  Allows the user to magnify the scroll view.
- [var magnification: CGFloat](./magnification.md)
  The amount by which the content is currently scaled.
- [var maxMagnification: CGFloat](./maxmagnification.md)
  The maximum value to which the content can be magnified.
- [var minMagnification: CGFloat](./minmagnification.md)
  The minimum value to which the content can be magnified.
- [func setMagnification(CGFloat, centeredAt: NSPoint)](./setmagnification%28_,centeredat%29.md)
  Magnify the content by the given amount and center the result on the given point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/magnify(tofit:))*