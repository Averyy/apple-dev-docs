# checkSpelling(of:startingAt:)

**Framework**: AppKit  
**Kind**: method

Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.

**Availability**:
- macOS ?+

## Declaration

```swift
func checkSpelling(of stringToCheck: String, startingAt startingOffset: Int) -> NSRange
```

#### Return Value

Returns the range of the first misspelled word.

#### Discussion

Wrapping occurs, but no ignored-words dictionary is used.

## Parameters

- `stringToCheck`: The string to spell check.
- `startingOffset`: The offset at which to start checking.

## See Also

- [func countWords(in: String, language: String?) -> Int](nsspellchecker/countwords(in:language:).md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](nsspellchecker/checkspelling(of:startingat:language:wrap:inspelldocumentwithtag:wordcount:).md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](nsspellchecker/checkgrammar(of:startingat:language:wrap:inspelldocumentwithtag:details:).md)
  Initiates a grammatical analysis of a given string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:).md)
  Requests unified text checking for the given range of the given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:).md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/guesses(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns an array of possible substitutions for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/checkspelling(of:startingat:))*