# FIMenuKind

**Framework**: Finder Sync  
**Kind**: enum

The different kinds of custom menus that the Finder Sync extension can provide.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum FIMenuKind
```

## Topics

### Constants
- [FIMenuKind.contextualMenuForItems](fimenukind/contextualmenuforitems.md)
  A shortcut menu created when the user control-clicks on an item or a group of selected items inside the Finder window.
- [FIMenuKind.contextualMenuForContainer](fimenukind/contextualmenuforcontainer.md)
  A shortcut menu created when the user control-clicks on the Finder window’s background.
- [FIMenuKind.contextualMenuForSidebar](fimenukind/contextualmenuforsidebar.md)
  A shortcut menu created when the user control-clicks on an item in the sidebar.
- [FIMenuKind.toolbarItemMenu](fimenukind/toolbaritemmenu.md)
  A menu created when the user clicks on the extension’s toolbar button.
### Initializers
- [init?(rawValue: UInt)](fimenukind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fimenukind)*