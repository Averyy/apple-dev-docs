# reservedThicknessForMarkers

**Framework**: AppKit  
**Kind**: property

The room available for ruler markers to `thickness`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var reservedThicknessForMarkers: CGFloat { get set }
```

#### Discussion

The default thickness reserved for markers is 15.0 PostScript units for a horizontal ruler and 0.0 PostScript units for a vertical ruler (under the assumption that vertical rulers rarely contain markers). If you don’t expect to have any markers on the ruler, you can set the reserved thickness to 0.0.

An NSRulerView automatically increases the reserved thickness as necessary to that of its thickest marker. If you plan to use markers of varying sizes, you should set the reserved thickness beforehand to that of the thickest one in order to avoid retiling of the NSScrollView.

## See Also

- [var thicknessRequiredInRuler: CGFloat](nsrulermarker/thicknessrequiredinruler.md)
  The amount of the receiver’s image that’s displayed above or to the left of the ruler view’s baseline.
- [var markers: [NSRulerMarker]?](nsrulerview/markers.md)
  The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.
- [var scrollView: NSScrollView?](nsrulerview/scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](nsrulerview/orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [NSRulerView.Orientation](nsrulerview/orientation-swift.enum.md)
  These constants are defined to specify a ruler’s orientation and are used by [`orientation`](nsrulerview/orientation-swift.property.md).
- [var reservedThicknessForAccessoryView: CGFloat](nsrulerview/reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var ruleThickness: CGFloat](nsrulerview/rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](nsrulerview/requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](nsrulerview/baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](nsrulerview/isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/reservedthicknessformarkers)*