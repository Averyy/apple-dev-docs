# textEditing

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Placement for commands that manipulate and transform text selections.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let textEditing: CommandGroupPlacement
```

#### Discussion

By default, this group includes the following commands in macOS:

- Find submenu
- Spelling and Grammar submenu
- Substitutions submenu
- Transformations submenu
- Speech submenu

## See Also

### Content updates
- [static let pasteboard: CommandGroupPlacement](./pasteboard.md)
  Placement for commands that interact with the Clipboard and manipulate content that is currently selected in the app’s view hierarchy.
- [static let textFormatting: CommandGroupPlacement](./textformatting.md)
  Placement for commands that manipulate and transform the styles applied to text selections.
- [static let undoRedo: CommandGroupPlacement](./undoredo.md)
  Placement for commands that control the Undo Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroupplacement/textediting)*