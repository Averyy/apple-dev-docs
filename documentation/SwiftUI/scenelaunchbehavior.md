# SceneLaunchBehavior

**Framework**: SwiftUI  
**Kind**: struct

The launch behavior for a scene.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct SceneLaunchBehavior
```

#### Overview

Use the [`defaultLaunchBehavior(_:)`](scene/defaultlaunchbehavior(_:).md) modifier to apply a value of this type to a [`Scene`](scene.md) you specify in your [`App`](app.md). The value you specify determines how the system will present the scene in the absense of any previously restored scenes on launch of your application.

For example, you may wish to present a welcome window on launch of your app when there are no previous document windows being restored:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { configuration in
            DocumentEditor(configuration.$document)
        }

        Window("Welcome to My App", id: "welcome") {
            WelcomeView()
        }
        .defaultLaunchBehavior(.presented)
    }
}
```

## Topics

### Type Properties
- [static let automatic: SceneLaunchBehavior](scenelaunchbehavior/automatic.md)
  The automatic behavior.
- [static let presented: SceneLaunchBehavior](scenelaunchbehavior/presented.md)
  The presented behavior. The scene will present itself in the absence of any previously restored scenes.
- [static let suppressed: SceneLaunchBehavior](scenelaunchbehavior/suppressed.md)
  The suppressed behavior. The scene will not present itself in the absence of any previously restored scenes.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct WindowVisibilityToggle](windowvisibilitytoggle.md)
  A specialized button for toggling the visibility of a window.
- [func defaultLaunchBehavior(SceneLaunchBehavior) -> some Scene](scene/defaultlaunchbehavior(_:).md)
  Sets the default launch behavior for this scene.
- [func restorationBehavior(SceneRestorationBehavior) -> some Scene](scene/restorationbehavior(_:).md)
  Sets the restoration behavior for this scene.
- [struct SceneRestorationBehavior](scenerestorationbehavior.md)
  The restoration behavior for a scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](view/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [struct WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md)
  The visibility of the window toolbar with respect to full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenelaunchbehavior)*