# addFontTrait(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a trait to the font.

**Availability**:
- macOS

## Declaration

```swift
func addFontTrait(_ sender: Any?)
```

```objc
- (void) addFontTrait:(id) sender;
```

## Discussion

By default, the action message is [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md). This action method causes the receiver to send its action message up the responder chain.

When a responder replies by providing a font to convert in a [`convert(_:)`](./convert%28_%29.md) message, the receiver converts the font by adding the trait specified by `sender`. This trait is determined by sending a `tag` message to `sender` and interpreting it as a font trait mask for a [`convert(_:toHaveTrait:)`](./convert%28_,tohavetrait%29.md) message.

## Parameters

- `sender`: The control that sent the message.

## See Also

### Sending Action Methods
- [func removeFontTrait(Any?)](./removefonttrait%28_%29.md)
  Removes a trait from the font.
- [func modifyFont(Any?)](./modifyfont%28_%29.md)
  Modifies a trait of the font.
- [func modifyFontViaPanel(Any?)](./modifyfontviapanel%28_%29.md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](./orderfrontstylespanel%28_%29.md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](./orderfrontfontpanel%28_%29.md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.
- [enum NSFontAction](../nsfontaction.md)
  Actions that modify a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/addfonttrait(_:))*