# modifyFontViaPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Modifies a font trait using input from the Font panel.

**Availability**:
- macOS

## Declaration

```swift
func modifyFontViaPanel(_ sender: Any?)
```

```objc
- (void) modifyFontViaPanel:(id) sender;
```

#### Discussion

By default, the action message is [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](./convert%28_%29.md) message, the receiver converts the font by sending a [`convert(_:)`](../nsfontpanel/convert%28_%29.md) message to the Font panel. The panel in turn may send [`convert(_:toFamily:)`](./convert%28_,tofamily%29.md), [`convert(_:toHaveTrait:)`](./convert%28_,tohavetrait%29.md), and other specific conversion methods to make its change.

## Parameters

- `sender`: The control that sent the message.

## See Also

### Sending Action Methods
- [func addFontTrait(Any?)](./addfonttrait%28_%29.md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](./removefonttrait%28_%29.md)
  Removes a trait from the font.
- [func modifyFont(Any?)](./modifyfont%28_%29.md)
  Modifies a trait of the font.
- [func orderFrontStylesPanel(Any?)](./orderfrontstylespanel%28_%29.md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](./orderfrontfontpanel%28_%29.md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.
- [enum NSFontAction](../nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/modifyfontviapanel(_:))*