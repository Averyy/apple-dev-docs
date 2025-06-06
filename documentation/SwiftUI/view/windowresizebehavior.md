# windowResizeBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the resize functionality for the window enclosing `self`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowResizeBehavior(_ behavior: WindowInteractionBehavior) -> some View
```

#### Discussion

By default, the window resizability functionality is determined by the scene, as well as any modifiers applied to it. Additionally, when using the [`windowResizability(_:)`](scene/windowresizability(_:).md) modifier, the minimum and maximum size of the window’s contents will also determine the resizability behavior.

You can use this modifier to override the default behavior.

For example, you can create a custom “About” window which only allows for dismissal:

```swift
struct MyApp: App {
    var body: some Scene {
        ...
        Window("About MyApp", id: "about") {
            AboutView()
                .windowResizeBehavior(.disabled)
                .windowMinimizeBehavior(.disabled)
        }
        .windowResizability(.contentSize)
    }
}
```

## Parameters

- `behavior`: The resize behavior.

## See Also

- [struct WindowManagerRole](windowmanagerrole.md)
  Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [func windowManagerRole(WindowManagerRole) -> some Scene](scene/windowmanagerrole(_:).md)
  Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [struct WindowInteractionBehavior](windowinteractionbehavior.md)
  Options for enabling and disabling window interaction behaviors.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](view/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](view/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](view/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](scene/windowbackgrounddragbehavior(_:).md)
  Configures the behavior of dragging a window by its background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/windowresizebehavior(_:))*