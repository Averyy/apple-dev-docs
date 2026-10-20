# orderFrontFontPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.

**Availability**:
- macOS

## Declaration

```swift
func orderFrontFontPanel(_ sender: Any?)
```

```objc
- (void) orderFrontFontPanel:(id) sender;
```

## Parameters

- `sender`: The control that sent the message.

## See Also

### Related Documentation
- [func fontPanel(Bool) -> NSFontPanel?](./fontpanel%28_%29.md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [class func setFontPanelFactory(AnyClass?)](./setfontpanelfactory%28_%29.md)
  Sets the class that creates the shared Font panel object.
### Sending Action Methods
- [func addFontTrait(Any?)](./addfonttrait%28_%29.md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](./removefonttrait%28_%29.md)
  Removes a trait from the font.
- [func modifyFont(Any?)](./modifyfont%28_%29.md)
  Modifies a trait of the font.
- [func modifyFontViaPanel(Any?)](./modifyfontviapanel%28_%29.md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](./orderfrontstylespanel%28_%29.md)
  Opens the Font Styles panel.
- [enum NSFontAction](../nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/orderfrontfontpanel(_:))*