# WindowInteractionBehavior

**Framework**: SwiftUI  
**Kind**: struct

Options for enabling and disabling window interaction behaviors.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct WindowInteractionBehavior
```

#### Overview

Use values of this type in conjunction with the following view and scene modifiers to adjust the supported functionality for the window:

- [`windowDismissBehavior(_:)`](view/windowdismissbehavior(_:).md)
- [`windowMinimizeBehavior(_:)`](view/windowminimizebehavior(_:).md)
- [`windowFullScreenBehavior(_:)`](view/windowfullscreenbehavior(_:).md)
- [`windowResizeBehavior(_:)`](view/windowresizebehavior(_:).md)
- [`windowBackgroundDragBehavior(_:)`](scene/windowbackgrounddragbehavior(_:).md)

For example, you can create a custom “About” window which only allows for dismissal:

```swift
struct MyApp: App {
    var body: some Scene {
        ...
        Window("About MyApp", id: "about") {
            AboutView()
                .windowMinimizeBehavior(.disabled)
                .windowResizeBehavior(.disabled)
        }
        .windowResizability(.contentSize)
    }
}
```

## Topics

### Type Properties
- [static let automatic: WindowInteractionBehavior](windowinteractionbehavior/automatic.md)
  The automatic behavior. The associated window behavior will be enabled or disabled depending on the configuration of the enclosing `Scene`.
- [static let disabled: WindowInteractionBehavior](windowinteractionbehavior/disabled.md)
  The disabled behavior. The associated window interaction behavior will be disabled.
- [static let enabled: WindowInteractionBehavior](windowinteractionbehavior/enabled.md)
  The enabled behavior. The associated window interaction behavior will be enabled.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct WindowManagerRole](windowmanagerrole.md)
  Options for defining how a scene’s windows behave when used within a managed window context, such as full screen mode and Stage Manager.
- [func windowManagerRole(WindowManagerRole) -> some Scene](scene/windowmanagerrole(_:).md)
  Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](view/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](view/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](view/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](view/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowBackgroundDragBehavior(WindowInteractionBehavior) -> some Scene](scene/windowbackgrounddragbehavior(_:).md)
  Configures the behavior of dragging a window by its background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowinteractionbehavior)*