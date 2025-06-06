# focusedSceneObject(_:)

**Framework**: Assignables  
**Kind**: method

Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func focusedSceneObject<T>(_ object: T) -> some View where T : ObservableObject
```

#### Return Value

A view that supplies an observable object while the scene is active.

#### Discussion

Use this method instead of `View/focusedObject(_:)` for observable objects that must be visible regardless of where focus is located in the active scene. This is sometimes needed for things like main menu and discoverability HUD commands that observe and update data from the active scene but aren’t concerned with what the user is actually focused on. The scene’s root view can supply the scene’s state object:

```None
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

Interested views can then use the `FocusedObject` property wrapper to observe and update the active scene’s state object. In this example, an app command updates the active scene’s data, and is enabled as long as any scene is active.

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/focusedsceneobject(_:)-22cm2)*