# textView(_:shouldSetSpellingState:range:)

**Framework**: AppKit  
**Kind**: method

Sent when the spelling state is changed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldSetSpellingState value: Int, range affectedCharRange: NSRange) -> Int
```

#### Return Value

The actual spelling state to set.

#### Discussion

Delegate only. Allows delegate to control the setting of spelling and grammar indicators.

## Parameters

- `textView`: The text view sending the message.
- `value`: The proposed spelling state value to set. Possible values, for the temporary attribute on the layout manager using the key NSSpellingStateAttributeName, are:
- `affectedCharRange`: The character range over which to set the given spelling state.

## See Also

- [func setSpellingState(Int, range: NSRange)](nstextview/setspellingstate(_:range:).md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.
- [func textView(NSTextView, willCheckTextIn: NSRange, options: [NSSpellChecker.OptionKey : Any], types: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]](nstextviewdelegate/textview(_:willchecktextin:options:types:).md)
  Invoked to allow the delegate to modify the text checking process before it occurs.
- [func textView(NSTextView, didCheckTextIn: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]](nstextviewdelegate/textview(_:didchecktextin:types:options:results:orthography:wordcount:).md)
  Invoked to allow the delegate to modify the text checking results after checking has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldsetspellingstate:range:))*