# NSMenu.SelectionMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Describes how the menu manages selection states of the menu items that belong to the same selection group.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum SelectionMode
```

```c
enum NSMenuSelectionMode : NSInteger;
```

#### Overview

This doesn’t apply to menu items that have distinct target-action values.

## Topics

### Defining the selection mode
- [NSMenu.SelectionMode.automatic](./selectionmode-swift.enum/automatic.md)
  A selection mode where the menu determines the appropriate selection mode based on the context and its constants.
- [NSMenu.SelectionMode.selectAny](./selectionmode-swift.enum/selectany.md)
  A selection mode where someone can select multiple items in the menu.
- [NSMenu.SelectionMode.selectOne](./selectionmode-swift.enum/selectone.md)
  A selection mode where someone can select at most one menu item in the same selection group at the same time.
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

### Selecting Items
- [var selectedItems: [NSMenuItem]](./selecteditems.md)
  The menu items that are currently selected.
- [var selectionMode: NSMenu.SelectionMode](./selectionmode-swift.property.md)
  The selection mode of the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.enum)*