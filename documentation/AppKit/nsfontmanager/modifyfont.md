# modifyFont(_:)

**Framework**: AppKit  
**Kind**: method

Modifies a trait of the font.

**Availability**:
- macOS ?+

## Declaration

```swift
func modifyFont(_ sender: Any?)
```

#### Discussion

By default, the action message is [`changeFont:`](https://developer.apple.com/documentation/objectivec/nsobject/1462311-changefont). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](nsfontmanager/convert(_:).md) message, the receiver converts the font in the manner specified by `sender`. The conversion is determined by sending a `tag` message to `sender` and invoking a corresponding method:

| Sender’s Tag | Method Used |
| --- | --- |
| `NSNoFontChangeAction` | None; the font is returned unchanged. |
| `NSViaPanelFontAction` | The Font panel’s [`convert(_:)`](nsfontpanel/convert(_:).md). |
| `NSAddTraitFontAction` | [`convert(_:toHaveTrait:)`](nsfontmanager/convert(_:tohavetrait:).md). |
| `NSRemoveTraitFontAction` | [`convert(_:toNotHaveTrait:)`](nsfontmanager/convert(_:tonothavetrait:).md). |
| `NSSizeUpFontAction` | [`convert(_:toSize:)`](nsfontmanager/convert(_:tosize:).md). |
| `NSSizeDownFontAction` | [`convert(_:toSize:)`](nsfontmanager/convert(_:tosize:).md). |
| `NSHeavierFontAction` | [`convertWeight(_:of:)`](nsfontmanager/convertweight(_:of:).md). |
| `NSLighterFontAction` | [`convertWeight(_:of:)`](nsfontmanager/convertweight(_:of:).md). |

## Parameters

- `sender`: The control that sent the message.

## See Also

- [func addFontTrait(Any?)](nsfontmanager/addfonttrait(_:).md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](nsfontmanager/removefonttrait(_:).md)
  Removes a trait from the font.
- [func modifyFontViaPanel(Any?)](nsfontmanager/modifyfontviapanel(_:).md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](nsfontmanager/orderfrontstylespanel(_:).md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](nsfontmanager/orderfrontfontpanel(_:).md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.
- [enum NSFontAction](nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/modifyfont(_:))*