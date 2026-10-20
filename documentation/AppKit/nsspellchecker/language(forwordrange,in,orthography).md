# language(forWordRange:in:orthography:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.7+

## Declaration

```swift
func language(forWordRange range: NSRange, in string: String, orthography: NSOrthography?) -> String?
```

```objc
- (NSString *) languageForWordRange:(NSRange) range inString:(NSString *) string orthography:(NSOrthography *) orthography;
```

## See Also

### Instance Methods
- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](./deletesautospacebetweenstring%28_,andstring,language%29.md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](./preventsautocorrection%28before,language%29.md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](./requestcandidates%28forselectedrange,in,types,options,inspelldocumentwithtag,completionhandler%29.md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](./showinlineprediction%28forcandidates,client%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/language(forwordrange:in:orthography:))*