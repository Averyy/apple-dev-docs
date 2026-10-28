# substitutionsPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the substitutions panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var substitutionsPanel: NSPanel { get }
```

```objc
@property (strong, readonly) NSPanel * substitutionsPanel;
```

## Return Value

The substitutions checking panel.

## See Also

### Managing Panels
- [var spellingPanel: NSPanel](./spellingpanel.md)
  Returns the spell checker’s panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](./updatespellingpanel%28withgrammarstring,detail%29.md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](./updatepanels%28%29.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](./accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](./substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/substitutionspanel)*