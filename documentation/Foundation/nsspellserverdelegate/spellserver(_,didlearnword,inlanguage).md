# spellServer(_:didLearnWord:inLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, didLearnWord word: String, inLanguage language: String)
```

```objc
- (void) spellServer:(NSSpellServer *) sender didLearnWord:(NSString *) word inLanguage:(NSString *) language;
```

## Discussion

If your delegate maintains a similar auxiliary word list, you may wish to edit the list accordingly.

## Parameters

- `sender`: The `NSSpellServer` object that added the word.
- `word`: The word that was added.
- `language`: The language of the added word.

## See Also

### Managing the Spelling Dictionary
- [func spellServer(NSSpellServer, didForgetWord: String, inLanguage: String)](./spellserver%28_,didforgetword,inlanguage%29.md)
  Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [func spellServer(NSSpellServer, suggestCompletionsForPartialWordRange: NSRange, in: String, language: String) -> [String]?](./spellserver%28_,suggestcompletionsforpartialwordrange,in,language%29.md)
  This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.
- [func spellServer(NSSpellServer, recordResponse: Int, toCorrection: String, forWord: String, language: String)](./spellserver%28_,recordresponse,tocorrection,forword,language%29.md)
  Notifies the spell checker of the users’s response to a correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:didlearnword:inlanguage:))*