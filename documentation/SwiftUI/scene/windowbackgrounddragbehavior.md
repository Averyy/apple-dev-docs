# windowBackgroundDragBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the behavior of dragging a window by its background.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowBackgroundDragBehavior(_ behavior: WindowInteractionBehavior) -> some Scene
```

#### Return Value

A scene configured with the specified behavior of dragging it by its background background.

#### Discussion

By default, or when you apply the [`automatic`](windowinteractionbehavior/automatic.md) behavior, the system will determine the best suitable behavior based on the configuration of the modified scene.

You can use this modifier to override the default behavior. For example, to always enable dragging a window by its background:

```swift
struct MyApp: App {
    var body: some Scene {
        Window("About MyApp", id: "about") {
            AboutView()
        }
        .windowBackgroundDragBehavior(.enabled)
    }
}
```

If you want to let your users drag your window by a specific view instead of (or in addition to) letting them drag it by its background, use [`WindowDragGesture`](windowdraggesture.md).

Applying the [`enabled`](windowinteractionbehavior/enabled.md) behavior is equivalent to adding a [`WindowDragGesture`](windowdraggesture.md) to the window’s background view.

## Parameters

- `behavior`: The behavior of dragging the modified window by its   background.

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
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](view/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowbackgrounddragbehavior(_:))*