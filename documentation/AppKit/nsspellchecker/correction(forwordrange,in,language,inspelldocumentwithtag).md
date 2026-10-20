# correction(forWordRange:in:language:inSpellDocumentWithTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a single proposed correction if a word is mis-spelled.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func correction(forWordRange range: NSRange, in string: String, language: String, inSpellDocumentWithTag tag: Int) -> String?
```

```objc
- (NSString *) correctionForWordRange:(NSRange) range inString:(NSString *) string language:(NSString *) language inSpellDocumentWithTag:(NSInteger) tag;
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

### Automatic Spelling Correction
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](./showcorrectionindicator%28of,primarystring,alternativestrings,forstringin,view,completionhandler%29.md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](./dismisscorrectionindicator%28for%29.md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](./correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](./correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:))*