# NSSpellChecker.CorrectionResponse

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The correction response passed to the[`record(_:toCorrection:forWord:language:inSpellDocumentWithTag:)`](./record%28_,tocorrection,forword,language,inspelldocumentwithtag%29.md) method.

**Availability**:
- macOS

## Declaration

```swift
enum CorrectionResponse
```

```c
enum NSCorrectionResponse : NSInteger;
```

## Topics

### Enumeration Cases
- [NSSpellChecker.CorrectionResponse.accepted](./correctionresponse/accepted.md)
  The user accepted the correction.
- [NSSpellChecker.CorrectionResponse.edited](./correctionresponse/edited.md)
  After the correction was accepted, the user edited the corrected word (to something other than its original form.
- [NSSpellChecker.CorrectionResponse.ignored](./correctionresponse/ignored.md)
  The user continued in such a way as to ignore the correction.
- [NSSpellChecker.CorrectionResponse.none](./correctionresponse/none.md)
  No response was received from the user.
- [NSSpellChecker.CorrectionResponse.rejected](./correctionresponse/rejected.md)
  The user rejected the correction by dismissing the correction indicator.
- [NSSpellChecker.CorrectionResponse.reverted](./correctionresponse/reverted.md)
  After the correction was accepted, the user reverted the correction back to the original word.
### Initializers
- [init?(rawValue: Int)](./correctionresponse/init%28rawvalue%29.md)

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
- [NSSpellChecker.CorrectionIndicatorType](./correctionindicatortype.md)
  Constants that allow an app to specify the correction indicator type displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/correctionresponse)*