# requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Requests that the string be checked in the background.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func requestChecking(of stringToCheck: String, range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]? = nil, inSpellDocumentWithTag tag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)? = nil) -> Int
```

#### Return Value

The return value is a monotonically increasing sequence number that can be used to keep track of requests in flight.

## Parameters

- `stringToCheck`: The string to check.
- `range`: The range of the string to check.
- `checkingTypes`: The type of checking to be performed. The possible constants are listed in [`NSTextCheckingResult.CheckingType`](https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype) and can be combined using the C bit-wise `OR` operator to perform multiple checks at the same time.
- `options`: The options dictionary specifying the types of checking to perform. See [`NSSpellChecker.OptionKey`](nsspellchecker/optionkey.md) for the possible keys and expected values.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.
- `completionHandler`: The completion handler block object will be called (in an arbitrary context) when results are available, with the sequence number and results. The block takes four arguments: - **sequenceNumber**: A monotonically increasing sequence number.
- **results**: An array of [`NSTextCheckingResult`](https://developer.apple.com/documentation/foundation/nstextcheckingresult) objects describing particular items found during checking and their individual ranges, sorted by range origin, then range end, then result type.
- **orthography**: The orthography of the string.
- **wordCount**: The number of words in the range of the string.

## See Also

- [func countWords(in: String, language: String?) -> Int](nsspellchecker/countwords(in:language:).md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](nsspellchecker/checkspelling(of:startingat:).md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](nsspellchecker/checkspelling(of:startingat:language:wrap:inspelldocumentwithtag:wordcount:).md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func checkGrammar(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange](nsspellchecker/checkgrammar(of:startingat:language:wrap:inspelldocumentwithtag:details:).md)
  Initiates a grammatical analysis of a given string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:).md)
  Requests unified text checking for the given range of the given string.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](nsspellchecker/guesses(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns an array of possible substitutions for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:))*