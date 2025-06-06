# handleTextCheckingResults(_:forRange:types:options:orthography:wordCount:)

**Framework**: AppKit  
**Kind**: method

Handles the text checking results returned by the text view

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func handleTextCheckingResults(_ results: [NSTextCheckingResult], forRange range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any] = [:], orthography: NSOrthography, wordCount: Int)
```

#### Discussion

The [`NSTextViewDelegate`](nstextviewdelegate.md) offers a method, [`textView(_:didCheckTextIn:types:options:results:orthography:wordCount:)`](nstextviewdelegate/textview(_:didchecktextin:types:options:results:orthography:wordcount:).md) that is called after the checking is performed, allowing you to modify the results.

This method usually would not be called directly, since `NSTextView` itself will call it as needed, but it can be overridden.

## Parameters

- `results`: An array of   objects.
- `range`: The range of text that was checked.
- `checkingTypes`: The type of checking  performed. The possible constants are listed in   and can be combined using the C bit-wise   operator to perform multiple checks at the same time.
- `options`: The dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.
- `orthography`: The orthography of the checked text.
- `wordCount`: The number of words.

## See Also

- [func checkTextInDocument(Any?)](nstextview/checktextindocument(_:).md)
  Performs the default text checking on the entire document.
- [func checkTextInSelection(Any?)](nstextview/checktextinselection(_:).md)
  Performs the default text checking on the current selection.
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](nstextview/checktext(in:types:options:).md)
  Check and replace the text in the range using the specified checking types and options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/handletextcheckingresults(_:forrange:types:options:orthography:wordcount:))*