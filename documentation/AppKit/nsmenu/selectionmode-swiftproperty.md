# selectionMode

**Framework**: AppKit  
**Kind**: property

The selection mode of the menu.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var selectionMode: NSMenu.SelectionMode { get set }
```

#### Discussion

The selection mode only affects menu items that belong to the same selection group. A selection group consists of the items with the same target-action.

## See Also

- [var selectedItems: [NSMenuItem]](nsmenu/selecteditems.md)
  The menu items that are currently selected.
- [NSMenu.SelectionMode](nsmenu/selectionmode-swift.enum.md)
  Describes how the menu manages selection states of the menu items that belong to the same selection group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.property)*