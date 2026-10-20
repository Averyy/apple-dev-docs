# checkSpelling(of:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts the search for a misspelled word in a string starting at specified offset within the string.

**Availability**:
- macOS

## Declaration

```swift
func checkSpelling(of stringToCheck: String, startingAt startingOffset: Int, language: String?, wrap wrapFlag: Bool, inSpellDocumentWithTag tag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange
```

```objc
- (NSRange) checkSpellingOfString:(NSString *) stringToCheck startingAt:(NSInteger) startingOffset language:(NSString *) language wrap:(BOOL) wrapFlag inSpellDocumentWithTag:(NSInteger) tag wordCount:(NSInteger *) wordCount;
```

#### Return Value

The range of the first misspelled word and optionally (and by reference) the count of words spellchecked in the string in `wordCount`.

## Parameters

- `stringToCheck`: The string object containing the words to spellcheck.
- `startingOffset`: The offset within `stringToCheck` at which to begin spellchecking.
- `language`: The language of the words in the string. If `language` is `nil`, or if you obtain the value by sending [`language()`](./language%28%29.md) to `self`, the current selection in the Spelling panel’s pop-up menu is used. Do not pass in an empty string for `language`.
- `wrapFlag`: [`true`](../../Swift/true.md) to indicate that spell checking should continue at the beginning of the string when the end of the string is reached; [`false`](../../Swift/false.md) to indicate that spellchecking should stop at the end of the document.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.
- `wordCount`: Returns by indirection a count of the words spell-checked up to and including the first error (if any), or -1 if the spell checker fails or does not support word counting. Specify `NULL` if you do not want this word count.

## See Also

### Checking Strings for Spelling and Grammar
- [func countWords(in: String, language: String?) -> Int](./countwords%28in,language%29.md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](./checkspelling%28of,startingat%29.md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](./checkgrammar%28of,startingat,language,wrap,inspelldocumentwithtag,details%29.md)
  Initiates a grammatical analysis of a given string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](./check%28_,range,types,options,inspelldocumentwithtag,orthography,wordcount%29.md)
  Requests unified text checking for the given range of the given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](./requestchecking%28of,range,types,options,inspelldocumentwithtag,completionhandler%29.md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](./guesses%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns an array of possible substitutions for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/checkspelling(of:startingat:language:wrap:inspelldocumentwithtag:wordcount:))*