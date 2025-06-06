# removeFontTrait(_:)

**Framework**: AppKit  
**Kind**: method

Removes a trait from the font.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeFontTrait(_ sender: Any?)
```

#### Discussion

By default, the action message is [`changeFont:`](https://developer.apple.com/documentation/objectivec/nsobject/1462311-changefont). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](nsfontmanager/convert(_:).md) message, the receiver converts the font by removing the trait specified by `sender`. This trait is determined by sending a `tag` message to `sender` and interpreting it as a font trait mask for a [`convert(_:toNotHaveTrait:)`](nsfontmanager/convert(_:tonothavetrait:).md) message.

## Parameters

- `sender`: The control that sent the message.

## See Also

- [func addFontTrait(Any?)](nsfontmanager/addfonttrait(_:).md)
  Adds a trait to the font.
- [func modifyFont(Any?)](nsfontmanager/modifyfont(_:).md)
  Modifies a trait of the font.
- [func modifyFontViaPanel(Any?)](nsfontmanager/modifyfontviapanel(_:).md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](nsfontmanager/orderfrontstylespanel(_:).md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](nsfontmanager/orderfrontfontpanel(_:).md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.
- [enum NSFontAction](nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/removefonttrait(_:))*