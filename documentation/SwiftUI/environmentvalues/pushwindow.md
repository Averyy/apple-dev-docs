# pushWindow

**Framework**: SwiftUI  
**Kind**: property

A window presentation action stored in a view’s environment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var pushWindow: PushWindowAction { get }
```

#### Discussion

This action opens the requested window in place of the window the action is called from. The scene this action is called from will be backgrounded. The requested scene will be center-aligned with the backgrounded scene. The requested scene will have a default size that matches the size of the backgrounded scene. Closing the requested window will result in the backgrounded scene reappearing.

Call [`dismissWindow`](environmentvalues/dismisswindow.md) from the pushed window to dismiss the pushed window and show the backgrounded window.

Calling this action from a pushed window is not allowed.

Alternatively, use [`openWindow`](environmentvalues/openwindow.md) to open a window separate from the window the action is called from.

Use the `pushWindow` environment value to get an [`PushWindowAction`](pushwindowaction.md) instance for a given [`Environment`](environment.md). Then call the instance to push a window. You call the instance directly because it defines a [`callAsFunction(id:)`](pushwindowaction/callasfunction(id:).md) method that Swift calls when you call the instance.

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
- Both an identifier and a value. This enables you to define multiple window groups that take input values of the same type like a [`UUID`](https://developer.apple.com/documentation/Foundation/UUID).

Use the first option to target either a [`WindowGroup`](windowgroup.md) or a [`Window`](window.md) scene in your app that has a matching identifier. For a [`WindowGroup`](windowgroup.md), the system creates a new window for the group. If the window group presents data, the system provides the default value or `nil` to the window’s root view. If the targeted scene is a `Window`, the system orders it to the front.

Use the other two options to target a [`WindowGroup`](windowgroup.md) and provide a value to present. If the interface already has a window from the group that is presenting the specified value, the system brings the window to the front. Otherwise, the system creates a new window and passes a binding to the specified value.

## See Also

- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [var dismissSearch: DismissSearchAction](environmentvalues/dismisssearch.md)
  An action that ends the current search interaction.
- [var dismissWindow: DismissWindowAction](environmentvalues/dismisswindow.md)
  A window dismissal action stored in a view’s environment.
- [var openImmersiveSpace: OpenImmersiveSpaceAction](environmentvalues/openimmersivespace.md)
  An action that presents an immersive space.
- [var dismissImmersiveSpace: DismissImmersiveSpaceAction](environmentvalues/dismissimmersivespace.md)
  An immersive space dismissal action stored in a view’s environment.
- [var newDocument: NewDocumentAction](environmentvalues/newdocument.md)
  An action in the environment that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [var openURL: OpenURLAction](environmentvalues/openurl.md)
  An action that opens a URL.
- [var openWindow: OpenWindowAction](environmentvalues/openwindow.md)
  A window presentation action stored in a view’s environment.
- [var purchase: PurchaseAction](environmentvalues/purchase.md)
  An action that starts an in-app purchase.
- [var refresh: RefreshAction?](environmentvalues/refresh.md)
  A refresh action stored in a view’s environment.
- [var rename: RenameAction?](environmentvalues/rename.md)
  An action that activates the standard rename interaction.
- [var resetFocus: ResetFocusAction](environmentvalues/resetfocus.md)
  An action that requests the focus system to reevaluate default focus.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/pushwindow)*