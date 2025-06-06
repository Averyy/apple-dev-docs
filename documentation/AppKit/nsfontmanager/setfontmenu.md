# setFontMenu(_:)

**Framework**: AppKit  
**Kind**: method

Records the given menu as the application’s Font menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func setFontMenu(_ newMenu: NSMenu)
```

## Parameters

- `newMenu`: The new Font menu.

## See Also

- [var isEnabled: Bool](nsfontmanager/isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func fontPanel(Bool) -> NSFontPanel?](nsfontmanager/fontpanel(_:).md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func fontMenu(Bool) -> NSMenu?](nsfontmanager/fontmenu(_:).md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setfontmenu(_:))*