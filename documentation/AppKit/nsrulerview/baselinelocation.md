# baselineLocation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The location of the receiver’s baseline, in its own coordinate system.

**Availability**:
- macOS

## Declaration

```swift
var baselineLocation: CGFloat { get }
```

```objc
@property (readonly) CGFloat baselineLocation;
```

#### Discussion

This is a y position for horizontal rulers and an x position for vertical ones.

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
- [var ruleThickness: CGFloat](./rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](./requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/baselinelocation)*