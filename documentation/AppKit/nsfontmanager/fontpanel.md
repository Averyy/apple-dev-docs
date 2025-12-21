# fontPanel(_:)

**Framework**: AppKit  
**Kind**: method

Returns the application’s shared Font panel object, creating it if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
func fontPanel(_ create: Bool) -> NSFontPanel?
```

#### Return Value

The application’s shared Font panel object.

## Parameters

- `create`: If  , the Font panel object is created if necessary; if  , it is not.

## See Also

- [class var shared: NSFontPanel](nsfontpanel/shared.md)
  Returns the single `NSFontPanel` instance for the application, creating it if necessary.
- [class func setFontPanelFactory(AnyClass?)](nsfontmanager/setfontpanelfactory(_:).md)
  Sets the class that creates the shared Font panel object.
- [class var sharedFontPanelExists: Bool](nsfontpanel/sharedfontpanelexists.md)
  A Boolean value that indicates whether the shared Font panel has been created.
- [var isEnabled: Bool](nsfontmanager/isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func setFontMenu(NSMenu)](nsfontmanager/setfontmenu(_:).md)
  Records the given menu as the application’s Font menu.
- [func fontMenu(Bool) -> NSMenu?](nsfontmanager/fontmenu(_:).md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/fontpanel(_:))*