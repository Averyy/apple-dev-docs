# PushWindowAction

**Framework**: SwiftUI  
**Kind**: struct

An action that opens the requested window in place of the window the action is called from.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
struct PushWindowAction
```

#### Overview

The scene this action is called from will be backgrounded. The requested scene will be center-aligned with the backgrounded scene. The requested scene will have a default size that matches the size of the backgrounded scene. Closing the requested window will result in the backgrounded scene reappearing.

Call [`dismissWindow`](environmentvalues/dismisswindow.md) from the pushed window to dismiss the pushed window and show the backgrounded window.

Calling this action from a pushed window is not allowed.

Use the [`pushWindow`](environmentvalues/pushwindow.md) environment value to get the instance of this structure for a given [`Environment`](environment.md). Then call the instance to push a window. You call the instance directly because it defines a [`callAsFunction(id:)`](pushwindowaction/callasfunction(id:).md) method that Swift calls when you call the instance.

For example, you can define a button that pushes a video preview from an editor window:

```swift
@main
struct VideoEditor: App {
    var body: some Scene {
        WindowGroup(id: "editor") {
            EditorView()
        }

        WindowGroup(id: "viewer") {
            VideoView()
        }
    }
}

struct EditorView: View {
    @Environment(\.pushWindow) private var pushWindow

    var body: some View {
        Button("Play", systemImage: "play.fill") {
            pushWindow(id: "viewer")
        }
    }
}
```

You indicate which scene to push by providing one of the following:

- A string identifier that you pass through the `id` parameter, as in the above example.
- A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.
- Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type, like a [`UUID`](https://developer.apple.com/documentation/Foundation/UUID).

Use the first option to target either a [`WindowGroup`](windowgroup.md) or a [`Window`](window.md) scene in your app that has a matching identifier. For a [`WindowGroup`](windowgroup.md), the system creates a new window for the group. If the window group presents data, the system provides the default value or `nil` to the window’s root view. If the targeted scene is a [`Window`](window.md), the system orders it to the front.

Use the other two options to target a [`WindowGroup`](windowgroup.md) and provide a value to present. If the interface already has a window from the group that is presenting the specified value, the system brings the window to the front. Otherwise, the system creates a new window and passes a binding to the specified value.

## Topics

### Instance Methods
- [func callAsFunction(id: String)](pushwindowaction/callasfunction(id:).md)
  Pushes a window that is associated with the specified identifier.
- [func callAsFunction<D>(id: String, value: D)](pushwindowaction/callasfunction(id:value:).md)
  Pushes a window defined by the window group that presents the specified value type and that is associated with the specified identifier.
- [func callAsFunction<D>(value: D)](pushwindowaction/callasfunction(value:).md)
  Pushes a window defined by a window group that presents the type of the specified value.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Presenting windows and spaces](../visionOS/presenting-windows-and-spaces.md)
  Open and close the scenes that make up your app’s interface.
- [var supportsMultipleWindows: Bool](environmentvalues/supportsmultiplewindows.md)
  A Boolean value that indicates whether the current platform supports opening multiple windows.
- [var openWindow: OpenWindowAction](environmentvalues/openwindow.md)
  A window presentation action stored in a view’s environment.
- [struct OpenWindowAction](openwindowaction.md)
  An action that presents a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pushwindowaction)*