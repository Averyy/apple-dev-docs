# orderFrontFontPanel(_:)

**Framework**: AppKit  
**Kind**: method

Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.

**Availability**:
- macOS ?+

## Declaration

```swift
func orderFrontFontPanel(_ sender: Any?)
```

## Parameters

- `sender`: The control that sent the message.

## See Also

- [func fontPanel(Bool) -> NSFontPanel?](nsfontmanager/fontpanel(_:).md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [class func setFontPanelFactory(AnyClass?)](nsfontmanager/setfontpanelfactory(_:).md)
  Sets the class that creates the shared Font panel object.
- [func addFontTrait(Any?)](nsfontmanager/addfonttrait(_:).md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](nsfontmanager/removefonttrait(_:).md)
  Removes a trait from the font.
- [func modifyFont(Any?)](nsfontmanager/modifyfont(_:).md)
  Modifies a trait of the font.
- [func modifyFontViaPanel(Any?)](nsfontmanager/modifyfontviapanel(_:).md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](nsfontmanager/orderfrontstylespanel(_:).md)
  Opens the Font Styles panel.
- [enum NSFontAction](nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/orderfrontfontpanel(_:))*