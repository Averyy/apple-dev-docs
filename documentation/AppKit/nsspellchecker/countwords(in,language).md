# countWords(in:language:)

**Framework**: AppKit  
**Kind**: method

Returns the number of words in the specified string.

**Availability**:
- macOS ?+

## Declaration

```swift
func countWords(in stringToCount: String, language: String?) -> Int
```

#### Return Value

The number of words in the string or `-1` if word counting is unavailable or has not occurred for some reason.

#### Discussion

If `language` is `nil`, the current selection in the Spelling panel’s pop-up menu is used.

## Parameters

- `stringToCount`: The string to count the words in.
- `language`: The language of the string.

## See Also

- [func checkSpelling(of: String, startingAt: Int) -> NSRange](nsspellchecker/checkspelling(of:startingat:).md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/countwords(in:language:))*