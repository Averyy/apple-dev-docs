# WindowLevel

**Framework**: SwiftUI  
**Kind**: struct

The level of a window.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct WindowLevel
```

#### Overview

Use this in conjunction with the `.windowLevel(_:)` modifier to control window levels.

## Topics

### Type Properties
- [static var automatic: WindowLevel](windowlevel/automatic.md)
  Automatic window level.
- [static var desktop: WindowLevel](windowlevel/desktop.md)
  Desktop window level.
- [static var floating: WindowLevel](windowlevel/floating.md)
  Floating window level.
- [static var normal: WindowLevel](windowlevel/normal.md)
  Normal window level.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func defaultPosition(UnitPoint) -> some Scene](scene/defaultposition(_:).md)
  Sets a default position for a window.
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
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowlevel)*