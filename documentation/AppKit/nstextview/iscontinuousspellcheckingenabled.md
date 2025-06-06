# isContinuousSpellCheckingEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver has continuous spell checking enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isContinuousSpellCheckingEnabled: Bool { get set }
```

## See Also

- [var spellCheckerDocumentTag: Int](nstextview/spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [func toggleContinuousSpellChecking(Any?)](nstextview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [var isGrammarCheckingEnabled: Bool](nstextview/isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](nstextview/togglegrammarchecking(_:).md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](nstextview/setspellingstate(_:range:).md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/iscontinuousspellcheckingenabled)*