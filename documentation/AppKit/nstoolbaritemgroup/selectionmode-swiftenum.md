# NSToolbarItemGroup.SelectionMode

**Framework**: AppKit  
**Kind**: enum

A value that indicates how a grouped toolbar item selects its subitems.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
enum SelectionMode
```

## Topics

### Selection modes
- [NSToolbarItemGroup.SelectionMode.momentary](nstoolbaritemgroup/selectionmode-swift.enum/momentary.md)
  The system temporarily highlights the select group item when the user selects the item.
- [NSToolbarItemGroup.SelectionMode.selectAny](nstoolbaritemgroup/selectionmode-swift.enum/selectany.md)
  The system toggles a highlight on any item selected.
- [NSToolbarItemGroup.SelectionMode.selectOne](nstoolbaritemgroup/selectionmode-swift.enum/selectone.md)
  The system displays a highlighted mode on the most recent item selected.
### Initializers
- [init?(rawValue: Int)](nstoolbaritemgroup/selectionmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSToolbarItem](nstoolbaritem.md)
  A single item that appears in a window’s toolbar.
- [class NSToolbarItemGroup](nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [class NSMenuToolbarItem](nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSSearchToolbarItem](nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/selectionmode-swift.enum)*