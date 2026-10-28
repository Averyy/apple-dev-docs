# NSMenu.SelectionMode.selectAny

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A selection mode where someone can select multiple items in the menu.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case selectAny
```

```c
NSMenuSelectionModeSelectAny
```

## Discussion

A change in selection doesn’t automatically deselect any previously selected item in the same selection group.

## See Also

### Defining the selection mode
- [NSMenu.SelectionMode.automatic](./automatic.md)
  A selection mode where the menu determines the appropriate selection mode based on the context and its constants.
- [NSMenu.SelectionMode.selectOne](./selectone.md)
  A selection mode where someone can select at most one menu item in the same selection group at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.enum/selectany)*