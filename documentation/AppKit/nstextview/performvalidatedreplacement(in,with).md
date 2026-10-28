# performValidatedReplacement(in:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces text in the range you specify with the attributed string you provide.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func performValidatedReplacement(in range: NSRange, with attributedString: NSAttributedString) -> Bool
```

```objc
- (BOOL) performValidatedReplacementInRange:(NSRange) range withAttributedString:(NSAttributedString *) attributedString;
```

## Return Value

Retuns `true` if the replacement was successful, `false` otherwise.

## Parameters

- `range`: The range of the replacement.
- `attributedString`: The attributed string to use as the replacement text.

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
- [var isAutomaticDataDetectionEnabled: Bool](./isautomaticdatadetectionenabled.md)
  A Boolean value that indicates whether automatic data detection is enabled.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/performvalidatedreplacement(in:with:))*