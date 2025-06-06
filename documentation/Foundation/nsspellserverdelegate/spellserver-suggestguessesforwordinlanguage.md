# spellServer(_:suggestGuessesForWord:inLanguage:)

**Framework**: Foundation  
**Kind**: method

Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, suggestGuessesForWord word: String, inLanguage language: String) -> [String]?
```

#### Return Value

An array of `NSString` objects indicating possible correct spellings.

## Parameters

- `sender`: The   object that sent this message.
- `word`: The misspelled word.
- `language`: The language to use for the guesses.

## See Also

- [func spellServer(NSSpellServer, check: String, offset: Int, types: NSTextCheckingTypes, options: [String : Any]?, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?](nsspellserverdelegate/spellserver(_:check:offset:types:options:orthography:wordcount:).md)
  Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [func spellServer(NSSpellServer, checkGrammarIn: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](nsspellserverdelegate/spellserver(_:checkgrammarin:language:details:).md)
  Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [func spellServer(NSSpellServer, findMisspelledWordIn: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange](nsspellserverdelegate/spellserver(_:findmisspelledwordin:language:wordcount:countonly:).md)
  Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestguessesforword:inlanguage:))*