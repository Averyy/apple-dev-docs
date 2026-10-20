# accessoryView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.

**Availability**:
- macOS

## Declaration

```swift
var accessoryView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * accessoryView;
```

#### Discussion

The accessory view can be any custom view you want to display with the spelling panel. The accessory view is displayed below the spelling checker and the panel automatically resizes to accommodate the accessory view.

This method posts a notification named [`didResizeNotification`](../nswindow/didresizenotification.md) with the Spelling panel object to the default notification center.

## Parameters

- `aView`: The accessory view displayed in the receiver.

## See Also

### Managing Panels
- [var spellingPanel: NSPanel](./spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](./substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](./updatespellingpanel%28withgrammarstring,detail%29.md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](./updatepanels%28%29.md)
  Updates the available panels to account for user changes.
- [var substitutionsPanelAccessoryViewController: NSViewController?](./substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/accessoryview)*