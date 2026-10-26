# guesses(forWordRange:in:language:inSpellDocumentWithTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of possible substitutions for the specified string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func guesses(forWordRange range: NSRange, in string: String, language: String?, inSpellDocumentWithTag tag: Int) -> [String]?
```

```objc
- (NSArray<NSString *> *) guessesForWordRange:(NSRange) range inString:(NSString *) string language:(NSString *) language inSpellDocumentWithTag:(NSInteger) tag;
```

#### Return Value

An array of strings containing possible replacement words.

## Parameters

- `range`: The range of the string to check.
- `string`: The string to guess.
- `language`: The language of the string.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.

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
- [- guessesForWord:](./guessesforword_.md)
  Returns an array of suggested spellings for the misspelled word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/guesses(forwordrange:in:language:inspelldocumentwithtag:))*