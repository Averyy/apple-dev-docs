# moveRulerline(fromLocation:toLocation:)

**Framework**: AppKit  
**Kind**: method

Draws temporary lines in the ruler area.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func moveRulerline(fromLocation oldLocation: CGFloat, toLocation newLocation: CGFloat)
```

#### Discussion

If `oldLoc` is 0 or greater, erases the ruler line at that location; if `newLoc` is 0 or greater, draws a new rulerline at that location. `oldLoc` and `newLoc` are expressed in the coordinate system of the NSRulerView, not the client or document view, and are x coordinates for horizontal rulers and y coordinates for vertical rulers. Use NSView’s `convert...` methods to convert coordinates from the client or document view’s coordinate system to that of the NSRulerView.

This method is useful for drawing highlight lines in the ruler to show the position or extent of an object while it’s being dragged in the client view. The sender is responsible for keeping track of the number and positions of temporary lines—the NSRulerView only does the drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/moverulerline(fromlocation:tolocation:))*