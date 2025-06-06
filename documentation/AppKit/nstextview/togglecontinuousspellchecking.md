# toggleContinuousSpellChecking(_:)

**Framework**: AppKit  
**Kind**: method

Toggles whether continuous spell checking is enabled for the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func toggleContinuousSpellChecking(_ sender: Any?)
```

## Parameters

- `sender`: The control sending the message; may be  .

## See Also

- [var isContinuousSpellCheckingEnabled: Bool](nstextview/iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [var spellCheckerDocumentTag: Int](nstextview/spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [var isGrammarCheckingEnabled: Bool](nstextview/isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](nstextview/togglegrammarchecking(_:).md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](nstextview/setspellingstate(_:range:).md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/togglecontinuousspellchecking(_:))*