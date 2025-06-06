# focusedSceneObject(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func focusedSceneObject<T>(_ object: T) -> some View where T : ObservableObject
```

#### Return Value

A view that supplies an observable object while the scene is active.

#### Discussion

Use this method instead of [`focusedObject(_:)`](view/focusedobject(_:).md) for observable objects that must be visible regardless of where focus is located in the active scene. This is sometimes needed for things like main menu and discoverability HUD commands that observe and update data from the active scene but aren’t concerned with what the user is actually focused on. The scene’s root view can supply the scene’s state object:

```swift
struct RootView: View {
    @StateObject private var sceneData = SceneData()

    var body: some View {
        NavigationSplitView {
            ...
        }
        .focusedSceneObject(sceneData)
    }
}
```

Interested views can then use the [`FocusedObject`](focusedobject.md) property wrapper to observe and update the active scene’s state object. In this example, an app command updates the active scene’s data, and is enabled as long as any scene is active.

```swift
struct MessageCommands: Commands {
    @FocusedObject private var sceneData: SceneData?

    var body: some Commands {
        CommandGroup(after: .newItem) {
            Button("New Message") {
                sceneData?.addMessage()
            }
            .keyboardShortcut("n", modifiers: [.option, .command])
            .disabled(sceneData == nil)
        }
    }
}
```

## Parameters

- `object`: The observable object to associate with the scene.

## See Also

- [func focusedObject(_:)](view/focusedobject(_:).md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [struct FocusedObject](focusedobject.md)
  A property wrapper type for an observable object supplied by the focused view or one of its ancestors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusedsceneobject(_:))*