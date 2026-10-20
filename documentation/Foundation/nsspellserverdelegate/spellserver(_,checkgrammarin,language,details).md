# spellServer(_:checkGrammarIn:language:details:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Gives the delegate the opportunity to customize the grammatical analysis of a given string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, checkGrammarIn stringToCheck: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange
```

```objc
- (NSRange) spellServer:(NSSpellServer *) sender checkGrammarInString:(NSString *) stringToCheck language:(NSString *) language details:(NSArray<NSDictionary<NSString *,id> *> **) details;
```

#### Return Value

Location of the first flagged grammatical unit within `string`.

## Parameters

- `sender`: Spell server satisfying a grammatical analysis request.
- `stringToCheck`: String to analyze.
- `language`: Language use in `string`. When `nil`, the language selected in the Spelling panel is used.
- `details`: On output, dictionaries describing grammar-analysis details within the flagged grammatical unit. See the [`NSSpellServer`](../nsspellserver.md) class for information about these dictionaries.

## See Also

### Check Grammar and Spelling in Strings
- [func spellServer(NSSpellServer, check: String, offset: Int, types: NSTextCheckingTypes, options: [String : Any]?, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?](./spellserver%28_,check,offset,types,options,orthography,wordcount%29.md)
  Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [func spellServer(NSSpellServer, suggestGuessesForWord: String, inLanguage: String) -> [String]?](./spellserver%28_,suggestguessesforword,inlanguage%29.md)
  Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [func spellServer(NSSpellServer, findMisspelledWordIn: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange](./spellserver%28_,findmisspelledwordin,language,wordcount,countonly%29.md)
  Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:checkgrammarin:language:details:))*