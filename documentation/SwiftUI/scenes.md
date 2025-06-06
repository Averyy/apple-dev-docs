# Scenes

**Framework**: SwiftUI

Declare the user interface groupings that make up the parts of your app.

#### Overview

A scene represents a part of your app’s user interface that has a life cycle that the system manages. An [`App`](app.md) instance presents the scenes it contains, while each [`Scene`](scene.md) acts as the root element of a [`View`](view.md) hierarchy.

![None](https://docs-assets.developer.apple.com/published/0ae322d333458f9341bc3aa57f4e8250/scenes-hero%402x.png)

The system presents scenes in different ways depending on the type of scene, the platform, and the context. A scene might fill the entire display, part of the display, a window, a tab in a window, or something else. In some cases, your app might also be able to display more than one instance of the scene at a time, like when a user simultaneously opens multiple windows based on a single [`WindowGroup`](windowgroup.md) declaration in your app. For more information about the primary built-in scene types, see [`Windows`](windows.md) and [`Documents`](documents.md).

You configure scenes using modifiers, similar to how you configure views. For example, you can adjust the appearance of the window that contains a scene — if the scene happens to appear in a window — using the [`windowStyle(_:)`](scene/windowstyle(_:).md) modifier. Similarly, you can add menu commands that become available when the scene is in the foreground on certain platforms using the [`commands(content:)`](scene/commands(content:).md) modifier.

## Topics

### Creating scenes
- [protocol Scene](scene.md)
  A part of an app’s user interface with a life cycle managed by the system.
- [struct SceneBuilder](scenebuilder.md)
  A result builder for composing a collection of scenes into a single composite scene.
### Monitoring scene life cycle
- [var scenePhase: ScenePhase](environmentvalues/scenephase.md)
  The current phase of the scene.
- [enum ScenePhase](scenephase.md)
  An indication of a scene’s operational state.
### Managing a settings window
- [struct Settings](settings.md)
  A scene that presents an interface for viewing and modifying an app’s settings.
- [struct SettingsLink](settingslink.md)
  A view that opens the Settings scene defined by an app.
- [struct OpenSettingsAction](opensettingsaction.md)
  An action that presents the settings scene for an app.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.
### Creating a menu bar extra
- [struct MenuBarExtra](menubarextra.md)
  A scene that renders itself as a persistent control in the system menu bar.
- [func menuBarExtraStyle<S>(S) -> some Scene](scene/menubarextrastyle(_:).md)
  Sets the style for menu bar extra created by this scene.
- [protocol MenuBarExtraStyle](menubarextrastyle.md)
  A specification for the appearance and behavior of a menu bar extra scene.
### Creating watch notifications
- [struct WKNotificationScene](wknotificationscene.md)
  A scene which appears in response to receiving the specified category of remote or local notifications.

## See Also

- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenes)*