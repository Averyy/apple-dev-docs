# spellCheckerDocumentTag

**Framework**: AppKit  
**Kind**: property

A tag identifying the text view’s text as a document for the spell checker server.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var spellCheckerDocumentTag: Int { get }
```

#### Discussion

The document tag is obtained by sending a [`uniqueSpellDocumentTag()`](nsspellchecker/uniquespelldocumenttag().md) message to the spell server the first time this method is invoked for a particular group of text views. See the [`NSSpellChecker`](nsspellchecker.md)and [`NSSpellServer`](https://developer.apple.com/documentation/Foundation/NSSpellServer)class specifications for more information on how this tag is used.

## See Also

- [var isContinuousSpellCheckingEnabled: Bool](nstextview/iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [func toggleContinuousSpellChecking(Any?)](nstextview/togglecontinuousspellchecking(_:).md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [var isGrammarCheckingEnabled: Bool](nstextview/isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](nstextview/togglegrammarchecking(_:).md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](nstextview/setspellingstate(_:range:).md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/spellcheckerdocumenttag)*