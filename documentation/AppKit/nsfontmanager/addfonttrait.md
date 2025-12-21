# addFontTrait(_:)

**Framework**: AppKit  
**Kind**: method

Adds a trait to the font.

**Availability**:
- macOS ?+

## Declaration

```swift
func addFontTrait(_ sender: Any?)
```

#### Discussion

By default, the action message is [`changeFont:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/changeFont:). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](nsfontmanager/convert(_:).md) message, the receiver converts the font by adding the trait specified by `sender`. This trait is determined by sending a `tag` message to `sender` and interpreting it as a font trait mask for a [`convert(_:toHaveTrait:)`](nsfontmanager/convert(_:tohavetrait:).md) message.

## Parameters

- `sender`: The control that sent the message.

## See Also

- [func removeFontTrait(Any?)](nsfontmanager/removefonttrait(_:).md)
  Removes a trait from the font.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/addfonttrait(_:))*