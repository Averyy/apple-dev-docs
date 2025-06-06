# updateSpellingPanel(withGrammarString:detail:)

**Framework**: AppKit  
**Kind**: method

Specifies a grammar-analysis detail to highlight in the Spelling panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateSpellingPanel(withGrammarString string: String, detail: [String : Any])
```

## Parameters

- `string`: Problematic grammatical unit identified by  .
- `detail`: One of the grammar-analysis details provided by  .

## See Also

- [var spellingPanel: NSPanel](nsspellchecker/spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](nsspellchecker/substitutionspanel.md)
  Returns the substitutions panel.
- [func updatePanels()](nsspellchecker/updatepanels.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](nsspellchecker/accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](nsspellchecker/substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/updatespellingpanel(withgrammarstring:detail:))*