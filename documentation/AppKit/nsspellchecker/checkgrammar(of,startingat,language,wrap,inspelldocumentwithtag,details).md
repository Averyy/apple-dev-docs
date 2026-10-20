# checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a grammatical analysis of a given string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func checkGrammar(of stringToCheck: String, startingAt startingOffset: Int, language: String?, wrap wrapFlag: Bool, inSpellDocumentWithTag tag: Int, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange
```

```objc
- (NSRange) checkGrammarOfString:(NSString *) stringToCheck startingAt:(NSInteger) startingOffset language:(NSString *) language wrap:(BOOL) wrapFlag inSpellDocumentWithTag:(NSInteger) tag details:(NSArray<NSDictionary<NSString *,id> *> **) details;
```

#### Return Value

Location of the first flagged grammatical unit.

## Parameters

- `stringToCheck`: String to analyze.
- `startingOffset`: Location within `string` at which to start the analysis.
- `language`: Language use in `string`. When `nil`, the language selected in the Spelling panel is used.
- `wrapFlag`: [`true`](../../Swift/true.md) to specify that the analysis continue to the beginning of string when the end is reached.

  [`false`](../../Swift/false.md) to have the analysis stop at the end of string.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.
- `details`: On output, dictionaries describing grammar-analysis details within the flagged grammatical unit. See the [`NSSpellServer`](../../Foundation/nsspellserver.md) class for information about these dictionaries.

## See Also

### Checking Strings for Spelling and Grammar
- [func countWords(in: String, language: String?) -> Int](./countwords%28in,language%29.md)
  Returns the number of words in the specified string.
- [func checkSpelling(of: String, startingAt: Int) -> NSRange](./checkspelling%28of,startingat%29.md)
  Starts the search for a misspelled word in `stringToCheck` starting at `startingOffset` within the string object.
- [func checkSpelling(of: String, startingAt: Int, language: String?, wrap: Bool, inSpellDocumentWithTag: Int, wordCount: UnsafeMutablePointer<Int>?) -> NSRange](./checkspelling%28of,startingat,language,wrap,inspelldocumentwithtag,wordcount%29.md)
  Starts the search for a misspelled word in a string starting at specified offset within the string.
- [func check(String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, orthography: AutoreleasingUnsafeMutablePointer<NSOrthography?>?, wordCount: UnsafeMutablePointer<Int>?) -> [NSTextCheckingResult]](./check%28_,range,types,options,inspelldocumentwithtag,orthography,wordcount%29.md)
  Requests unified text checking for the given range of the given string.
- [func requestChecking(of: String, range: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult], NSOrthography, Int) -> Void)?) -> Int](./requestchecking%28of,range,types,options,inspelldocumentwithtag,completionhandler%29.md)
  Requests that the string be checked in the background.
- [func guesses(forWordRange: NSRange, in: String, language: String?, inSpellDocumentWithTag: Int) -> [String]?](./guesses%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns an array of possible substitutions for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/checkgrammar(of:startingat:language:wrap:inspelldocumentwithtag:details:))*