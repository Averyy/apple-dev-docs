# toggleContinuousSpellChecking(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Toggles whether continuous spell checking is enabled for the receiver.

**Availability**:
- macOS

## Declaration

```swift
func toggleContinuousSpellChecking(_ sender: Any?)
```

```objc
- (void) toggleContinuousSpellChecking:(id) sender;
```

## Parameters

- `sender`: The control sending the message; may be `nil`.

## See Also

### Working with the spelling checker
- [var isContinuousSpellCheckingEnabled: Bool](./iscontinuousspellcheckingenabled.md)
  A Boolean value that indicates whether the receiver has continuous spell checking enabled.
- [var spellCheckerDocumentTag: Int](./spellcheckerdocumenttag.md)
  A tag identifying the text view’s text as a document for the spell checker server.
- [var isGrammarCheckingEnabled: Bool](./isgrammarcheckingenabled.md)
  Enables and disables grammar checking.
- [func toggleGrammarChecking(Any?)](./togglegrammarchecking%28_%29.md)
  Changes the state of grammar checking from enabled to disabled and vice versa.
- [func setSpellingState(Int, range: NSRange)](./setspellingstate%28_,range%29.md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/togglecontinuousspellchecking(_:))*