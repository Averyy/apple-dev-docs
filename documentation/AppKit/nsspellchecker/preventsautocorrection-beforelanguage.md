# preventsAutocorrection(before:language:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.12+

## Declaration

```swift
func preventsAutocorrection(before string: String, language: String?) -> Bool
```

## See Also

- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](nsspellchecker/deletesautospacebetweenstring(_:andstring:language:).md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](nsspellchecker/language(forwordrange:in:orthography:).md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:).md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](nsspellchecker/showinlineprediction(forcandidates:client:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/preventsautocorrection(before:language:))*