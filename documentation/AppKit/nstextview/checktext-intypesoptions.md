# checkText(in:types:options:)

**Framework**: AppKit  
**Kind**: method

Check and replace the text in the range using the specified checking types and options.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func checkText(in range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any] = [:])
```

#### Discussion

This method calls the delegate method [`textView(_:willCheckTextIn:options:types:)`](nstextviewdelegate/textview(_:willchecktextin:options:types:).md) allowing you to modify the parameters before the checking occurs.

This method usually would not be called directly, since `NSTextView` itself will call it as needed, but it can be overridden.

## Parameters

- `range`: The range to check.
- `checkingTypes`: The type of checking to be performed, passed by-reference. The possible constants are listed in   and can be combined using the C bit-wise   operator to perform multiple checks at the same time.
- `options`: A dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.

## See Also

- [func checkTextInDocument(Any?)](nstextview/checktextindocument(_:).md)
  Performs the default text checking on the entire document.
- [func checkTextInSelection(Any?)](nstextview/checktextinselection(_:).md)
  Performs the default text checking on the current selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/checktext(in:types:options:))*