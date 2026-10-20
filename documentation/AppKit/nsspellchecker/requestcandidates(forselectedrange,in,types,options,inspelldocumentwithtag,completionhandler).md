# requestCandidates(forSelectedRange:in:types:options:inSpellDocumentWithTag:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func requestCandidates(forSelectedRange selectedRange: NSRange, in stringToCheck: String, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any]? = nil, inSpellDocumentWithTag tag: Int, completionHandler: ((Int, [NSTextCheckingResult]) -> Void)? = nil) -> Int
```

```objc
- (NSInteger) requestCandidatesForSelectedRange:(NSRange) selectedRange inString:(NSString *) stringToCheck types:(NSTextCheckingTypes) checkingTypes options:(NSDictionary<NSString *,id> *) options inSpellDocumentWithTag:(NSInteger) tag completionHandler:(void (^)(NSInteger sequenceNumber, NSArray<NSTextCheckingResult *> *candidates)) completionHandler;
```

## See Also

### Instance Methods
- [func deletesAutospaceBetweenString(String, andString: String, language: String?) -> Bool](./deletesautospacebetweenstring%28_,andstring,language%29.md)
- [func language(forWordRange: NSRange, in: String, orthography: NSOrthography?) -> String?](./language%28forwordrange,in,orthography%29.md)
- [func preventsAutocorrection(before: String, language: String?) -> Bool](./preventsautocorrection%28before,language%29.md)
- [func showInlinePrediction(forCandidates: [NSTextCheckingResult], client: any NSTextInputClient)](./showinlineprediction%28forcandidates,client%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/requestcandidates(forselectedrange:in:types:options:inspelldocumentwithtag:completionhandler:))*