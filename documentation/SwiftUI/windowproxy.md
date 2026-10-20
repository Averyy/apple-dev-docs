# WindowProxy

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The proxy for an open window in the app.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct WindowProxy
```

## Topics

### Instance Properties
- [var id: String?](./windowproxy/id.md)
  The ID for the window, if one was provided.
- [var phase: ScenePhase](./windowproxy/phase.md)
  The window’s current [`ScenePhase`](./scenephase.md).

## See Also

### Positioning a window
- [func defaultPosition(UnitPoint) -> some Scene](./scene/defaultposition%28_%29.md)
  Sets a default position for a window.
- [struct WindowLevel](./windowlevel.md)
  The level of a window.
- [func windowLevel(WindowLevel) -> some Scene](./scene/windowlevel%28_%29.md)
  Sets the window level of this scene.
- [struct WindowLayoutRoot](./windowlayoutroot.md)
  A proxy which represents the root contents of a window.
- [struct WindowPlacement](./windowplacement.md)
  A type which represents a preferred size and position for a window.
- [func defaultWindowPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](./scene/defaultwindowplacement%28_%29.md)
  Defines a function used for determining the default placement of windows.
- [func windowIdealPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](./scene/windowidealplacement%28_%29.md)
  Provides a function which determines a placement to use when windows of a scene zoom.
- [struct WindowPlacementContext](./windowplacementcontext.md)
  A type which represents contextual information used for sizing and positioning windows.
- [struct DisplayProxy](./displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowproxy)*