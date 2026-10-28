# convertToLayer(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Convert the size from the view’s interior coordinate system to the layer’s interior coordinate system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func convertToLayer(_ size: NSSize) -> NSSize
```

```objc
- (NSSize) convertSizeToLayer:(NSSize) size;
```

## Return Value

A size in the layer’s interior coordinate system.

## Discussion

The layer’s space is virtual, and doesn’t take into account the layer’s [`contentsScale`](../../QuartzCore/calayer/contentsscale.md) setting.

The returned `NSSize` values are always forced to have positive a width and height.

## Parameters

- `size`: A size in the view’s interior coordinate system.

## See Also

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
- [func convert(NSPoint, from: NSView?) -> NSPoint](./convert%28_,from%29-1dq9l.md)
  Converts a point from the coordinate system of a given view to that of the view.
- [func convert(NSPoint, to: NSView?) -> NSPoint](./convert%28_,to%29-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.
- [func convert(NSSize, from: NSView?) -> NSSize](./convert%28_,from%29-40x0w.md)
  Converts a size from another view’s coordinate system to that of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/converttolayer(_:)-2vozx)*