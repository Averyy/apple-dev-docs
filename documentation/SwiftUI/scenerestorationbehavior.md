# SceneRestorationBehavior

**Framework**: SwiftUI  
**Kind**: struct

The restoration behavior for a scene.

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
struct SceneRestorationBehavior
```

#### Overview

Use the [`restorationBehavior(_:)`](scene/restorationbehavior(_:).md) scene modifier to apply a value of this type to a [`Scene`](scene.md) you define in your [`App`](app.md) declaration. The value you specify determines how the system will restore windows from a previous run of your application.

For example, you may have a scene that you do not wish to be restored on launch:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        Window(id: "network-test", "Network Connection Test") {
            NetworkTestView()
        }
        .restorationBehavior(.disabled)
    }
}
```

## Topics

### Type Properties
- [static let automatic: SceneRestorationBehavior](scenerestorationbehavior/automatic.md)
  The automatic behavior. The scene’s windows will be restored as defined by the underlying platform.
- [static let disabled: SceneRestorationBehavior](scenerestorationbehavior/disabled.md)
  The disabled behavior. The scene’s windows will not be restored.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WindowVisibilityToggle](windowvisibilitytoggle.md)
  A specialized button for toggling the visibility of a window.
- [func defaultLaunchBehavior(SceneLaunchBehavior) -> some Scene](scene/defaultlaunchbehavior(_:).md)
  Sets the default launch behavior for this scene.
- [func restorationBehavior(SceneRestorationBehavior) -> some Scene](scene/restorationbehavior(_:).md)
  Sets the restoration behavior for this scene.
- [struct SceneLaunchBehavior](scenelaunchbehavior.md)
  The launch behavior for a scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](view/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [struct WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md)
  The visibility of the window toolbar with respect to full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenerestorationbehavior)*