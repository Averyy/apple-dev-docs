# backingAlignedRect(_:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a backing store pixel-aligned rectangle in window coordinates.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func backingAlignedRect(_ rect: NSRect, options: AlignmentOptions = []) -> NSRect
```

```objc
- (NSRect) backingAlignedRect:(NSRect) rect options:(NSAlignmentOptions) options;
```

#### Return Value

A rectangle, in window coordinates, aligned to the backing store pixels according to the specified options.

#### Discussion

This method uses [`NSIntegralRectWithOptions(_:_:)`](../../Foundation/nsintegralrectwithoptions%28_,_%29.md) to align the input rectangle, and produces a backing store pixel-aligned rectangle.

## Parameters

- `rect`: The rectangle in view coordinates.
- `options`: The alignment options. [`AlignmentOptions`](../../Foundation/alignmentoptions.md) specifies the possible values.

## See Also

### Converting Coordinates
- [var backingScaleFactor: CGFloat](./backingscalefactor.md)
  The backing scale factor.
- [func convertFromBacking(NSRect) -> NSRect](./convertfrombacking%28_%29.md)
  Converts a rectangle from its pixel-aligned backing store coordinate system to the window’s coordinate system.
- [func convertFromScreen(NSRect) -> NSRect](./convertfromscreen%28_%29.md)
  Converts a rectangle from the screen coordinate system to the window’s coordinate system.
- [func convertPointFromBacking(NSPoint) -> NSPoint](./convertpointfrombacking%28_%29.md)
  Converts a point from its pixel-aligned backing store coordinate system to the window’s coordinate system.
- [func convertPoint(fromScreen: NSPoint) -> NSPoint](./convertpoint%28fromscreen%29.md)
  Converts a point from the screen coordinate system to the window’s coordinate system.
- [func convertToBacking(NSRect) -> NSRect](./converttobacking%28_%29.md)
  Converts a rectangle from the window’s coordinate system to its pixel-aligned backing store coordinate system.
- [func convertToScreen(NSRect) -> NSRect](./converttoscreen%28_%29.md)
  Converts a rectangle to the screen coordinate system from the window’s coordinate system.
- [func convertPointToBacking(NSPoint) -> NSPoint](./convertpointtobacking%28_%29.md)
  Converts a point from the window’s coordinate system to its pixel-aligned backing store coordinate system.
- [func convertPoint(toScreen: NSPoint) -> NSPoint](./convertpoint%28toscreen%29.md)
  Converts a point to the screen coordinate system from the window’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingalignedrect(_:options:))*