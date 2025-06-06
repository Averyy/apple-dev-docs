# WindowPlacementContext

**Framework**: SwiftUI  
**Kind**: struct

A type which represents contextual information used for sizing and positioning windows.

**Availability**:
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct WindowPlacementContext
```

#### Overview

The placement context provides information to be used when providing a new placement via the closure provided to the `defaultWindowPlacement(_:)` modifier.

## Topics

### Instance Properties
- [var defaultDisplay: DisplayProxy](windowplacementcontext/defaultdisplay.md)
  The display on which new windows will be presented by default.
- [var windows: [WindowProxy]](windowplacementcontext/windows.md)
  The list of current active scenes

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
- [struct WindowProxy](windowproxy.md)
  The proxy for an open window in the app.
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowplacementcontext)*