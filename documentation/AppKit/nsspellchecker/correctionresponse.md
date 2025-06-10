# NSSpellChecker.CorrectionResponse

**Framework**: AppKit  
**Kind**: enum

The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](nsspellchecker/record(_:tocorrection:forword:language:inspelldocumentwithtag:).md) method.

**Availability**:
- macOS ?+

## Declaration

```swift
enum CorrectionResponse
```

## Topics

### Enumeration Cases
- [NSSpellChecker.CorrectionResponse.accepted](nsspellchecker/correctionresponse/accepted.md)
  The user accepted the correction.
- [NSSpellChecker.CorrectionResponse.edited](nsspellchecker/correctionresponse/edited.md)
  After the correction was accepted, the user edited the corrected word (to something other than its original form.
- [NSSpellChecker.CorrectionResponse.ignored](nsspellchecker/correctionresponse/ignored.md)
  The user continued in such a way as to ignore the correction.
- [NSSpellChecker.CorrectionResponse.none](nsspellchecker/correctionresponse/none.md)
  No response was received from the user.
- [NSSpellChecker.CorrectionResponse.rejected](nsspellchecker/correctionresponse/rejected.md)
  The user rejected the correction by dismissing the correction indicator.
- [NSSpellChecker.CorrectionResponse.reverted](nsspellchecker/correctionresponse/reverted.md)
  After the correction was accepted, the user reverted the correction back to the original word.
### Initializers
- [init?(rawValue: Int)](nsspellchecker/correctionresponse/init(rawvalue:).md)

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
- [NSSpellChecker.CorrectionIndicatorType](nsspellchecker/correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionresponse)*