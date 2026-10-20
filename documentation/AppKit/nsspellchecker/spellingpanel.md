# spellingPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the spell checker’s panel.

**Availability**:
- macOS

## Declaration

```swift
var spellingPanel: NSPanel { get }
```

```objc
@property (strong, readonly) NSPanel * spellingPanel;
```

#### Return Value

The spell checking panel.

## See Also

### Managing Panels
- [var substitutionsPanel: NSPanel](./substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](./updatespellingpanel%28withgrammarstring,detail%29.md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](./updatepanels%28%29.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](./accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](./substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/spellingpanel)*