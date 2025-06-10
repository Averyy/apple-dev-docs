# Commands

**Framework**: SwiftUI  
**Kind**: protocol

Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol Commands
```

## Mentions

- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)

#### Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Implementing commands
- [var body: Self.Body](commands/body-swift.property.md)
  The contents of the command hierarchy.
- [associatedtype Body : Commands](commands/body-swift.associatedtype.md)
  The type of commands that represents the body of this command hierarchy.

## Relationships

### Conforming Types
- [CommandGroup](commandgroup.md)
- [CommandMenu](commandmenu.md)
- [EmptyCommands](emptycommands.md)
- [Group](group.md)
- [ImportFromDevicesCommands](importfromdevicescommands.md)
- [InspectorCommands](inspectorcommands.md)
- [SidebarCommands](sidebarcommands.md)
- [TextEditingCommands](texteditingcommands.md)
- [TextFormattingCommands](textformattingcommands.md)
- [ToolbarCommands](toolbarcommands.md)

## See Also

- [func commands<Content>(content: () -> Content) -> some Scene](scene/commands(content:).md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](scene/commandsremoved.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](scene/commandsreplaced(content:).md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [struct CommandMenu](commandmenu.md)
  Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [struct CommandGroup](commandgroup.md)
  Groups of controls that you can add to existing command menus.
- [struct CommandsBuilder](commandsbuilder.md)
  Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [struct CommandGroupPlacement](commandgroupplacement.md)
  The standard locations that you can place new command groups relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commands)*