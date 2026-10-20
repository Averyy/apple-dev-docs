# dismissCorrectionIndicator(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the correction indicator for the specified view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func dismissCorrectionIndicator(for view: NSView)
```

```objc
- (void) dismissCorrectionIndicatorForView:(NSView *) view;
```

## Parameters

- `view`: The view.

## See Also

### Automatic Spelling Correction
- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](./correction%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](./showcorrectionindicator%28of,primarystring,alternativestrings,forstringin,view,completionhandler%29.md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md)
  Records the user response to the correction indicator being displayed.
- [NSSpellChecker.CorrectionIndicatorType](./correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](./correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/dismisscorrectionindicator(for:))*