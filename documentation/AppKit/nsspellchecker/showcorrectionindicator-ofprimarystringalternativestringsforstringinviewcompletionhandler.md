# showCorrectionIndicator(of:primaryString:alternativeStrings:forStringIn:view:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Display a suitable user interface to indicate a correction may need to be made.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func showCorrectionIndicator(of type: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn rectOfTypedString: NSRect, view: NSView) async -> String?
```

#### Discussion

Only one indicator at a time may be displayed for a given view, and the only thing a client may do with the indicator after displaying it is to dismiss it using the [`dismissCorrectionIndicator(for:)`](nsspellchecker/dismisscorrectionindicator(for:).md) method.

> **Note**:  In order to record responses properly (for use with the [`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method), clients must store the original word and original correction at least from the point at which the user accepts it until the user edits or reverts it.

## Parameters

- `type`: The correction type to display. See   for possible values.
- `primaryString`: The first string to be displayed, a correction or reversion according to the   of indicator.
- `alternativeStrings`: An array of alternative strings to insert. This array may be empty.
- `rectOfTypedString`: The rectangle of the typed text.
- `view`: The view in which the correction indicator is to be displayed.
- `completionBlock`: The Block takes one argument:

## See Also

- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns a single proposed correction if a word is mis-spelled.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](nsspellchecker/dismisscorrectionindicator(for:).md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionIndicatorType](nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.
- [NSSpellChecker.CorrectionResponse](nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/showcorrectionindicator(of:primarystring:alternativestrings:forstringin:view:completionhandler:))*