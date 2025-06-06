# substitutionsPanelAccessoryViewController

**Framework**: AppKit  
**Kind**: property

Sets the substitutions panel’s accessory view.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var substitutionsPanelAccessoryViewController: NSViewController? { get set }
```

#### Discussion

The accessory view controller can accommodate any custom view you want to display with the substitutions panel. The accessory view controller’s view is displayed below the substitutions list and the panel automatically resizes to accommodate the accessory view.

This method posts a notification named  [`didResizeNotification`](nswindow/didresizenotification.md) with the substitutions panel object to the default notification center.

## Parameters

- `accessoryController`: The accessory view controller or   if there is none.

## See Also

- [var spellingPanel: NSPanel](nsspellchecker/spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](nsspellchecker/substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](nsspellchecker/updatespellingpanel(withgrammarstring:detail:).md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](nsspellchecker/updatepanels.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](nsspellchecker/accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/substitutionspanelaccessoryviewcontroller)*