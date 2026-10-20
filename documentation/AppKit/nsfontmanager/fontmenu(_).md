# fontMenu(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu that’s connected to the font conversion system, creating it if necessary.

**Availability**:
- macOS

## Declaration

```swift
func fontMenu(_ create: Bool) -> NSMenu?
```

```objc
- (NSMenu *) fontMenu:(BOOL) create;
```

#### Return Value

The font conversion system menu.

## Parameters

- `create`: If [`true`](../../Swift/true.md), the menu object is created if necessary; if [`false`](../../Swift/false.md), it is not.

## See Also

### Managing the Font Panel and Font Menu
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func fontPanel(Bool) -> NSFontPanel?](./fontpanel%28_%29.md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func setFontMenu(NSMenu)](./setfontmenu%28_%29.md)
  Records the given menu as the application’s Font menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontmenu(_:))*