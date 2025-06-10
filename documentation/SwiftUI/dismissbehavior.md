# DismissBehavior

**Framework**: SwiftUI  
**Kind**: struct

Programmatic window dismissal behaviors.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct DismissBehavior
```

#### Overview

Use values of this type to control window dismissal during the current transaction.

For example, to dismiss windows showing a modal presentation that would otherwise prohibit dismissal, use the [`destructive`](dismissbehavior/destructive.md) behavior:

```swift
struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            withTransaction(\.dismissBehavior, .destructive) {
                dismissWindow(id: "auxiliary")
            }
        }
    }
}
```

## Topics

### Getting behaviors
- [static let destructive: DismissBehavior](dismissbehavior/destructive.md)
  The destructive dismiss behavior.
- [static let interactive: DismissBehavior](dismissbehavior/interactive.md)
  The interactive dismiss behavior.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dismissWindow: DismissWindowAction](environmentvalues/dismisswindow.md)
  A window dismissal action stored in a view’s environment.
- [struct DismissWindowAction](dismisswindowaction.md)
  An action that dismisses a window associated to a particular scene.
- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [struct DismissAction](dismissaction.md)
  An action that dismisses a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismissbehavior)*