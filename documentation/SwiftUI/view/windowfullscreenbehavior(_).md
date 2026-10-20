# windowFullScreenBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the full screen functionality for the window enclosing `self`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowFullScreenBehavior(_ behavior: WindowInteractionBehavior) -> some View
```

#### Discussion

By default, the window full screen functionality is determined by the scene, as well as any modifiers applied to it. Additionally, when using the [`windowResizability(_:)`](../scene/windowresizability%28_%29.md) modifier, the maximum size of the window’s contents will also determine whether a window can be made full screen.

You can use this modifier to override the default behavior.

For example, you can specify that a window cannot enter full screen mode:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .windowFullScreenBehavior(.disabled)
        }
    }
}
```

## Parameters

- `behavior`: The full screen behavior.

## See Also

### Managing window behavior
- [struct WindowManagerRole](../windowmanagerrole.md)
  Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [func windowManagerRole(WindowManagerRole) -> some Scene](../scene/windowmanagerrole%28_%29.md)
  Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [struct WindowInteractionBehavior](../windowinteractionbehavior.md)
  Options for enabling and disabling window interaction behaviors.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](./windowdismissbehavior%28_%29.md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](./windowminimizebehavior%28_%29.md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](./windowresizebehavior%28_%29.md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](../scene/windowbackgrounddragbehavior%28_%29.md)
  Configures the behavior of dragging a window by its background.
- [func allowsWindowActivationEvents() -> some View](./allowswindowactivationevents%28%29.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](./allowswindowactivationevents%28_%29.md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/windowfullscreenbehavior(_:))*