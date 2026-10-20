# WindowManagerRole

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.

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
struct WindowManagerRole
```

#### Overview

Use values of this type in conjunction with the [`windowManagerRole(_:)`](./scene/windowmanagerrole%28_%29.md) modifier to override the default system behavior.

For example, you can specify that a secondary `Window` scene should use the principal role for full screen and Stage Manager:

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

## Topics

### Type Properties
- [static let associated: WindowManagerRole](./windowmanagerrole/associated.md)
  The associated role. Windows derived from this scene can be shown alongside windows with a `.principal` role in either full screen or Stage Manager, but do not participate in those modes on their own.
- [static let automatic: WindowManagerRole](./windowmanagerrole/automatic.md)
  The automatic role. The type and configuration of the scene will be used to determine how its windows behave in full screen and Stage Manager.
- [static let principal: WindowManagerRole](./windowmanagerrole/principal.md)
  The principal role. Windows derived from this scene will show in full screen, if enabled, or in Stage Manager.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing window behavior
- [func windowManagerRole(WindowManagerRole) -> some Scene](./scene/windowmanagerrole%28_%29.md)
  Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [struct WindowInteractionBehavior](./windowinteractionbehavior.md)
  Options for enabling and disabling window interaction behaviors.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](./view/windowdismissbehavior%28_%29.md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](./view/windowfullscreenbehavior%28_%29.md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](./view/windowminimizebehavior%28_%29.md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](./view/windowresizebehavior%28_%29.md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](./scene/windowbackgrounddragbehavior%28_%29.md)
  Configures the behavior of dragging a window by its background.
- [func allowsWindowActivationEvents() -> some View](./view/allowswindowactivationevents%28%29.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](./view/allowswindowactivationevents%28_%29.md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowmanagerrole)*