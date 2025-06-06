# WindowLayoutRoot

**Framework**: SwiftUI  
**Kind**: struct

A proxy which represents the root contents of a window.

**Availability**:
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct WindowLayoutRoot
```

#### Overview

This type acts like a proxy for the contents of the window defined by a SwiftUI [`Scene`](scene.md). The `Scene.defaultWindowPlacement(_:)` modifier receives an instance of this type, representing the contents of the window being created.

Use this proxy to get information about the window’s contents, like it’s size.

## Topics

### Instance Methods
- [func sizeThatFits(ProposedViewSize) -> CGSize](windowlayoutroot/sizethatfits(_:).md)
  Asks the window’s content for its size.

## See Also

- [func defaultPosition(UnitPoint) -> some Scene](scene/defaultposition(_:).md)
  Sets a default position for a window.
- [struct WindowLevel](windowlevel.md)
  The level of a window.
- [func windowLevel(WindowLevel) -> some Scene](scene/windowlevel(_:).md)
  Sets the window level of this scene.
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
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowlayoutroot)*