# handleTextCheckingResults(_:forRange:types:options:orthography:wordCount:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles the text checking results returned by the text view

**Availability**:
- macOS 10.6+

## Declaration

```swift
func handleTextCheckingResults(_ results: [NSTextCheckingResult], forRange range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any] = [:], orthography: NSOrthography, wordCount: Int)
```

```objc
- (void) handleTextCheckingResults:(NSArray<NSTextCheckingResult *> *) results forRange:(NSRange) range types:(NSTextCheckingTypes) checkingTypes options:(NSDictionary<NSString *,id> *) options orthography:(NSOrthography *) orthography wordCount:(NSInteger) wordCount;
```

## Discussion

The [`NSTextViewDelegate`](../nstextviewdelegate.md) offers a method, [`textView(_:didCheckTextIn:types:options:results:orthography:wordCount:)`](../nstextviewdelegate/textview%28_,didchecktextin,types,options,results,orthography,wordcount%29.md) that is called after the checking is performed, allowing you to modify the results.

This method usually would not be called directly, since `NSTextView` itself will call it as needed, but it can be overridden.

## Parameters

- `results`: An array of [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md) objects.
- `range`: The range of text that was checked.
- `checkingTypes`: The type of checking  performed. The possible constants are listed in [`NSTextCheckingTypes`](../../Foundation/nstextcheckingtypes.md) and can be combined using the C bit-wise `OR` operator to perform multiple checks at the same time.
- `options`: The dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.
- `orthography`: The orthography of the checked text.
- `wordCount`: The number of words.

## See Also

### Checking and substituting text
- [func checkTextInDocument(Any?)](./checktextindocument%28_%29.md)
  Performs the default text checking on the entire document.
- [func checkTextInSelection(Any?)](./checktextinselection%28_%29.md)
  Performs the default text checking on the current selection.
- [func checkText(in: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any])](./checktext%28in,types,options%29.md)
  Check and replace the text in the range using the specified checking types and options.
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
- [func performValidatedReplacement(in: NSRange, with: NSAttributedString) -> Bool](./performvalidatedreplacement%28in,with%29.md)
  Replaces text in the range you specify with the attributed string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/handletextcheckingresults(_:forrange:types:options:orthography:wordcount:))*