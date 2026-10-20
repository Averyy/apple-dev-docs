# record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Records the user response to the correction indicator being displayed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func record(_ response: NSSpellChecker.CorrectionResponse, toCorrection correction: String, forWord word: String, language: String?, inSpellDocumentWithTag tag: Int)
```

```objc
- (void) recordResponse:(NSCorrectionResponse) response toCorrection:(NSString *) correction forWord:(NSString *) word language:(NSString *) language inSpellDocumentWithTag:(NSInteger) tag;
```

#### Discussion

When a correction is automatically proposed, the user may respond in one of several ways.  Clients may report this to the spell checker so that it can learn from the user’s response and adjust future correction behavior accordingly.

> **Note**:  Use of this method implies that the client stored the original word and original correction at least from the point at which the user accepts it until the user edits or reverts it.

## Parameters

- `response`: The user’s response. The possible values are shown in [`NSSpellChecker.CorrectionResponse`](./correctionresponse.md).
- `correction`: The corrected word.  This should match the original correction.
- `word`: The original word.  This should match the original correction.
- `language`: The language being edited. This should match the original correction.
- `tag`: An identifier unique within the application used to inform the spell checker which document that text is associated, potentially for many purposes, not necessarily just for ignored words. A value of 0 can be passed in for text not associated with a particular document.

## See Also

### Automatic Spelling Correction
- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](./correction%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](./showcorrectionindicator%28of,primarystring,alternativestrings,forstringin,view,completionhandler%29.md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func dismissCorrectionIndicator(for: NSView)](./dismisscorrectionindicator%28for%29.md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](./correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](./correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:))*