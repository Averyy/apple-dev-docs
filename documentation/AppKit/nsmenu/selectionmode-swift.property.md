# selectionMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The selection mode of the menu.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var selectionMode: NSMenu.SelectionMode { get set }
```

```objc
@property NSMenuSelectionMode selectionMode;
```

#### Discussion

The selection mode only affects menu items that belong to the same selection group. A selection group consists of the items with the same target-action.

## See Also

### Selecting Items
- [var selectedItems: [NSMenuItem]](./selecteditems.md)
  The menu items that are currently selected.
- [NSMenu.SelectionMode](./selectionmode-swift.enum.md)
  Describes how the menu manages selection states of the menu items that belong to the same selection group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.property)*