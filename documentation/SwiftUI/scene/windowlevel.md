# windowLevel(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the window level of this scene.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowLevel(_ level: WindowLevel) -> some Scene
```

#### Discussion

```swift
Window("Utility Window", id: "...") {
    UtilityContent()
}
.windowLevel(.floating)
```

## Parameters

- `level`: The desired window level

## See Also

- [func defaultPosition(UnitPoint) -> some Scene](scene/defaultposition(_:).md)
  Sets a default position for a window.
- [struct WindowLevel](windowlevel.md)
  The level of a window.
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
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowlevel(_:))*