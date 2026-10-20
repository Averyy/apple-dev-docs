# updateSpellingPanel(withGrammarString:detail:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies a grammar-analysis detail to highlight in the Spelling panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateSpellingPanel(withGrammarString string: String, detail: [String : Any])
```

```objc
- (void) updateSpellingPanelWithGrammarString:(NSString *) string detail:(NSDictionary<NSString *,id> *) detail;
```

## Parameters

- `string`: Problematic grammatical unit identified by [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](./checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md).
- `detail`: One of the grammar-analysis details provided by [`checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)`](./checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md).

## See Also

### Managing Panels
- [var spellingPanel: NSPanel](./spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](./substitutionspanel.md)
  Returns the substitutions panel.
- [func updatePanels()](./updatepanels%28%29.md)
  Updates the available panels to account for user changes.
- [var accessoryView: NSView?](./accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](./substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/updatespellingpanel(withgrammarstring:detail:))*