# NSToolbarItemGroup.SelectionMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSToolbarItemGroupSelectionMode : NSInteger;
```

## Topics

### Selection modes
- [NSToolbarItemGroup.SelectionMode.momentary](./selectionmode-swift.enum/momentary.md)
  The system temporarily highlights the select group item when the user selects the item.
- [NSToolbarItemGroup.SelectionMode.selectAny](./selectionmode-swift.enum/selectany.md)
  The system toggles a highlight on any item selected.
- [NSToolbarItemGroup.SelectionMode.selectOne](./selectionmode-swift.enum/selectone.md)
  The system displays a highlighted mode on the most recent item selected.
### Initializers
- [init?(rawValue: Int)](./selectionmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Items
- [class NSToolbarItem](../nstoolbaritem.md)
  A single item that appears in a window’s toolbar.
- [class NSToolbarItemGroup](../nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](./controlrepresentation-swift.enum.md)
- [class NSMenuToolbarItem](../nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSSearchToolbarItem](../nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](../nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/selectionmode-swift.enum)*