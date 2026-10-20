# NSSpellChecker.CorrectionIndicatorType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that allow an app to specify the correction indicator type displayed.

**Availability**:
- macOS

## Declaration

```swift
enum CorrectionIndicatorType
```

```c
enum NSCorrectionIndicatorType : NSInteger;
```

## Topics

### Constants
- [NSSpellChecker.CorrectionIndicatorType.default](./correctionindicatortype/default.md)
  The default indicator that shows a proposed correction.
- [NSSpellChecker.CorrectionIndicatorType.reversion](./correctionindicatortype/reversion.md)
  Provides the option to revert to the original form after a correction has been made.
- [NSSpellChecker.CorrectionIndicatorType.guesses](./correctionindicatortype/guesses.md)
  Shows multiple alternatives from which the user may choose the appropriate spelling.
### Initializers
- [init?(rawValue: Int)](./correctionindicatortype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Automatic Spelling Correction
- [func correction(forWordRange: NSRange, in: String, language: String, inSpellDocumentWithTag: Int) -> String?](./correction%28forwordrange,in,language,inspelldocumentwithtag%29.md)
  Returns a single proposed correction if a word is mis-spelled.
- [func showCorrectionIndicator(of: NSSpellChecker.CorrectionIndicatorType, primaryString: String, alternativeStrings: [String], forStringIn: NSRect, view: NSView, completionHandler: ((String?) -> Void)?)](./showcorrectionindicator%28of,primarystring,alternativestrings,forstringin,view,completionhandler%29.md)
  Display a suitable user interface to indicate a correction may need to be made.
- [func record(NSSpellChecker.CorrectionResponse, toCorrection: String, forWord: String, language: String?, inSpellDocumentWithTag: Int)](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md)
  Records the user response to the correction indicator being displayed.
- [func dismissCorrectionIndicator(for: NSView)](./dismisscorrectionindicator%28for%29.md)
  Dismisses the correction indicator for the specified view.
- [NSSpellChecker.CorrectionResponse](./correctionresponse.md)
  The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionindicatortype)*