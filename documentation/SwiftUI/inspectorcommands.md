# InspectorCommands

**Framework**: SwiftUI  
**Kind**: struct

A built-in set of commands for manipulating inspectors.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct InspectorCommands
```

#### Overview

`InspectorCommands` include a command for toggling the presented state of the inspector with a keyboard shortcut of Control-Command-I.

These commands are optional and can be explicitly requested by passing a value of this type to the [`commands(content:)`](scene/commands(content:).md) modifier:

```swift
@State var presented = true
WindowGroup {
    MainView()
        .inspector(isPresented: $presented) {
            InspectorView()
        }
}
.commands {
    InspectorCommands()
}
```

## Topics

### Creating a command
- [init()](inspectorcommands/init.md)
  A new value describing the built-in inspector-related commands.

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
- [struct ImportFromDevicesCommands](importfromdevicescommands.md)
  A built-in set of commands that enables importing content from nearby devices.
- [struct EmptyCommands](emptycommands.md)
  An empty group of commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/inspectorcommands)*