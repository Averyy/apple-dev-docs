# deletesAutospaceBetweenString(_:andString:language:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func deletesAutospaceBetweenString(_ precedingString: String, andString followingString: String, language: String?) -> Bool
```

## See Also

- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](nsspellchecker/language(forwordrange:in:orthography:).md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](nsspellchecker/preventsautocorrection(before:language:).md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:).md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](nsspellchecker/showinlineprediction(forcandidates:client:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/deletesautospacebetweenstring(_:andstring:language:))*