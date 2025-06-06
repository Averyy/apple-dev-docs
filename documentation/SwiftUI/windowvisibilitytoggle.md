# WindowVisibilityToggle

**Framework**: SwiftUI  
**Kind**: struct

A specialized button for toggling the visibility of a window.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct WindowVisibilityToggle<Label> where Label : View
```

#### Overview

This is most commonly used in the main menu, where it can toggle the visibility of `Window` and `UtilityWindow` windows. The default label uses the title of the window in the format of “Show ” and “Hide ” depending on the current visibility of the window.

A keyboard shortcut can be assigned to this button.

The below example demonstrates how a main menu can be constructed with visibility buttons, replacing the default commands added by `Window` and `Utility Window`:

```swift
 struct PhotoEditor: App {
     var body: some Scene {
         WindowGroup {
             PhotoEditor()
         }
         .commands {
            CommandGroup(before: .textFormatting) {
                Section {
                    WindowVisibilityToggle(windowID: "formatting")
                        .keyboardShortcut("t", modifiers: [.command, .shift])

                    // other custom/image formatting controls
                }
            }
            CommandGroup(before: .sidebar) {
                Section {
                    WindowVisibilityToggle(windowID: "photo-library")

                    // other controls for showing/hiding UI
                }
            }
         }

         UtilityWindow("Formatting Style", id: "formatting") {
             TextAndImageFormatForm()
         }
         .commandsRemoved()

         Window("Photo Library", id: "photo-library") {
             PhotoInfoViewer()
         }
         .commandsRemoved()
     }
 }
```

## Topics

### Creating a window visibility toggle
- [init(windowID: String)](windowvisibilitytoggle/init(windowid:).md)
  Create a window visibility toggle to alter the visibility of a specific window.
### Supporting types
- [struct DefaultWindowVisibilityToggleLabel](defaultwindowvisibilitytogglelabel.md)
  The default label of a window visibility toggle.

## Relationships

### Conforms To
- [View](view.md)

## See Also

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
- [struct WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md)
  The visibility of the window toolbar with respect to full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowvisibilitytoggle)*