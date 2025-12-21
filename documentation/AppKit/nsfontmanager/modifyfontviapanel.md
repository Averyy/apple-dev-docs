# modifyFontViaPanel(_:)

**Framework**: AppKit  
**Kind**: method

Modifies a font trait using input from the Font panel.

**Availability**:
- macOS ?+

## Declaration

```swift
func modifyFontViaPanel(_ sender: Any?)
```

#### Discussion

By default, the action message is [`changeFont:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/changeFont:). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](nsfontmanager/convert(_:).md) message, the receiver converts the font by sending a [`convert(_:)`](nsfontpanel/convert(_:).md) message to the Font panel. The panel in turn may send [`convert(_:toFamily:)`](nsfontmanager/convert(_:tofamily:).md), [`convert(_:toHaveTrait:)`](nsfontmanager/convert(_:tohavetrait:).md), and other specific conversion methods to make its change.

## Parameters

- `sender`: The control that sent the message.

## See Also

- [func addFontTrait(Any?)](nsfontmanager/addfonttrait(_:).md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](nsfontmanager/removefonttrait(_:).md)
  Removes a trait from the font.
- [func modifyFont(Any?)](nsfontmanager/modifyfont(_:).md)
  Modifies a trait of the font.
- [func orderFrontStylesPanel(Any?)](nsfontmanager/orderfrontstylespanel(_:).md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](nsfontmanager/orderfrontfontpanel(_:).md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.
- [enum NSFontAction](nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/modifyfontviapanel(_:))*