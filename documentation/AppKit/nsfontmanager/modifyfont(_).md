# modifyFont(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Modifies a trait of the font.

**Availability**:
- macOS

## Declaration

```swift
func modifyFont(_ sender: Any?)
```

```objc
- (void) modifyFont:(id) sender;
```

#### Discussion

By default, the action message is [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](./convert%28_%29.md) message, the receiver converts the font in the manner specified by `sender`. The conversion is determined by sending a `tag` message to `sender` and invoking a corresponding method:

| Sender’s Tag | Method Used |
| --- | --- |
| `NSNoFontChangeAction` | None; the font is returned unchanged. |
| `NSViaPanelFontAction` | The Font panel’s [`convert(_:)`](../nsfontpanel/convert%28_%29.md). |
| `NSAddTraitFontAction` | [`convert(_:toHaveTrait:)`](./convert%28_,tohavetrait%29.md). |
| `NSRemoveTraitFontAction` | [`convert(_:toNotHaveTrait:)`](./convert%28_,tonothavetrait%29.md). |
| `NSSizeUpFontAction` | [`convert(_:toSize:)`](./convert%28_,tosize%29.md). |
| `NSSizeDownFontAction` | [`convert(_:toSize:)`](./convert%28_,tosize%29.md). |
| `NSHeavierFontAction` | [`convertWeight(_:of:)`](./convertweight%28_,of%29.md). |
| `NSLighterFontAction` | [`convertWeight(_:of:)`](./convertweight%28_,of%29.md). |

## Parameters

- `sender`: The control that sent the message.

## See Also

### Sending Action Methods
- [func addFontTrait(Any?)](./addfonttrait%28_%29.md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](./removefonttrait%28_%29.md)
  Removes a trait from the font.
- [func modifyFontViaPanel(Any?)](./modifyfontviapanel%28_%29.md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](./orderfrontstylespanel%28_%29.md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](./orderfrontfontpanel%28_%29.md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.
- [enum NSFontAction](../nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/modifyfont(_:))*