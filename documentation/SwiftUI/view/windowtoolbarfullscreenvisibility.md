# windowToolbarFullScreenVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the visibility of the window toolbar when the window enters full screen mode.

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
nonisolated
func windowToolbarFullScreenVisibility(_ visibility: WindowToolbarFullScreenVisibility) -> some View
```

#### Discussion

By default, the window toolbar will show at the top of the display, above the window’s contents.

You can use this modifier to override the default behavior.

For example, you can specify that the window toolbar should be hidden by default, and only show once the mouse moves into the area occupied by the menu bar:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ...
            }
            .windowToolbarFullScreenVisibility(.onHover)
    }
}
```

## Parameters

- `visibility`: The visibility to use for the window toolbar in   full screen mode.

## See Also

- [struct WindowVisibilityToggle](windowvisibilitytoggle.md)
  A specialized button for toggling the visibility of a window.
- [func defaultLaunchBehavior(SceneLaunchBehavior) -> some Scene](scene/defaultlaunchbehavior(_:).md)
  Sets the default launch behavior for this scene.
- [func restorationBehavior(SceneRestorationBehavior) -> some Scene](scene/restorationbehavior(_:).md)
  Sets the restoration behavior for this scene.
- [struct SceneLaunchBehavior](scenelaunchbehavior.md)
  The launch behavior for a scene.
- [struct SceneRestorationBehavior](scenerestorationbehavior.md)
  The restoration behavior for a scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [struct WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md)
  The visibility of the window toolbar with respect to full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/windowtoolbarfullscreenvisibility(_:))*