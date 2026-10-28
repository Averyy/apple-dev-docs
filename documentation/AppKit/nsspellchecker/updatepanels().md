# updatePanels()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the available panels to account for user changes.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func updatePanels()
```

```objc
- (void) updatePanels;
```

## Discussion

This method should be called when a client changes some relevant setting, such as what kind of spelling, grammar checking, or substitutions it uses.

## See Also

### Managing Panels
- [var spellingPanel: NSPanel](./spellingpanel.md)
  Returns the spell checker’s panel.
- [var substitutionsPanel: NSPanel](./substitutionspanel.md)
  Returns the substitutions panel.
- [func updateSpellingPanel(withGrammarString: String, detail: [String : Any])](./updatespellingpanel%28withgrammarstring,detail%29.md)
  Specifies a grammar-analysis detail to highlight in the Spelling panel.
- [var accessoryView: NSView?](./accessoryview.md)
  Makes a view an accessory of the Spelling panel by making it a subview of the panel’s content view.
- [var substitutionsPanelAccessoryViewController: NSViewController?](./substitutionspanelaccessoryviewcontroller.md)
  Sets the substitutions panel’s accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/updatepanels())*