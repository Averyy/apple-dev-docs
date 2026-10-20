# isGrammarCheckingEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Enables and disables grammar checking.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isGrammarCheckingEnabled: Bool { get set }
```

```objc
@property (getter=isGrammarCheckingEnabled) BOOL grammarCheckingEnabled;
```

#### Discussion

If [`true`](../../Swift/true.md), grammar checking is enabled; if [`false`](../../Swift/false.md), it is disabled.

## See Also

### Working with the spelling checker
- [var isContinuousSpellCheckingEnabled: Bool](./iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [var spellCheckerDocumentTag: Int](./spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [func toggleContinuousSpellChecking(Any?)](./togglecontinuousspellchecking%28_%29.md)
  Toggles whether continuous spell checking is enabled for the receiver.
- [func toggleGrammarChecking(Any?)](./togglegrammarchecking%28_%29.md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](./setspellingstate%28_,range%29.md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/isgrammarcheckingenabled)*