# setFontMenu(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Records the given menu as the application’s Font menu.

**Availability**:
- macOS

## Declaration

```swift
func setFontMenu(_ newMenu: NSMenu)
```

```objc
- (void) setFontMenu:(NSMenu *) newMenu;
```

## Parameters

- `newMenu`: The new Font menu.

## See Also

### Managing the Font Panel and Font Menu
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func fontPanel(Bool) -> NSFontPanel?](./fontpanel%28_%29.md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func fontMenu(Bool) -> NSMenu?](./fontmenu%28_%29.md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setfontmenu(_:))*