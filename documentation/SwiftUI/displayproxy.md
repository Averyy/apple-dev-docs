# DisplayProxy

**Framework**: SwiftUI  
**Kind**: struct

A type which provides information about display hardware.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct DisplayProxy
```

#### Overview

You can use this type with your custom window layouts to size and position windows relative to a display’s bounds.

For example, your custom window layout can position a window 140 points from the bottom of the screen’s visible area:

```swift
Window("Status", id: "status") {
    StatusView()
}
.windowResizability(.contentSize)
.defaultWindowPlacement { content, context in
    let displayBounds = context.defaultDisplay.visibleRect
    let size = content.sizeThatFits(.unspecified)
    let position = CGPoint(
        x: displayBounds.midX - (size.width / 2),
        y: displayBounds.maxY - size.height - 140)
    return WindowPlacement(position: position, size: size)
}
```

## Topics

### Instance Properties
- [let bounds: CGRect](displayproxy/bounds.md)
  The full dimensions of the display, including any space occupied by system interface elements.
- [let safeAreaInsets: EdgeInsets](displayproxy/safeareainsets.md)
  The safe area inset of this display.
- [let visibleRect: CGRect](displayproxy/visiblerect.md)
  The portion of the display where it is safe to place windows.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func defaultPosition(UnitPoint) -> some Scene](scene/defaultposition(_:).md)
  Sets a default position for a window.
- [struct WindowLevel](windowlevel.md)
  The level of a window.
- [func windowLevel(WindowLevel) -> some Scene](scene/windowlevel(_:).md)
  Sets the window level of this scene.
- [struct WindowLayoutRoot](windowlayoutroot.md)
  A proxy which represents the root contents of a window.
- [struct WindowPlacement](windowplacement.md)
  A type which represents a preferred size and position for a window.
- [func defaultWindowPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/defaultwindowplacement(_:).md)
  Defines a function used for determining the default placement of windows.
- [func windowIdealPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/windowidealplacement(_:).md)
  Provides a function which determines a placement to use when windows of a scene zoom.
- [struct WindowPlacementContext](windowplacementcontext.md)
  A type which represents contextual information used for sizing and positioning windows.
- [struct WindowProxy](windowproxy.md)
  The proxy for an open window in the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/displayproxy)*