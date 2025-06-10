# record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)

**Framework**: AppKit  
**Kind**: method

Records the user response to the correction indicator being displayed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func record(_ response: NSSpellChecker.CorrectionResponse, toCorrection correction: String, forWord word: String, language: String?, inSpellDocumentWithTag tag: Int)
```

#### Discussion

When a correction is automatically proposed, the user may respond in one of several ways.  Clients may report this to the spell checker so that it can learn from the user’s response and adjust future correction behavior accordingly.

> **Note**:  Use of this method implies that the client stored the original word and original correction at least from the point at which the user accepts it until the user edits or reverts it.

## Parameters

- `response`: The user’s response. The possible values are shown in  .
- `correction`: The corrected word.  This should match the original correction.
- `word`: The original word.  This should match the original correction.
- `language`: The language being edited. This should match the original correction.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.

## See Also

- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](nsspellchecker/showcorrectionindicator(of:primarystring:alternativestrings:forstringin:view:completionhandler:).md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func dismissCorrectionIndicator(for: NSView)](nsspellchecker/dismisscorrectionindicator(for:).md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:))*