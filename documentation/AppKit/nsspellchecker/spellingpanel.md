# spellingPanel

**Framework**: AppKit  
**Kind**: property

Returns the spell checker’s panel.

**Availability**:
- macOS ?+

## Declaration

```swift
var spellingPanel: NSPanel { get }
```

#### Return Value

The spell checking panel.

## See Also

- [var substitutionsPanel: NSPanel](nsspellchecker/substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](nsspellchecker/updatespellingpanel(withgrammarstring:detail:).md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [func updatePanels()](nsspellchecker/updatepanels.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](nsspellchecker/accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](nsspellchecker/substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/spellingpanel)*