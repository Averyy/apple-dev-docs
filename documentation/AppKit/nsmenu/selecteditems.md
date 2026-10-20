# selectedItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu items that are currently selected.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var selectedItems: [NSMenuItem] { get set }
```

```objc
@property (copy) NSArray<NSMenuItem *> * selectedItems;
```

#### Discussion

An item selects when its state is [`on`](../nscontrol/statevalue/on.md). If the tracking mode is [`NSMenu.SelectionMode.selectOne`](./selectionmode-swift.enum/selectone.md) or [`NSMenu.SelectionMode.selectAny`](./selectionmode-swift.enum/selectany.md), the property only selects or returns menu items whose show-target action is `nil`.

## See Also

### Selecting Items
- [var selectionMode: NSMenu.SelectionMode](./selectionmode-swift.property.md)
  The selection mode of the menu.
- [NSMenu.SelectionMode](./selectionmode-swift.enum.md)
  Describes how the menu manages selection states of the menu items that belong to the same selection group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selecteditems)*