# convertPointToBacking(_:)

**Framework**: AppKit  
**Kind**: method

Converts a point from the window’s coordinate system to its pixel-aligned backing store coordinate system.

**Availability**:
- macOS 10.14+

## Declaration

```swift
@MainActor
func convertPointToBacking(_ point: NSPoint) -> NSPoint
```

#### Return Value

A point in its pixel-aligned backing store coordinate system.

## Parameters

- `point`: A point in the window’s coordinate system.

## See Also

- [var backingScaleFactor: CGFloat](nswindow/backingscalefactor.md)
  The backing scale factor.
- [func backingAlignedRect(NSRect, options: AlignmentOptions) -> NSRect](nswindow/backingalignedrect(_:options:).md)
  Returns a backing store pixel-aligned rectangle in window coordinates.
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
- [func convertPoint(toScreen: NSPoint) -> NSPoint](nswindow/convertpoint(toscreen:).md)
  Converts a point to the screen coordinate system from the window’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/convertpointtobacking(_:))*