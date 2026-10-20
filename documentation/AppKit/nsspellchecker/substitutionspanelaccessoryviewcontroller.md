# substitutionsPanelAccessoryViewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the substitutions panel’s accessory view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var substitutionsPanelAccessoryViewController: NSViewController? { get set }
```

```objc
@property (strong, nullable) NSViewController * substitutionsPanelAccessoryViewController;
```

#### Discussion

The accessory view controller can accommodate any custom view you want to display with the substitutions panel. The accessory view controller’s view is displayed below the substitutions list and the panel automatically resizes to accommodate the accessory view.

This method posts a notification named  [`didResizeNotification`](../nswindow/didresizenotification.md) with the substitutions panel object to the default notification center.

## Parameters

- `accessoryController`: The accessory view controller or `nil` if there is none.

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
- [var accessoryView: NSView?](./accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/substitutionspanelaccessoryviewcontroller)*