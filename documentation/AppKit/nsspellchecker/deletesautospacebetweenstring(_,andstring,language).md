# deletesAutospaceBetweenString(_:andString:language:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func deletesAutospaceBetweenString(_ precedingString: String, andString followingString: String, language: String?) -> Bool
```

```objc
- (BOOL) deletesAutospaceBetweenString:(NSString *) precedingString andString:(NSString *) followingString language:(NSString *) language;
```

## See Also

### Instance Methods
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](./language%28forwordrange,in,orthography%29.md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](./preventsautocorrection%28before,language%29.md)
- [func requestCandidates(forSelectedRange: NSRange, in: String, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]?, inSpellDocumentWithTag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)?) -> Int](./requestcandidates%28forselectedrange,in,types,options,inspelldocumentwithtag,completionhandler%29.md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](./showinlineprediction%28forcandidates,client%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/deletesautospacebetweenstring(_:andstring:language:))*