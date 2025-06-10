# WindowToolbarFullScreenVisibility

**Framework**: SwiftUI  
**Kind**: struct

The visibility of the window toolbar with respect to full screen mode.

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
struct WindowToolbarFullScreenVisibility
```

#### Overview

Use values of this type in conjunction with the [`windowToolbarFullScreenVisibility(_:)`](view/windowtoolbarfullscreenvisibility(_:).md) modifier to configure how the window toolbar displays itself when the window enters full screen mode.

For example, you can specify that the window toolbar should be hidden by default, and only show when the mouse moves into the area occupied by the menu bar:

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

## Topics

### Type Properties
- [static let automatic: WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility/automatic.md)
  The window toolbar visibility will be defined by the system default behavior.
- [static let onHover: WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility/onhover.md)
  Hide the window toolbar in full screen mode by default. It will reveal itself when the mouse moves into the area occupied by the menu bar.
- [static let visible: WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility/visible.md)
  Prefer to show window toolbar when the window is in full screen mode.

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
- [struct SceneRestorationBehavior](scenerestorationbehavior.md)
  The restoration behavior for a scene.
- [func persistentSystemOverlays(Visibility) -> some Scene](scene/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](view/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowtoolbarfullscreenvisibility)*