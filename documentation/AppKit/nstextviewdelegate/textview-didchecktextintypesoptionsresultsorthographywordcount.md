# textView(_:didCheckTextIn:types:options:results:orthography:wordCount:)

**Framework**: AppKit  
**Kind**: method

Invoked to allow the delegate to modify the text checking results after checking has occurred.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, didCheckTextIn range: NSRange, types checkingTypes: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any] = [:], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]
```

#### Return Value

An array of [`NSTextCheckingResult`](https://developer.apple.com/documentation/Foundation/NSTextCheckingResult) instances. You can return the results array as is, or an altered array of [`NSTextCheckingResult`](https://developer.apple.com/documentation/Foundation/NSTextCheckingResult) objects.

#### Discussion

Invoked by [`handleTextCheckingResults(_:forRange:types:options:orthography:wordCount:)`](nstextview/handletextcheckingresults(_:forrange:types:options:orthography:wordcount:).md), this method allows observation of text checking, or modification of the results

## Parameters

- `view`: The text view sending the message.
- `range`: The range that was checked.
- `checkingTypes`: The type of checking that was performed. The possible constants are listed in   and can be combined using the C bit-wise   operator to perform multiple checks at the same time.
- `options`: A dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.
- `results`: An array of   instances.
- `orthography`: The orthography of the text.
- `wordCount`: The number of words checked.

## See Also

- [func textView(NSTextView, shouldSetSpellingState: Int, range: NSRange) -> Int](nstextviewdelegate/textview(_:shouldsetspellingstate:range:).md)
  Sent when the spelling state is changed.
- [func textView(NSTextView, willCheckTextIn: NSRange, options: [NSSpellChecker.OptionKey : Any], types: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]](nstextviewdelegate/textview(_:willchecktextin:options:types:).md)
  Invoked to allow the delegate to modify the text checking process before it occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:didchecktextin:types:options:results:orthography:wordcount:))*