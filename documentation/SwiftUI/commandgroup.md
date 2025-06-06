# CommandGroup

**Framework**: SwiftUI  
**Kind**: struct

Groups of controls that you can add to existing command menus.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct CommandGroup<Content> where Content : View
```

#### Overview

In macOS, SwiftUI realizes command groups as collections of menu items in a menu bar menu. In iOS, iPadOS, and tvOS, SwiftUI creates key commands for each of a group’s commands that has a keyboard shortcut.

## Topics

### Creating a command group
- [init(after: CommandGroupPlacement, addition: () -> Content)](commandgroup/init(after:addition:).md)
  A value describing the addition of the given views to the end of the indicated group.
- [init(before: CommandGroupPlacement, addition: () -> Content)](commandgroup/init(before:addition:).md)
  A value describing the addition of the given views to the beginning of the indicated group.
- [init(replacing: CommandGroupPlacement, addition: () -> Content)](commandgroup/init(replacing:addition:).md)
  A value describing the complete replacement of the contents of the indicated group with the given views.

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
- [struct CommandMenu](commandmenu.md)
  Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [struct CommandsBuilder](commandsbuilder.md)
  Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [struct CommandGroupPlacement](commandgroupplacement.md)
  The standard locations that you can place new command groups relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroup)*