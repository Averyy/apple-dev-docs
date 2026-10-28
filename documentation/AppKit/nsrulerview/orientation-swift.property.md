# orientation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The orientation of the receiver to `orientation`.

**Availability**:
- macOS

## Declaration

```swift
var orientation: NSRulerView.Orientation { get set }
```

```objc
@property NSRulerOrientation orientation;
```

## Discussion

Possible values for `orientation` are described in `Constants`.

## See Also

### Ruler layout
- [var scrollView: NSScrollView?](./scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
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
- [var baselineLocation: CGFloat](./baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/orientation-swift.property)*