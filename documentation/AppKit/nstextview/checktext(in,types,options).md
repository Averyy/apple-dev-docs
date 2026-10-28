# checkText(in:types:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Check and replace the text in the range using the specified checking types and options.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func checkText(in range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any] = [:])
```

```objc
- (void) checkTextInRange:(NSRange) range types:(NSTextCheckingTypes) checkingTypes options:(NSDictionary<NSString *,id> *) options;
```

## Discussion

This method calls the delegate method [`textView(_:willCheckTextIn:options:types:)`](../nstextviewdelegate/textview%28_,willchecktextin,options,types%29.md) allowing you to modify the parameters before the checking occurs.

This method usually would not be called directly, since `NSTextView` itself will call it as needed, but it can be overridden.

## Parameters

- `range`: The range to check.
- `checkingTypes`: The type of checking to be performed, passed by-reference. The possible constants are listed in [`NSTextCheckingTypes`](../../Foundation/nstextcheckingtypes.md) and can be combined using the C bit-wise `OR` operator to perform multiple checks at the same time.
- `options`: A dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.

## See Also

### Checking and substituting text
- [func checkTextInDocument(Any?)](./checktextindocument%28_%29.md)
  Performs the default text checking on the entire document.
- [func checkTextInSelection(Any?)](./checktextinselection%28_%29.md)
  Performs the default text checking on the current selection.
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
- [func performValidatedReplacement(in: NSRange, with: NSAttributedString) -> Bool](./performvalidatedreplacement%28in,with%29.md)
  Replaces text in the range you specify with the attributed string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/checktext(in:types:options:))*