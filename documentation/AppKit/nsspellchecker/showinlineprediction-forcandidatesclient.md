# showInlinePrediction(forCandidates:client:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func showInlinePrediction(forCandidates candidates: [NSTextCheckingResult], client: any NSTextInputClient)
```

## See Also

- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](nsspellchecker/deletesautospacebetweenstring(_:andstring:language:).md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](nsspellchecker/language(forwordrange:in:orthography:).md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](nsspellchecker/preventsautocorrection(before:language:).md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/showinlineprediction(forcandidates:client:))*