# preventsAutocorrection(before:language:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.12+

## Declaration

```swift
func preventsAutocorrection(before string: String, language: String?) -> Bool
```

```objc
- (BOOL) preventsAutocorrectionBeforeString:(NSString *) string language:(NSString *) language;
```

## See Also

### Instance Methods
- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](./deletesautospacebetweenstring%28_,andstring,language%29.md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](./language%28forwordrange,in,orthography%29.md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](./requestcandidates%28forselectedrange,in,types,options,inspelldocumentwithtag,completionhandler%29.md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](./showinlineprediction%28forcandidates,client%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/preventsautocorrection(before:language:))*