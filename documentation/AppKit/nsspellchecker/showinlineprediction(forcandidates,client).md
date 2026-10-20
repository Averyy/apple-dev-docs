# showInlinePrediction(forCandidates:client:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func showInlinePrediction(forCandidates candidates: [NSTextCheckingResult], client: any NSTextInputClient)
```

```objc
- (void) showInlinePredictionForCandidates:(NSArray<NSTextCheckingResult *> *) candidates client:(id<NSTextInputClient>) client;
```

## See Also

### Instance Methods
- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](./deletesautospacebetweenstring%28_,andstring,language%29.md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](./language%28forwordrange,in,orthography%29.md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](./preventsautocorrection%28before,language%29.md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](./requestcandidates%28forselectedrange,in,types,options,inspelldocumentwithtag,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/showinlineprediction(forcandidates:client:))*