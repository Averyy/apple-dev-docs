# selectedItems

**Framework**: AppKit  
**Kind**: property

The menu items that are currently selected.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var selectedItems: [NSMenuItem] { get set }
```

#### Discussion

An item selects when its state is [`on`](nscontrol/statevalue/on.md). If the tracking mode is [`NSMenu.SelectionMode.selectOne`](nsmenu/selectionmode-swift.enum/selectone.md) or [`NSMenu.SelectionMode.selectAny`](nsmenu/selectionmode-swift.enum/selectany.md), the property only selects or returns menu items whose show-target action is `nil`.

## See Also

- [var selectionMode: NSMenu.SelectionMode](nsmenu/selectionmode-swift.property.md)
  The selection mode of the menu.
- [NSMenu.SelectionMode](nsmenu/selectionmode-swift.enum.md)
  Describes how the menu manages selection states of the menu items that belong to the same selection group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selecteditems)*