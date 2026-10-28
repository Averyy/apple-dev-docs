# convertFromBacking(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts a rectangle from its pixel-aligned backing store coordinate system to the window’s coordinate system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func convertFromBacking(_ rect: NSRect) -> NSRect
```

```objc
- (NSRect) convertRectFromBacking:(NSRect) rect;
```

## Return Value

A rectangle in the window’s coordinate system.

## Parameters

- `rect`: The rectangle aligned to the pixel backing store coordinate system.

## See Also

### Converting Coordinates
- [var backingScaleFactor: CGFloat](./backingscalefactor.md)
  The backing scale factor.
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](./backingalignedrect%28_,options%29.md)
  Returns a backing store pixel-aligned rectangle in window coordinates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/convertfrombacking(_:))*