# language(forWordRange:in:orthography:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.7+

## Declaration

```swift
func language(forWordRange range: NSRange, in string: String, orthography: NSOrthography?) -> String?
```

## See Also

- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](nsspellchecker/deletesautospacebetweenstring(_:andstring:language:).md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](nsspellchecker/preventsautocorrection(before:language:).md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:).md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](nsspellchecker/showinlineprediction(forcandidates:client:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/language(forwordrange:in:orthography:))*