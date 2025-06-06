# DismissWindowAction

**Framework**: SwiftUI  
**Kind**: struct

An action that dismisses a window associated to a particular scene.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DismissWindowAction
```

#### Overview

Use the [`dismissWindow`](environmentvalues/dismisswindow.md) environment value to get the instance of this structure for a given [`Environment`](environment.md). Then call the instance to dismiss a window. You call the instance directly because it defines a [`callAsFunction(id:)`](dismisswindowaction/callasfunction(id:).md) method that Swift calls when you call the instance.

For example, you can define a button that closes an auxiliary window:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Window("Auxiliary", id: "auxiliary") {
            AuxiliaryContentView()
        }
        #endif
    }
}

struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            dismissWindow(id: "auxiliary")
        }
    }
}
```

If the window was opened with [`pushWindow`](environmentvalues/pushwindow.md), the original presenting will reappear when this action is performed.

## Topics

### Calling the action
- [func callAsFunction()](dismisswindowaction/callasfunction.md)
  Dismisses the current window.
- [func callAsFunction(id: String)](dismisswindowaction/callasfunction(id:).md)
  Dismisses the window that’s associated with the specified identifier.
- [func callAsFunction<D>(id: String, value: D)](dismisswindowaction/callasfunction(id:value:).md)
  Dismisses the window defined by the window group that is presenting the specified value type and that’s associated with the specified identifier.
- [func callAsFunction<D>(value: D)](dismisswindowaction/callasfunction(value:).md)
  Dismisses the window defined by the window group that is presenting the specified value type.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var dismissWindow: DismissWindowAction](environmentvalues/dismisswindow.md)
  A window dismissal action stored in a view’s environment.
- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [struct DismissAction](dismissaction.md)
  An action that dismisses a presentation.
- [struct DismissBehavior](dismissbehavior.md)
  Programmatic window dismissal behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismisswindowaction)*