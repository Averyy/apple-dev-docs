# NSMenu.SelectionMode.selectOne

**Framework**: AppKit  
**Kind**: case

A selection mode where someone can select at most one menu item in the same selection group at the same time.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case selectOne
```

#### Discussion

A change in selection deselects any previously selected item.

## See Also

- [NSMenu.SelectionMode.automatic](nsmenu/selectionmode-swift.enum/automatic.md)
  A selection mode where the menu determines the appropriate selection mode based on the context and its constants.
- [NSMenu.SelectionMode.selectAny](nsmenu/selectionmode-swift.enum/selectany.md)
  A selection mode where someone can select multiple items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/selectionmode-swift.enum/selectone)*