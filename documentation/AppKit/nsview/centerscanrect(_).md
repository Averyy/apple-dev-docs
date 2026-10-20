# centerScanRect(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts the corners of a specified rectangle to lie on the center of device pixels, which is useful in compensating for rendering overscanning when the coordinate system has been scaled.

**Availability**:
- macOS

## Declaration

```swift
func centerScanRect(_ rect: NSRect) -> NSRect
```

```objc
- (NSRect) centerScanRect:(NSRect) rect;
```

#### Return Value

The adjusted rectangle.

#### Discussion

This method converts the given rectangle to device coordinates, adjusts the rectangle to lie in the center of the pixels, and converts the resulting rectangle back to the view’s coordinate system. Note that this method does not take into account any transformations performed using the [`NSAffineTransform`](../../Foundation/nsaffinetransform.md) class or Quartz 2D routines.

## Parameters

- `rect`: The rectangle whose corners are to be converted.

## See Also

### Related Documentation
- [var isRotatedOrScaledFromBase: Bool](./isrotatedorscaledfrombase.md)
  A Boolean value indicating whether the view or any of its ancestors has ever had a rotation factor applied to its frame or bounds, or has been scaled from the window’s base coordinate system.
### Converting Coordinate Values
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](./backingalignedrect%28_,options%29.md)
  Returns a backing store pixel-aligned rectangle in local view coordinates.
- [func convertFromBacking(NSPoint) -> NSPoint](./convertfrombacking%28_%29-229ps.md)
  Converts a point from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSPoint) -> NSPoint](./converttobacking%28_%29-2xx45.md)
  Converts a point from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSPoint) -> NSPoint](./convertfromlayer%28_%29-3nsbu.md)
  Convert the point from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSPoint) -> NSPoint](./converttolayer%28_%29-44u7d.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convertFromBacking(NSRect) -> NSRect](./convertfrombacking%28_%29-2njpa.md)
  Converts a rectangle from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSRect) -> NSRect](./converttobacking%28_%29-3zors.md)
  Converts a rectangle from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSRect) -> NSRect](./convertfromlayer%28_%29-8s5bi.md)
  Convert the rectangle from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSRect) -> NSRect](./converttolayer%28_%29-160pw.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convertFromBacking(NSSize) -> NSSize](./convertfrombacking%28_%29-4agf9.md)
  Converts a size from its pixel aligned backing store coordinate system to the view’s interior coordinate system.
- [func convertToBacking(NSSize) -> NSSize](./converttobacking%28_%29-4ra9y.md)
  Converts a size from the view’s interior coordinate system to its pixel aligned backing store coordinate system.
- [func convertFromLayer(NSSize) -> NSSize](./convertfromlayer%28_%29-3usqp.md)
  Convert the size from the layer’s interior coordinate system to the view’s interior coordinate system.
- [func convertToLayer(NSSize) -> NSSize](./converttolayer%28_%29-2vozx.md)
  Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.
- [func convert(NSPoint, from: NSView?) -> NSPoint](./convert%28_,from%29-1dq9l.md)
  Converts a point from the coordinate system of a given view to that of the view.
- [func convert(NSPoint, to: NSView?) -> NSPoint](./convert%28_,to%29-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/centerscanrect(_:))*