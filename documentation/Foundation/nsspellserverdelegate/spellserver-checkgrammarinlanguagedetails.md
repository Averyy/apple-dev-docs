# spellServer(_:checkGrammarIn:language:details:)

**Framework**: Foundation  
**Kind**: method

Gives the delegate the opportunity to customize the grammatical analysis of a given string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, checkGrammarIn stringToCheck: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange
```

#### Return Value

Location of the first flagged grammatical unit within `string`.

## Parameters

- `sender`: Spell server satisfying a grammatical analysis request.
- `stringToCheck`: String to analyze.
- `language`: Language use in  . When  , the language selected in the Spelling panel is used.
- `details`: On output, dictionaries describing grammar-analysis details within the flagged grammatical unit. See the   class for information about these dictionaries.

## See Also

- [func spellServer(NSSpellServer, check: String, offset: Int, types: NSTextCheckingTypes, options: [String : Any]?, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?](nsspellserverdelegate/spellserver(_:check:offset:types:options:orthography:wordcount:).md)
  Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [func spellServer(NSSpellServer, suggestGuessesForWord: String, inLanguage: String) -> [String]?](nsspellserverdelegate/spellserver(_:suggestguessesforword:inlanguage:).md)
  Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [func spellServer(NSSpellServer, findMisspelledWordIn: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange](nsspellserverdelegate/spellserver(_:findmisspelledwordin:language:wordcount:countonly:).md)
  Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:checkgrammarin:language:details:))*