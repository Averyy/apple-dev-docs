# checkTextInSelection(_:)

**Framework**: AppKit  
**Kind**: method

Performs the default text checking on the current selection.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func checkTextInSelection(_ sender: Any?)
```

#### Discussion

Immediately performs the text checking and replaces the selection with the checked content.

The checks performed are specified by [`enabledTextCheckingTypes`](nstextview/enabledtextcheckingtypes.md);

## Parameters

- `sender`: The control sending the message. May be  .

## See Also

- [func checkTextInDocument(Any?)](nstextview/checktextindocument(_:).md)
  Performs the default text checking on the entire document.
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](nstextview/checktext(in:types:options:).md)
  Check and replace the text in the range using the specified checking types and options.
- [func handleTextCheckingResults([NSTextCheckingResult], forRange: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], orthography: NSOrthography, wordCount: Int)](nstextview/handletextcheckingresults(_:forrange:types:options:orthography:wordcount:).md)
  Handles the text checking results returned by the text view
- [var enabledTextCheckingTypes: NSTextCheckingTypes](nstextview/enabledtextcheckingtypes.md)
  The default text checking types.
- [var isAutomaticDashSubstitutionEnabled: Bool](nstextview/isautomaticdashsubstitutionenabled.md)
  A Boolean value that indicates whether automatic dash substitution is enabled.
- [func toggleAutomaticDashSubstitution(Any?)](nstextview/toggleautomaticdashsubstitution(_:).md)
  Toggles the state of the automatic dash substitution.
- [var isAutomaticDataDetectionEnabled: Bool](nstextview/isautomaticdatadetectionenabled.md)
  A Boolean value that indicates whether automatic data detection is enabled.
- [func toggleAutomaticDataDetection(Any?)](nstextview/toggleautomaticdatadetection(_:).md)
  Toggles the state of the automatic data detection.
- [var isAutomaticSpellingCorrectionEnabled: Bool](nstextview/isautomaticspellingcorrectionenabled.md)
  A Boolean value that indicates whether automatic spelling correction is enabled.
- [func toggleAutomaticSpellingCorrection(Any?)](nstextview/toggleautomaticspellingcorrection(_:).md)
  Toggles the state of the automatic spelling correction.
- [var isAutomaticTextReplacementEnabled: Bool](nstextview/isautomatictextreplacementenabled.md)
  A Boolean value that indicates whether automatic text replacement is enabled.
- [func toggleAutomaticTextReplacement(Any?)](nstextview/toggleautomatictextreplacement(_:).md)
  Toggles the state of the automatic text replacement.
- [func performValidatedReplacement(in: NSRange, with: NSAttributedString) -> Bool](nstextview/performvalidatedreplacement(in:with:).md)
  Replaces text in the range you specify with the attributed string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/checktextinselection(_:))*