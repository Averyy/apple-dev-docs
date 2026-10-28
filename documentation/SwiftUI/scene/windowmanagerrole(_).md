# windowManagerRole(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func windowManagerRole(_ role: WindowManagerRole) -> some Scene
```

## Discussion

By default, the type of `Scene` and its placement within the app’s definition will determine the behavior of its windows within a window management context.

You can use this modifier to override the default behaivor.

For example, you can specify that a secondary `Window` scene should use the principal behavior for full screen and Stage Manager:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        Window("Organizer", id: "organizer") {
            OrganizerView()
        }
        .windowManagerRole(.principal)
    }
}
```

## See Also

### Managing window behavior
- [struct WindowManagerRole](../windowmanagerrole.md)
  Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [struct WindowInteractionBehavior](../windowinteractionbehavior.md)
  Options for enabling and disabling window interaction behaviors.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](../view/windowdismissbehavior%28_%29.md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](../view/windowfullscreenbehavior%28_%29.md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](../view/windowminimizebehavior%28_%29.md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](../view/windowresizebehavior%28_%29.md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](./windowbackgrounddragbehavior%28_%29.md)
  Configures the behavior of dragging a window by its background.
- [func allowsWindowActivationEvents() -> some View](../view/allowswindowactivationevents%28%29.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](../view/allowswindowactivationevents%28_%29.md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowmanagerrole(_:))*