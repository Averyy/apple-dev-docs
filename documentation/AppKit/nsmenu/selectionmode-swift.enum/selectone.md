# NSMenu.SelectionMode.selectOne

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A selection mode where someone can select at most one menu item in the same selection group at the same time.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case selectOne
```

```c
NSMenuSelectionModeSelectOne
```

#### Discussion

A change in selection deselects any previously selected item.

## See Also

### Defining the selection mode
- [NSMenu.SelectionMode.automatic](./automatic.md)
  A selection mode where the menu determines the appropriate selection mode based on the context and its constants.
- [NSMenu.SelectionMode.selectAny](./selectany.md)
  A selection mode where someone can select multiple items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.enum/selectone)*