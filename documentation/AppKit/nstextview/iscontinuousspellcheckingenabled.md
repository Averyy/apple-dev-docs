# isContinuousSpellCheckingEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver has continuous spell checking enabled.

**Availability**:
- macOS

## Declaration

```swift
var isContinuousSpellCheckingEnabled: Bool { get set }
```

```objc
@property (getter=isContinuousSpellCheckingEnabled) BOOL continuousSpellCheckingEnabled;
```

## See Also

### Working with the spelling checker
- [var spellCheckerDocumentTag: Int](./spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [func toggleContinuousSpellChecking(Any?)](./togglecontinuousspellchecking%28_%29.md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [var isGrammarCheckingEnabled: Bool](./isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](./togglegrammarchecking%28_%29.md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](./setspellingstate%28_,range%29.md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/iscontinuousspellcheckingenabled)*