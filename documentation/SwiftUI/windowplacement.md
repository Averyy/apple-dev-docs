# WindowPlacement

**Framework**: SwiftUI  
**Kind**: struct

A type which represents a preferred size and position for a window.

**Availability**:
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct WindowPlacement
```

#### Overview

When using the `Scene.defaultWindowPlacement(_:)` modifier, you return an instance of a `WindowPlacement` in the closure you provide.

When constructing a window placement, many initial parameters are optional. Any value not specified will fall back to the scene’s default behavior and configuration for sizing and positioning it’s windows.

For example, you can use this to position a window 140 points from the bottom of the visible area of the screen:

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

### Structures
- [WindowPlacement.Position](windowplacement/position.md)
  A semantic or positional value for the location of a window.
### Initializers
- [init(WindowPlacement.Position?)](windowplacement/init(_:).md)
  Creates a new window placement with an optional position.
- [init(WindowPlacement.Position?, size3D: Size3D?)](windowplacement/init(_:size3d:).md)
  Creates a new window placement with an optional position and 3D size. Depth is ignored on scenes that don’t support it.
- [init(_:size:)](windowplacement/init(_:size:).md)
  Creates a new window placement with an absolute position and optional size.
- [init(UnitPoint, width: CGFloat?, height: CGFloat?)](windowplacement/init(_:width:height:).md)
  Creates a new window placement with a display-relative position, with an optional width and height.
- [init(WindowPlacement.Position?, width: CGFloat?, height: CGFloat?, depth: CGFloat?)](windowplacement/init(_:width:height:depth:).md)
  Creates a new window placement with an optional position and 3D size. Depth is ignored on scenes or platforms that don’t support it.
- [init(x: CGFloat?, y: CGFloat?, width: CGFloat?, height: CGFloat?)](windowplacement/init(x:y:width:height:).md)
  Creates a new window placement with an optional position and size.

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
- [func defaultWindowPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/defaultwindowplacement(_:).md)
  Defines a function used for determining the default placement of windows.
- [func windowIdealPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/windowidealplacement(_:).md)
  Provides a function which determines a placement to use when windows of a scene zoom.
- [struct WindowPlacementContext](windowplacementcontext.md)
  A type which represents contextual information used for sizing and positioning windows.
- [struct WindowProxy](windowproxy.md)
  The proxy for an open window in the app.
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowplacement)*