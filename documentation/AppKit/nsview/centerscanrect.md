# centerScanRect(_:)

**Framework**: AppKit  
**Kind**: method

Converts the corners of a specified rectangle to lie on the center of device pixels, which is useful in compensating for rendering overscanning when the coordinate system has been scaled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func centerScanRect(_ rect: NSRect) -> NSRect
```

#### Return Value

The adjusted rectangle.

#### Discussion

This method converts the given rectangle to device coordinates, adjusts the rectangle to lie in the center of the pixels, and converts the resulting rectangle back to the view’s coordinate system. Note that this method does not take into account any transformations performed using the [`NSAffineTransform`](https://developer.apple.com/documentation/Foundation/NSAffineTransform) class or Quartz 2D routines.

## Parameters

- `rect`: The rectangle whose corners are to be converted.

## See Also

- [var isRotatedOrScaledFromBase: Bool](nsview/isrotatedorscaledfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](nsview/backingalignedrect(_:options:).md)
  Returns a backing store pixel-aligned rectangle in local view coordinates.
- [func convertFromBacking(NSPoint) -> NSPoint](nsview/convertfrombacking(_:)-229ps.md)
  Converts a point from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSPoint) -> NSPoint](nsview/converttobacking(_:)-2xx45.md)
  Converts a point from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSPoint) -> NSPoint](nsview/convertfromlayer(_:)-3nsbu.md)
  Convert the point from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSPoint) -> NSPoint](nsview/converttolayer(_:)-44u7d.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convertFromBacking(NSRect) -> NSRect](nsview/convertfrombacking(_:)-2njpa.md)
  Converts a rectangle from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSRect) -> NSRect](nsview/converttobacking(_:)-3zors.md)
  Converts a rectangle from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSRect) -> NSRect](nsview/convertfromlayer(_:)-8s5bi.md)
  Convert the rectangle from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSRect) -> NSRect](nsview/converttolayer(_:)-160pw.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convertFromBacking(NSSize) -> NSSize](nsview/convertfrombacking(_:)-4agf9.md)
  Converts a size from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSSize) -> NSSize](nsview/converttobacking(_:)-4ra9y.md)
  Converts a size from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSSize) -> NSSize](nsview/convertfromlayer(_:)-3usqp.md)
  Convert the size from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSSize) -> NSSize](nsview/converttolayer(_:)-2vozx.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convert(NSPoint, from: NSView?) -> NSPoint](nsview/convert(_:from:)-1dq9l.md)
  Converts a point from the coordinate system of a given view to that of the view.
- [func convert(NSPoint, to: NSView?) -> NSPoint](nsview/convert(_:to:)-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/centerscanrect(_:))*