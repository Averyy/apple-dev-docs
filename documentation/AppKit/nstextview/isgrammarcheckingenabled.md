# isGrammarCheckingEnabled

**Framework**: AppKit  
**Kind**: property

Enables and disables grammar checking.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var isGrammarCheckingEnabled: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), grammar checking is enabled; if [`false`](https://developer.apple.com/documentation/swift/false), it is disabled.

## See Also

- [var isContinuousSpellCheckingEnabled: Bool](nstextview/iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [var spellCheckerDocumentTag: Int](nstextview/spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [func toggleContinuousSpellChecking(Any?)](nstextview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [func toggleGrammarChecking(Any?)](nstextview/togglegrammarchecking(_:).md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](nstextview/setspellingstate(_:range:).md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/isgrammarcheckingenabled)*