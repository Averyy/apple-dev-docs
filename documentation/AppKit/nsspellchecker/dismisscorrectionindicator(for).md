# dismissCorrectionIndicator(for:)

**Framework**: AppKit  
**Kind**: method

Dismisses the correction indicator for the specified view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func dismissCorrectionIndicator(for view: NSView)
```

## Parameters

- `view`: The view.

## See Also

- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](nsspellchecker/showcorrectionindicator(of:primarystring:alternativestrings:forstringin:view:completionhandler:).md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md)
  Records the user response to the correction indicator being displayed.
- [NSSpellChecker.CorrectionIndicatorType](nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/dismisscorrectionindicator(for:))*