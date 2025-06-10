# backingAlignedRect(_:options:)

**Framework**: AppKit  
**Kind**: method

Returns a backing store pixel-aligned rectangle in window coordinates.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func backingAlignedRect(_ rect: NSRect, options: AlignmentOptions = []) -> NSRect
```

#### Return Value

A rectangle, in window coordinates, aligned to the backing store pixels according to the specified options.

#### Discussion

This method uses [`NSIntegralRectWithOptions(_:_:)`](https://developer.apple.com/documentation/Foundation/NSIntegralRectWithOptions(_:_:)) to align the input rectangle, and produces a backing store pixel-aligned rectangle.

## Parameters

- `rect`: The rectangle in view coordinates.
- `options`: The alignment options.   specifies the possible values.

## See Also

- [var backingScaleFactor: CGFloat](nswindow/backingscalefactor.md)
  The backing scale factor.
- [func convertFromBacking(NSRect) -> NSRect](nswindow/convertfrombacking(_:).md)
  Converts a rectangle from its pixel-aligned backing store coordinate system to the window’s coordinate system.
- [func convertFromScreen(NSRect) -> NSRect](nswindow/convertfromscreen(_:).md)
  Converts a rectangle from the screen coordinate system to the window’s coordinate system.
- [func convertPointFromBacking(NSPoint) -> NSPoint](nswindow/convertpointfrombacking(_:).md)
  Converts a point from its pixel-aligned backing store coordinate system to the window’s coordinate system.
- [func convertPoint(fromScreen: NSPoint) -> NSPoint](nswindow/convertpoint(fromscreen:).md)
  Converts a point from the screen coordinate system to the window’s coordinate system.
- [func convertToBacking(NSRect) -> NSRect](nswindow/converttobacking(_:).md)
  Converts a rectangle from the window’s coordinate system to its pixel-aligned backing store coordinate system.
- [func convertToScreen(NSRect) -> NSRect](nswindow/converttoscreen(_:).md)
  Converts a rectangle to the screen coordinate system from the window’s coordinate system.
- [func convertPointToBacking(NSPoint) -> NSPoint](nswindow/convertpointtobacking(_:).md)
  Converts a point from the window’s coordinate system to its pixel-aligned backing store coordinate system.
- [func convertPoint(toScreen: NSPoint) -> NSPoint](nswindow/convertpoint(toscreen:).md)
  Converts a point to the screen coordinate system from the window’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingalignedrect(_:options:))*