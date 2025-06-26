# defaultLaunchBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the default launch behavior for this scene.

**Availability**:
- macOS 15.0+
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func defaultLaunchBehavior(_ behavior: SceneLaunchBehavior) -> some Scene
```

#### Discussion

This behavior can be used to define if a scene is shown on application launch in the absence of any previously saved state.

On platforms that do not support multiple windows, this value is ignored.

On platforms other than macOS, there must be at least one scene that presents itself. If no scenes are defined to present, the first scene will be presented, regardless of the value provided to this modifier.

> **Note**: During app launch, on platforms other than macOS, the system will only consider scenes whose role matches the [`UIApplicationPreferredDefaultSceneSessionRole`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationPreferredDefaultSceneSessionRole) key in the application scene manifest of the `Info.plist` file. For instance, a volumetric window would need the `UIWindowSceneSessionRoleVolumetricApplication` role.

On macOS, this behavior will also be used to determine which scene is presented when clicking on the icon of a running application with no visible windows.

On visionOS, the system may background the last dismissed scene instead of closing it. Thus, the suppressed behavior additionally specifies that the scene should not be presented when tapping on the application icon with no visible windows.

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

The default value for all scenes if you do not apply this modifier is [`automatic`](scenelaunchbehavior/automatic.md). With that strategy, a scene will only present itself if it is the first scene defined by the app, and no other scenes have presented themselves.

## See Also

- [struct WindowVisibilityToggle](windowvisibilitytoggle.md)
  A specialized button for toggling the visibility of a window.
- [func restorationBehavior(SceneRestorationBehavior) -> some Scene](scene/restorationbehavior(_:).md)
  Sets the restoration behavior for this scene.
- [struct SceneLaunchBehavior](scenelaunchbehavior.md)
  The launch behavior for a scene.
- [struct SceneRestorationBehavior](scenerestorationbehavior.md)
  The restoration behavior for a scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](view/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [struct WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md)
  The visibility of the window toolbar with respect to full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/defaultlaunchbehavior(_:))*