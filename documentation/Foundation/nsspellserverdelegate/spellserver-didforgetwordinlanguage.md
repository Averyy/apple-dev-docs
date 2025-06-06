# spellServer(_:didForgetWord:inLanguage:)

**Framework**: Foundation  
**Kind**: method

Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, didForgetWord word: String, inLanguage language: String)
```

#### Discussion

If your delegate maintains a similar auxiliary word list, you may wish to edit the list accordingly.

## Parameters

- `sender`: The   object that removed the word.
- `word`: The word that was removed.
- `language`: The language of the removed word.

## See Also

- [func spellServer(NSSpellServer, didLearnWord: String, inLanguage: String)](nsspellserverdelegate/spellserver(_:didlearnword:inlanguage:).md)
  Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [func spellServer(NSSpellServer, suggestCompletionsForPartialWordRange: NSRange, in: String, language: String) -> [String]?](nsspellserverdelegate/spellserver(_:suggestcompletionsforpartialwordrange:in:language:).md)
  This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.
- [func spellServer(NSSpellServer, recordResponse: Int, toCorrection: String, forWord: String, language: String)](nsspellserverdelegate/spellserver(_:recordresponse:tocorrection:forword:language:).md)
  Notifies the spell checker of the users’s response to a correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:didforgetword:inlanguage:))*