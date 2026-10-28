# guessesForWord:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of suggested spellings for the misspelled word.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`guesses(forWordRange:in:language:inSpellDocumentWithTag:)`](./guesses%28forwordrange,in,language,inspelldocumentwithtag%29.md) instead.

## Declaration

```objc
- (NSArray *) guessesForWord:(NSString *) word;
```

## Return Value

An array of suggested spellings for the word.

## Discussion

If `word` contains all capital letters, or its first letter is capitalized, the suggested words are capitalized in the same way.

## Parameters

- `word`: A misspelled word.

## See Also

### Checking Strings for Spelling and Grammar
- [func countWords(in: String, language: String?) -> Int](./countwords%28in,language%29.md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](./checkspelling%28of,startingat%29.md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](./checkspelling%28of,startingat,language,wrap,inspelldocumentwithtag,wordcount%29.md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](./checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md)
  Initiates a grammatical analysis of a given string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](./check%28_,range,types,options,inspelldocumentwithtag,orthography,wordcount%29.md)
  Requests unified text checking for the given range of the given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](./requestchecking%28of,range,types,options,inspelldocumentwithtag,completionhandler%29.md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](./guesses%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns an array of possible substitutions for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/guessesforword:)*