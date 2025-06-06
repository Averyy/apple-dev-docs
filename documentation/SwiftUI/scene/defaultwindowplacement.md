# defaultWindowPlacement(_:)

**Framework**: SwiftUI  
**Kind**: method

Defines a function used for determining the default placement of windows.

**Availability**:
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func defaultWindowPlacement(_ makePlacement: @escaping (WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene
```

#### Discussion

Use this scene modifier to indicate a default initial size and position for a new window that the system creates from a [`Scene`](scene.md) declaration.

On macOS, you can use the screen’s bounds to place the window. For example, you can specify that the window is always placed 140 points from the bottom of the screen:

```swift
struct MyApp: App {
    var body: some Scene {
        ...

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
    }
}
```

On visionOS, the system always places the first window relative to where the person is looking. The system ignores calls to `defaultWindowPlacement(_:)`.

You can place any subsequent windows relative to existing ones by returning one of the methods defined by [`WindowPlacement.Position`](windowplacement/position.md) with the existing window. For example, you can align the new window with the trailing edge of the `Content` window:

```swift
struct MyApp: App {
    @Environment(\.openWindow) private var openWindow

    var body: some Scene {
        WindowGroup("Content", id: "content") {
            Button("Open status window") {
                openWindow(id: "status")
            }
        }

        WindowGroup("Status", id: "status") {
            StatusView()
        }
        .windowResizability(.contentSize)
        .defaultWindowPlacement { content, context in
            if let contentWindow = context.windows.first(
            where: { $0.id == "content" }) {
                WindowPlacement(.trailing(contentWindow))
            } else {
                WindowPlacement()
            }
        }
    }
}
```

The placement that your function returns acts as a default for when the window first appears. People can later resize and move the window using interface controls that the system provides. Also, during state restoration, the system restores the window to it’s most recent size and position, rather than the default placement.

For more information on configuring how scenes behave with state restoration, see `Scene.stateRestoration(_:)`.

## Parameters

- `makePlacement`: A closure to generate the default window placement.

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
- [func windowIdealPlacement((WindowLayoutRoot, WindowPlacementContext) -> WindowPlacement) -> some Scene](scene/windowidealplacement(_:).md)
  Provides a function which determines a placement to use when windows of a scene zoom.
- [struct WindowPlacementContext](windowplacementcontext.md)
  A type which represents contextual information used for sizing and positioning windows.
- [struct WindowProxy](windowproxy.md)
  The proxy for an open window in the app.
- [struct DisplayProxy](displayproxy.md)
  A type which provides information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/defaultwindowplacement(_:))*