# NSSpellChecker.CorrectionIndicatorType

**Framework**: AppKit  
**Kind**: enum

Constants that allow an app to specify the correction indicator type displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
enum CorrectionIndicatorType
```

## Topics

### Constants
- [NSSpellChecker.CorrectionIndicatorType.default](nsspellchecker/correctionindicatortype/default.md)
  The default indicator that shows a proposed correction.
- [NSSpellChecker.CorrectionIndicatorType.reversion](nsspellchecker/correctionindicatortype/reversion.md)
  Provides the option to revert to the original form after a correction has been made.
- [NSSpellChecker.CorrectionIndicatorType.guesses](nsspellchecker/correctionindicatortype/guesses.md)
  Shows multiple alternatives from which the user may choose the appropriate spelling.
### Initializers
- [init?(rawValue: Int)](nsspellchecker/correctionindicatortype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](nsspellchecker/correction(forwordrange:in:language:inspelldocumentwithtag:).md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](nsspellchecker/showcorrectionindicator(of:primarystring:alternativestrings:forstringin:view:completionhandler:).md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](nsspellchecker/dismisscorrectionindicator(for:).md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionResponse](nsspellchecker/correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionindicatortype)*