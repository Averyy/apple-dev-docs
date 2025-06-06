# CommandGroupPlacement

**Framework**: SwiftUI  
**Kind**: struct

The standard locations that you can place new command groups relative to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CommandGroupPlacement
```

#### Overview

The names of these placements aren’t visible in the user interface, but the discussion for each placement lists the items that it includes.

## Topics

### App interactions
- [static let appInfo: CommandGroupPlacement](commandgroupplacement/appinfo.md)
  Placement for commands that provide information about the app, the terms of the user’s license agreement, and so on.
- [static let appSettings: CommandGroupPlacement](commandgroupplacement/appsettings.md)
  Placement for commands that expose app settings and preferences.
- [static let appTermination: CommandGroupPlacement](commandgroupplacement/apptermination.md)
  Placement for commands that result in app termination.
- [static let appVisibility: CommandGroupPlacement](commandgroupplacement/appvisibility.md)
  Placement for commands that control the visibility of running apps.
- [static let systemServices: CommandGroupPlacement](commandgroupplacement/systemservices.md)
  Placement for commands that expose services other apps provide.
### File manipulation
- [static let importExport: CommandGroupPlacement](commandgroupplacement/importexport.md)
  Placement for commands that relate to importing and exporting data using formats that the app doesn’t natively support.
- [static let newItem: CommandGroupPlacement](commandgroupplacement/newitem.md)
  Placement for commands that create and open different kinds of documents.
- [static let printItem: CommandGroupPlacement](commandgroupplacement/printitem.md)
  Placement for commands related to printing app content.
- [static let saveItem: CommandGroupPlacement](commandgroupplacement/saveitem.md)
  Placement for commands that save open documents and close windows.
### Content updates
- [static let pasteboard: CommandGroupPlacement](commandgroupplacement/pasteboard.md)
  Placement for commands that interact with the Clipboard and manipulate content that is currently selected in the app’s view hierarchy.
- [static let textEditing: CommandGroupPlacement](commandgroupplacement/textediting.md)
  Placement for commands that manipulate and transform text selections.
- [static let textFormatting: CommandGroupPlacement](commandgroupplacement/textformatting.md)
  Placement for commands that manipulate and transform the styles applied to text selections.
- [static let undoRedo: CommandGroupPlacement](commandgroupplacement/undoredo.md)
  Placement for commands that control the Undo Manager.
### Bars
- [static let sidebar: CommandGroupPlacement](commandgroupplacement/sidebar.md)
  Placement for commands that control the app’s sidebar and full-screen modes.
- [static let toolbar: CommandGroupPlacement](commandgroupplacement/toolbar.md)
  Placement for commands that manipulate the toolbar.
### Windows
- [static let singleWindowList: CommandGroupPlacement](commandgroupplacement/singlewindowlist.md)
  Placement for commands that describe and reveal any windows that the app defines.
- [static let windowArrangement: CommandGroupPlacement](commandgroupplacement/windowarrangement.md)
  Placement for commands that arrange all of an app’s windows.
- [static let windowList: CommandGroupPlacement](commandgroupplacement/windowlist.md)
  Placement for commands that describe and reveal the app’s open windows.
- [static let windowSize: CommandGroupPlacement](commandgroupplacement/windowsize.md)
  Placement for commands that control the size of the window.
### Help
- [static let help: CommandGroupPlacement](commandgroupplacement/help.md)
  Placement for commands that present documentation and helpful information to people.

## See Also

- [func commands<Content>(content: () -> Content) -> some Scene](scene/commands(content:).md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](scene/commandsremoved.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](scene/commandsreplaced(content:).md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [protocol Commands](commands.md)
  Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [struct CommandMenu](commandmenu.md)
  Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [struct CommandGroup](commandgroup.md)
  Groups of controls that you can add to existing command menus.
- [struct CommandsBuilder](commandsbuilder.md)
  Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroupplacement)*