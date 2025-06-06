# convert(_:from:)

**Framework**: AppKit  
**Kind**: method

Converts a point from the coordinate system of a given view to that of the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func convert(_ point: NSPoint, from view: NSView?) -> NSPoint
```

#### Return Value

The point converted to the coordinate system of the view.

## Parameters

- `point`: A point specifying a location in the coordinate system of  .
- `view`: The view with   in its coordinate system. Both   and the view must belong to the same   object, and that window must not be  . If   is  , this method converts from window coordinates instead.

## See Also

- [var contentView: NSView?](nswindow/contentview.md)
  The window’s content view, the highest accessible view object in the window’s view hierarchy.
- [func ancestorShared(with: NSView) -> NSView?](nsview/ancestorshared(with:).md)
  Returns the closest ancestor shared by the view and another specified view.
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
- [func convert(NSPoint, to: NSView?) -> NSPoint](nsview/convert(_:to:)-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.
- [func convert(NSSize, from: NSView?) -> NSSize](nsview/convert(_:from:)-40x0w.md)
  Converts a size from another view’s coordinate system to that of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/convert(_:from:)-1dq9l)*