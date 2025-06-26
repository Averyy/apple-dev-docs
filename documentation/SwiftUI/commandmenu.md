# CommandMenu

**Framework**: SwiftUI  
**Kind**: struct

Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CommandMenu<Content> where Content : View
```

## Mentions

- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)
- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)

#### Overview

Command menus are realized as menu bar menus on macOS, inserted between the built-in View and Window menus in order of declaration. On iOS, iPadOS, and tvOS, SwiftUI creates key commands for each of a menu’s commands that has a keyboard shortcut.

## Topics

### Creating a command menu
- [init(_:content:)](commandmenu/init(_:content:).md)
  Creates a new menu with a localized name for a collection of app- specific commands, inserted in the standard location for app menus (after the View menu, in order with other menus declared without an explicit location).

## Relationships

### Conforms To
- [Commands](commands.md)

## See Also

- [func commands<Content>(content: () -> Content) -> some Scene](scene/commands(content:).md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](scene/commandsremoved.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](scene/commandsreplaced(content:).md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [protocol Commands](commands.md)
  Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [struct CommandGroup](commandgroup.md)
  Groups of controls that you can add to existing command menus.
- [struct CommandsBuilder](commandsbuilder.md)
  Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [struct CommandGroupPlacement](commandgroupplacement.md)
  The standard locations that you can place new command groups relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandmenu)*