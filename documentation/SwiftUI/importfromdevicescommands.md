# ImportFromDevicesCommands

**Framework**: SwiftUI  
**Kind**: struct

A built-in set of commands that enables importing content from nearby devices.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct ImportFromDevicesCommands
```

#### Overview

This set of commands adds items based on nearby devices and capabilities, like taking photos or scanning documents. Views can receive imported content from these menu items by using the [`importsItemProviders(_:onImport:)`](view/importsitemproviders(_:onimport:).md) modifier.

These commands are optional and you can explicitly request them by passing a value of this type to the [`commands(content:)`](scene/commands(content:).md) modifier.

## Topics

### Creating the command group
- [init()](importfromdevicescommands/init.md)
  Creates a new set of device import commands.

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
- [struct ToolbarCommands](toolbarcommands.md)
  A built-in set of commands for manipulating window toolbars.
- [struct InspectorCommands](inspectorcommands.md)
  A built-in set of commands for manipulating inspectors.
- [struct EmptyCommands](emptycommands.md)
  An empty group of commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/importfromdevicescommands)*