# OpenWindowAction

**Framework**: SwiftUI  
**Kind**: struct

An action that presents a window.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct OpenWindowAction
```

#### Overview

Use the [`openWindow`](environmentvalues/openwindow.md) environment value to get the instance of this structure for a given [`Environment`](environment.md). Then call the instance to open a window. You call the instance directly because it defines a [`callAsFunction(id:)`](openwindowaction/callasfunction(id:).md) method that Swift calls when you call the instance.

For example, you can define a button that opens a new mail viewer window:

```swift
@main
struct Mail: App {
    var body: some Scene {
        WindowGroup(id: "mail-viewer") {
            MailViewer()
        }
    }
}

struct NewViewerButton: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open new mail viewer") {
            openWindow(id: "mail-viewer")
        }
    }
}
```

You indicate which scene to open by providing one of the following:

- A string identifier that you pass through the `id` parameter, as in the above example.
- A `value` parameter that has a type that matches the type that you specify in the scene’s initializer.
- Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type, like a [`UUID`](https://developer.apple.com/documentation/Foundation/UUID).

Use the first option to target either a [`WindowGroup`](windowgroup.md) or a [`Window`](window.md) scene in your app that has a matching identifier. For a `WindowGroup`, the system creates a new window for the group. If the window group presents data, the system provides the default value or `nil` to the window’s root view. If the targeted scene is a `Window`, the system orders it to the front.

Use the other two options to target a `WindowGroup` and provide a value to present. If the interface already has a window from the group that’s presenting the specified value, the system brings the window to the front. Otherwise, the system creates a new window and passes a binding to the specified value.

## Topics

### Calling the action
- [func callAsFunction(id: String)](openwindowaction/callasfunction(id:).md)
  Opens a window that’s associated with the specified identifier.
- [func callAsFunction<D>(id: String, value: D)](openwindowaction/callasfunction(id:value:).md)
  Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier.
- [func callAsFunction<D>(value: D)](openwindowaction/callasfunction(value:).md)
  Opens a window defined by a window group that presents the type of the specified value.
### Structures
- [OpenWindowAction.SharingBehavior](openwindowaction/sharingbehavior.md)
### Instance Methods
- [func callAsFunction(id: String, sharingBehavior: OpenWindowAction.SharingBehavior) async throws](openwindowaction/callasfunction(id:sharingbehavior:).md)
  Opens a window that’s associated with the specified identifier, using the specified sharing sharingBehavior..
- [func callAsFunction<D>(id: String, value: D, sharingBehavior: OpenWindowAction.SharingBehavior) async throws](openwindowaction/callasfunction(id:value:sharingbehavior:).md)
  Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier, using the specified sharingBehavior.
- [func callAsFunction<D>(value: D, sharingBehavior: OpenWindowAction.SharingBehavior) async throws](openwindowaction/callasfunction(value:sharingbehavior:).md)
  Opens a window defined by a window group that presents the type of the specified value, using the specified sharingBehavior.

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
- [struct PushWindowAction](pushwindowaction.md)
  An action that opens the requested window in place of the window the action is called from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openwindowaction)*