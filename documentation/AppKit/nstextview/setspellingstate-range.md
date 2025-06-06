# setSpellingState(_:range:)

**Framework**: AppKit  
**Kind**: method

Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setSpellingState(_ value: Int, range charRange: NSRange)
```

#### Discussion

May be called or overridden to control setting of spelling and grammar indicators on text, used to highlight portions of the text that are flagged for spelling or grammar issues.

## Parameters

- `value`: The spelling state value to set. Possible values, for the temporary attribute on the layout manager using the key NSSpellingStateAttributeName, are:
- `charRange`: The character range over which to set the given spelling state.

## See Also

- [var isContinuousSpellCheckingEnabled: Bool](nstextview/iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [var spellCheckerDocumentTag: Int](nstextview/spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [func toggleContinuousSpellChecking(Any?)](nstextview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [var isGrammarCheckingEnabled: Bool](nstextview/isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](nstextview/togglegrammarchecking(_:).md)
  Changes the state of grammar checking from enabled to disabled and vice versa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/setspellingstate(_:range:))*