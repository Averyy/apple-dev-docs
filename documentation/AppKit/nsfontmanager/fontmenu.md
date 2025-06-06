# fontMenu(_:)

**Framework**: AppKit  
**Kind**: method

Returns the menu that’s connected to the font conversion system, creating it if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
func fontMenu(_ create: Bool) -> NSMenu?
```

#### Return Value

The font conversion system menu.

## Parameters

- `create`: If  , the menu object is created if necessary; if  , it is not.

## See Also

- [var isEnabled: Bool](nsfontmanager/isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func fontPanel(Bool) -> NSFontPanel?](nsfontmanager/fontpanel(_:).md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func setFontMenu(NSMenu)](nsfontmanager/setfontmenu(_:).md)
  Records the given menu as the application’s Font menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontmenu(_:))*