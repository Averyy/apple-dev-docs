# ruleThickness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The thickness of the area where ruler hash marks and labels are drawn.

**Availability**:
- macOS

## Declaration

```swift
var ruleThickness: CGFloat { get set }
```

```objc
@property CGFloat ruleThickness;
```

#### Discussion

This value is the height of the ruler area for a horizontal ruler or the width of the ruler area for a vertical ruler. Rulers are by default 16.0 PostScript units thick. You should rarely need to change this layout attribute, but subclasses might do so to accommodate custom drawing.

## See Also

### Ruler layout
- [var scrollView: NSScrollView?](./scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](./orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [NSRulerView.Orientation](./orientation-swift.enum.md)
  These constants are defined to specify a ruler’s orientation and are used by [`orientation`](./orientation-swift.property.md).
- [var reservedThicknessForAccessoryView: CGFloat](./reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var reservedThicknessForMarkers: CGFloat](./reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var requiredThickness: CGFloat](./requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](./baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/rulethickness)*