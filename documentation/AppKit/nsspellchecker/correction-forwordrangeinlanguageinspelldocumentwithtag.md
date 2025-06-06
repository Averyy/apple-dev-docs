# correction(forWordRange:in:language:inSpellDocumentWithTag:)

**Framework**: AppKit  
**Kind**: method

Returns a single proposed correction if a word is mis-spelled.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func correction(forWordRange range: NSRange, in string: String, language: String, inSpellDocumentWithTag tag: Int) -> String?
```

#### Return Value

The proposed correct string.

#### Discussion

While correction functionality is available starting in OS X v10.6 as part of unified text checking, for convenience this method makes it available separately starting in OS X v10.7.

## Parameters

- `range`: The range of the word to be corrected.
- `string`: The string containing the proposed correction.
- `language`: The language.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.

## See Also

- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](nsspellchecker/showcorrectionindicator(of:primarystring:alternativestrings:forstringin:view:completionhandler:).md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](nsspellchecker/dismisscorrectionindicator(for:).md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:))*