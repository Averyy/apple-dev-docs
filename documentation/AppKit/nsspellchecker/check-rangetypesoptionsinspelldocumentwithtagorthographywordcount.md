# check(_:range:types:options:inSpellDocumentWithTag:orthography:wordCount:)

**Framework**: AppKit  
**Kind**: method

Requests unified text checking for the given range of the given string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func check(_ stringToCheck: String, range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]? = nil, inSpellDocumentWithTag tag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]
```

#### Return Value

An array of [`NSTextCheckingResult`](https://developer.apple.com/documentation/Foundation/NSTextCheckingResult) objects describing particular items found during checking and their individual ranges, sorted by range origin, then range end, then result type.

## Parameters

- `stringToCheck`: The string to check.
- `range`: The range of the string to check.
- `checkingTypes`: The type of checking to be performed. The possible constants are listed in   and can be combined using the C bit-wise   operator to perform multiple checks at the same time.
- `options`: The options dictionary specifying the types of checking to perform. See   for the possible keys and expected values.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.
- `orthography`: Returns by-reference, the orthography of the range of the string. See   for more information.
- `wordCount`: Returns by-reference, the word count for the range of the string.

## See Also

- [func countWords(in: String, language: String?) -> Int](nsspellchecker/countwords(in:language:).md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](nsspellchecker/checkspelling(of:startingat:).md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](nsspellchecker/checkspelling(of:startingat:language:wrap:inspelldocumentwithtag:wordcount:).md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](nsspellchecker/checkgrammar(of:startingat:language:wrap:inspelldocumentwithtag:details:).md)
  Initiates a grammatical analysis of a given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:).md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/guesses(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns an array of possible substitutions for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:))*