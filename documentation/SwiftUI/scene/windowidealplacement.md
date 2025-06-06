# windowIdealPlacement(_:)

**Framework**: SwiftUI  
**Kind**: method

Provides a function which determines a placement to use when windows of a scene zoom.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowIdealPlacement(_ makePlacement: @escaping (WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene
```

#### Discussion

The default behavior will size the window to its maximum size, or the bounds of the display, whichever is smaller. By overriding this behavior, you can provide a size that is appropriate for the contents of your window.

For example, you can provide a placement with a height equal to the display bounds, and a width based on your content’s ideal width:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .windowIdealPlacement { content, context in
            let displayBounds = context.defaultDisplay.visibleRect
            let proposal = ProposedViewSize(
                width: nil, height: displayBounds.height)
            let contentSize = content.sizeThatFits(proposal)
            return .init(
                width: contentSize.width,
                height: contentSize.height)
        }
    }
}
```

## Parameters

- `makePlacement`: A closure which returns the ideal placement for a   window derived from this scene.

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
- [struct WindowPlacementContext](windowplacementcontext.md)
  A type which represents contextual information used for sizing and positioning windows.
- [struct WindowProxy](windowproxy.md)
  The proxy for an open window in the app.
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowidealplacement(_:))*