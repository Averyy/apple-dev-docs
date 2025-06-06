# requestCandidates(forSelectedRange:in:types:options:inSpellDocumentWithTag:completionHandler:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func requestCandidates(forSelectedRange selectedRange: NSRange, in stringToCheck: String, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]? = nil, inSpellDocumentWithTag tag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)? = nil) -> Int
```

## See Also

- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](nsspellchecker/deletesautospacebetweenstring(_:andstring:language:).md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](nsspellchecker/language(forwordrange:in:orthography:).md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](nsspellchecker/preventsautocorrection(before:language:).md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](nsspellchecker/showinlineprediction(forcandidates:client:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:))*