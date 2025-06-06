# NSMenu.SelectionMode

**Framework**: AppKit  
**Kind**: enum

Describes how the menu manages selection states of the menu items that belong to the same selection group.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum SelectionMode
```

#### Overview

This doesn’t apply to menu items that have distinct target-action values.

## Topics

### Defining the selection mode
- [NSMenu.SelectionMode.automatic](nsmenu/selectionmode-swift.enum/automatic.md)
  A selection mode where the menu determines the appropriate selection mode based on the context and its constants.
- [NSMenu.SelectionMode.selectAny](nsmenu/selectionmode-swift.enum/selectany.md)
  A selection mode where someone can select multiple items in the menu.
- [NSMenu.SelectionMode.selectOne](nsmenu/selectionmode-swift.enum/selectone.md)
  A selection mode where someone can select at most one menu item in the same selection group at the same time.
### Initializers
- [init?(rawValue: Int)](nsmenu/selectionmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var selectedItems: [NSMenuItem]](nsmenu/selecteditems.md)
  The menu items that are currently selected.
- [var selectionMode: NSMenu.SelectionMode](nsmenu/selectionmode-swift.property.md)
  The selection mode of the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.enum)*