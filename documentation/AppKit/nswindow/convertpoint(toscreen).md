# convertPoint(toScreen:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts a point to the screen coordinate system from the window’s coordinate system.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func convertPoint(toScreen point: NSPoint) -> NSPoint
```

```objc
- (NSPoint) convertPointToScreen:(NSPoint) point;
```

#### Return Value

A point in the screen’s coordinate system.

## Parameters

- `point`: A point in the window’s coordinate system.

## See Also

### Converting Coordinates
- [var backingScaleFactor: CGFloat](./backingscalefactor.md)
  The backing scale factor.
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](./backingalignedrect%28_,options%29.md)
  Returns a backing store pixel-aligned rectangle in window coordinates.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/convertpoint(toscreen:))*