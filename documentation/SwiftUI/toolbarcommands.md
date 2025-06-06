# ToolbarCommands

**Framework**: SwiftUI  
**Kind**: struct

A built-in set of commands for manipulating window toolbars.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct ToolbarCommands
```

#### Overview

These commands are optional and can be explicitly requested by passing a value of this type to the [`commands(content:)`](scene/commands(content:).md) modifier.

## Topics

### Creating the command group
- [init()](toolbarcommands/init.md)
  A new value describing the built-in toolbar-related commands.

## Relationships

### Conforms To
- [Commands](commands.md)

## See Also

- [struct SidebarCommands](sidebarcommands.md)
  A built-in set of commands for manipulating window sidebars.
- [struct TextEditingCommands](texteditingcommands.md)
  A built-in group of commands for searching, editing, and transforming selections of text.
- [struct TextFormattingCommands](textformattingcommands.md)
  A built-in set of commands for transforming the styles applied to selections of text.
- [struct ImportFromDevicesCommands](importfromdevicescommands.md)
  A built-in set of commands that enables importing content from nearby devices.
- [struct InspectorCommands](inspectorcommands.md)
  A built-in set of commands for manipulating inspectors.
- [struct EmptyCommands](emptycommands.md)
  An empty group of commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcommands)*