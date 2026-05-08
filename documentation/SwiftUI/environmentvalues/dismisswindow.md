# dismissWindow

**Framework**: SwiftUI  
**Kind**: property

A window dismissal action stored in a view’s environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dismissWindow: DismissWindowAction { get }
```

#### Discussion

Use the `dismissWindow` environment value to get an [`DismissWindowAction`](dismisswindowaction.md) instance for a given [`Environment`](environment.md). Then call the instance to dismiss a window. You call the instance directly because it defines a [`callAsFunction(id:)`](dismisswindowaction/callasfunction(id:).md) method that Swift calls when you call the instance.

For example, you can define a button that dismisses an auxiliary window:

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

If the window was opened with [`pushWindow`](environmentvalues/pushwindow.md), the presenting window will reappear when this action is performed.

## See Also

- [struct DismissWindowAction](dismisswindowaction.md)
  An action that dismisses a window associated to a particular scene.
- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [struct DismissAction](dismissaction.md)
  An action that dismisses a presentation.
- [struct DismissBehavior](dismissbehavior.md)
  Programmatic window dismissal behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/dismisswindow)*