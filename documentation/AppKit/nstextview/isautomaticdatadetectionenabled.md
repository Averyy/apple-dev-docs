# isAutomaticDataDetectionEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether automatic data detection is enabled.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isAutomaticDataDetectionEnabled: Bool { get set }
```

```objc
@property (getter=isAutomaticDataDetectionEnabled) BOOL automaticDataDetectionEnabled;
```

#### Discussion

Automatic data detection enables detection of dates, addresses, and phone numbers.

## See Also

### Checking and substituting text
- [func checkTextInDocument(Any?)](./checktextindocument%28_%29.md)
  Performs the default text checking on the entire document.
- [func checkTextInSelection(Any?)](./checktextinselection%28_%29.md)
  Performs the default text checking on the current selection.
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](./checktext%28in,types,options%29.md)
  Check and replace the text in the range using the specified checking types and options.
- [func handleTextCheckingResults([NSTextCheckingResult], forRange: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], orthography: NSOrthography, wordCount: Int)](./handletextcheckingresults%28_,forrange,types,options,orthography,wordcount%29.md)
  Handles the text checking results returned by the text view
- [var enabledTextCheckingTypes: NSTextCheckingTypes](./enabledtextcheckingtypes.md)
  The default text checking types.
- [var isAutomaticDashSubstitutionEnabled: Bool](./isautomaticdashsubstitutionenabled.md)
  A Boolean value that indicates whether automatic dash substitution is enabled.
- [func toggleAutomaticDashSubstitution(Any?)](./toggleautomaticdashsubstitution%28_%29.md)
  Toggles the state of the automatic dash substitution.
- [func toggleAutomaticDataDetection(Any?)](./toggleautomaticdatadetection%28_%29.md)
  Toggles the state of the automatic data detection.
- [var isAutomaticSpellingCorrectionEnabled: Bool](./isautomaticspellingcorrectionenabled.md)
  A Boolean value that indicates whether automatic spelling correction is enabled.
- [func toggleAutomaticSpellingCorrection(Any?)](./toggleautomaticspellingcorrection%28_%29.md)
  Toggles the state of the automatic spelling correction.
- [var isAutomaticTextReplacementEnabled: Bool](./isautomatictextreplacementenabled.md)
  A Boolean value that indicates whether automatic text replacement is enabled.
- [func toggleAutomaticTextReplacement(Any?)](./toggleautomatictextreplacement%28_%29.md)
  Toggles the state of the automatic text replacement.
- [func performValidatedReplacement(in: NSRange, with: NSAttributedString) -> Bool](./performvalidatedreplacement%28in,with%29.md)
  Replaces text in the range you specify with the attributed string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/isautomaticdatadetectionenabled)*