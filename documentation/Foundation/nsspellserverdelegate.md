# NSSpellServerDelegate

**Framework**: Foundation  
**Kind**: protocol

The optional methods implemented by the delegate of a spell server.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
protocol NSSpellServerDelegate : NSObjectProtocol
```

## Topics

### Check Grammar and Spelling in Strings
- [func spellServer(NSSpellServer, check: String, offset: Int, types: NSTextCheckingTypes, options: [String : Any]?, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?](nsspellserverdelegate/spellserver(_:check:offset:types:options:orthography:wordcount:).md)
  Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [func spellServer(NSSpellServer, suggestGuessesForWord: String, inLanguage: String) -> [String]?](nsspellserverdelegate/spellserver(_:suggestguessesforword:inlanguage:).md)
  Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [func spellServer(NSSpellServer, checkGrammarIn: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](nsspellserverdelegate/spellserver(_:checkgrammarin:language:details:).md)
  Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [func spellServer(NSSpellServer, findMisspelledWordIn: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange](nsspellserverdelegate/spellserver(_:findmisspelledwordin:language:wordcount:countonly:).md)
  Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.
### Managing the Spelling Dictionary
- [func spellServer(NSSpellServer, didForgetWord: String, inLanguage: String)](nsspellserverdelegate/spellserver(_:didforgetword:inlanguage:).md)
  Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [func spellServer(NSSpellServer, didLearnWord: String, inLanguage: String)](nsspellserverdelegate/spellserver(_:didlearnword:inlanguage:).md)
  Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [func spellServer(NSSpellServer, suggestCompletionsForPartialWordRange: NSRange, in: String, language: String) -> [String]?](nsspellserverdelegate/spellserver(_:suggestcompletionsforpartialwordrange:in:language:).md)
  This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.
- [func spellServer(NSSpellServer, recordResponse: Int, toCorrection: String, forWord: String, language: String)](nsspellserverdelegate/spellserver(_:recordresponse:tocorrection:forword:language:).md)
  Notifies the spell checker of the users’s response to a correction.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSpellServer](nsspellserver.md)
  A server that your app uses to provide a spell checker service to other apps running in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate)*