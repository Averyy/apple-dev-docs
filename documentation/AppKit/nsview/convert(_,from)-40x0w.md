# convert(_:from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts a size from another view’s coordinate system to that of the view.

**Availability**:
- macOS

## Declaration

```swift
func convert(_ size: NSSize, from view: NSView?) -> NSSize
```

```objc
- (NSSize) convertSize:(NSSize) size fromView:(NSView *) view;
```

## Return Value

The converted size, as an [`NSSize`](../../Foundation/nssize.md) structure.

## Discussion

The returned `NSSize` values are always forced to have positive a width and height.

You can also use this method to get a view’s current magnification or zoom level, if it’s been changed from the default scale. Specifically, if you convert a known size from the window’s base coordinate space to that of `view`, the result is the current zoom level.

## Parameters

- `size`: The size (width and height) in view’s coordinate system.
- `view`: The view with `size` in its coordinate system. Both `view` and the view must belong to the same [`NSWindow`](../nswindow.md) object, and that window must not be `nil`. If `view` is `nil`, this method converts from window coordinates instead.

## See Also

### Related Documentation
- [var contentView: NSView?](../nswindow/contentview.md)
  The window’s content view, the highest accessible view object in the window’s view hierarchy.
- [func ancestorShared(with: NSView) -> NSView?](./ancestorshared%28with%29.md)
  Returns the closest ancestor shared by the view and another specified view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/convert(_:from:)-40x0w)*