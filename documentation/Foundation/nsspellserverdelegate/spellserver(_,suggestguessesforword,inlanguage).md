# spellServer(_:suggestGuessesForWord:inLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, suggestGuessesForWord word: String, inLanguage language: String) -> [String]?
```

```objc
- (NSArray<NSString *> *) spellServer:(NSSpellServer *) sender suggestGuessesForWord:(NSString *) word inLanguage:(NSString *) language;
```

## Return Value

An array of `NSString` objects indicating possible correct spellings.

## Parameters

- `sender`: The `NSSpellServer` object that sent this message.
- `word`: The misspelled word.
- `language`: The language to use for the guesses.

## See Also

### Check Grammar and Spelling in Strings
- [func spellServer(NSSpellServer, check: String, offset: Int, types: NSTextCheckingTypes, options: [String : Any]?, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?](./spellserver%28_,check,offset,types,options,orthography,wordcount%29.md)
  Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [func spellServer(NSSpellServer, checkGrammarIn: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](./spellserver%28_,checkgrammarin,language,details%29.md)
  Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [func spellServer(NSSpellServer, findMisspelledWordIn: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange](./spellserver%28_,findmisspelledwordin,language,wordcount,countonly%29.md)
  Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestguessesforword:inlanguage:))*