# fontPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the application’s shared Font panel object, creating it if necessary.

**Availability**:
- macOS

## Declaration

```swift
func fontPanel(_ create: Bool) -> NSFontPanel?
```

```objc
- (NSFontPanel *) fontPanel:(BOOL) create;
```

## Return Value

The application’s shared Font panel object.

## Parameters

- `create`: If [`true`](../../Swift/true.md), the Font panel object is created if necessary; if [`false`](../../Swift/false.md), it is not.

## See Also

### Related Documentation
- [class var shared: NSFontPanel](../nsfontpanel/shared.md)
  Returns the single `NSFontPanel` instance for the application, creating it if necessary.
- [class func setFontPanelFactory(AnyClass?)](./setfontpanelfactory%28_%29.md)
  Sets the class that creates the shared Font panel object.
- [class var sharedFontPanelExists: Bool](../nsfontpanel/sharedfontpanelexists.md)
  A Boolean value that indicates whether the shared Font panel has been created.
### Managing the Font Panel and Font Menu
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func setFontMenu(NSMenu)](./setfontmenu%28_%29.md)
  Records the given menu as the application’s Font menu.
- [func fontMenu(Bool) -> NSMenu?](./fontmenu%28_%29.md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontpanel(_:))*