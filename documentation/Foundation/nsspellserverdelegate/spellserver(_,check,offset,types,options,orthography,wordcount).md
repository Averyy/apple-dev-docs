# spellServer(_:check:offset:types:options:orthography:wordCount:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func spellServer(_ sender: NSSpellServer, check stringToCheck: String, offset: Int, types checkingTypes: NSTextCheckingTypes, options: [String : Any]? = nil, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?
```

```objc
- (NSArray<NSTextCheckingResult *> *) spellServer:(NSSpellServer *) sender checkString:(NSString *) stringToCheck offset:(NSUInteger) offset types:(NSTextCheckingTypes) checkingTypes options:(NSDictionary<NSString *,id> *) options orthography:(NSOrthography *) orthography wordCount:(NSInteger *) wordCount;
```

#### Return Value

An array of NSTextCheckingResult instances of the spelling, grammar, or correction types, depending on the `checkingTypes` requested.

#### Discussion

This method is optional, but if implemented it will be called during the course of unified text checking via the `NSSpellChecker` [`checkSpelling(of:startingAt:)`](../../AppKit/nsspellchecker/checkspelling%28of,startingat%29.md) and [`requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)`](../../AppKit/nsspellchecker/requestchecking%28of,range,types,options,inspelldocumentwithtag,completionhandler%29.md) methods.  This allows spelling and grammar checking to be performed simultaneously, which can be significantly more efficient, and allows the delegate to return autocorrection results as well.

If this method is not implemented, then unified text checking will call the separate spelling and grammar checking methods instead.

This method may be called repeatedly with strings representing different subranges of the string that was originally requested to be checked; the offset argument represents the offset of the portion passed in to this method within that original string, and should be added to the origin of the range in any [`NSTextCheckingResult`](../nstextcheckingresult.md) returned.

## Parameters

- `sender`: Spell server making the analysis request.
- `stringToCheck`: String to analyze.
- `offset`: The offset in the string.
- `checkingTypes`: The text checking types to perform.
- `options`: A dictionary defining the actions to be taken while checking this string. See Constants in [`NSSpellChecker`](../../AppKit/nsspellchecker.md) for the possible keys.
- `orthography`: The identified orthography of `stringToCheck`. See [`NSOrthography`](../nsorthography.md) for more information.
- `wordCount`: On output, returns by-reference the number of words from the beginning of the string object until the misspelled word (or the end of string).

## See Also

### Related Documentation
- [Spell Checking Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/SpellCheck.html#//apple_ref/doc/uid/10000092i)
### Check Grammar and Spelling in Strings
- [func spellServer(NSSpellServer, suggestGuessesForWord: String, inLanguage: String) -> [String]?](./spellserver%28_,suggestguessesforword,inlanguage%29.md)
  Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [func spellServer(NSSpellServer, checkGrammarIn: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](./spellserver%28_,checkgrammarin,language,details%29.md)
  Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [func spellServer(NSSpellServer, findMisspelledWordIn: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange](./spellserver%28_,findmisspelledwordin,language,wordcount,countonly%29.md)
  Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:check:offset:types:options:orthography:wordcount:))*