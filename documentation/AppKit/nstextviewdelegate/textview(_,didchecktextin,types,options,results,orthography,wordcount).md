# textView(_:didCheckTextIn:types:options:results:orthography:wordCount:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to allow the delegate to modify the text checking results after checking has occurred.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, didCheckTextIn range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any] = [:], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]
```

```objc
- (NSArray<NSTextCheckingResult *> *) textView:(NSTextView *) view didCheckTextInRange:(NSRange) range types:(NSTextCheckingTypes) checkingTypes options:(NSDictionary<NSString *,id> *) options results:(NSArray<NSTextCheckingResult *> *) results orthography:(NSOrthography *) orthography wordCount:(NSInteger) wordCount;
```

#### Return Value

An array of [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md) instances. You can return the results array as is, or an altered array of [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md) objects.

#### Discussion

Invoked by [`handleTextCheckingResults(_:forRange:types:options:orthography:wordCount:)`](../nstextview/handletextcheckingresults%28_,forrange,types,options,orthography,wordcount%29.md), this method allows observation of text checking, or modification of the results

## Parameters

- `view`: The text view sending the message.
- `range`: The range that was checked.
- `checkingTypes`: The type of checking that was performed. The possible constants are listed in [`NSTextCheckingTypes`](../../Foundation/nstextcheckingtypes.md) and can be combined using the C bit-wise `OR` operator to perform multiple checks at the same time.
- `options`: A dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.
- `results`: An array of [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md) instances.
- `orthography`: The orthography of the text.
- `wordCount`: The number of words checked.

## See Also

### Working With the Spelling Checker
- [func textView(NSTextView, shouldSetSpellingState: Int, range: NSRange) -> Int](./textview%28_,shouldsetspellingstate,range%29.md)
  Sent when the spelling state is changed.
- [func textView(NSTextView, willCheckTextIn: NSRange, options: [NSSpellChecker.OptionKey : Any], types: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]](./textview%28_,willchecktextin,options,types%29.md)
  Invoked to allow the delegate to modify the text checking process before it occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:didchecktextin:types:options:results:orthography:wordcount:))*