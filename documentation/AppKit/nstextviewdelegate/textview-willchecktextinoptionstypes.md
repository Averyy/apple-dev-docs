# textView(_:willCheckTextIn:options:types:)

**Framework**: AppKit  
**Kind**: method

Invoked to allow the delegate to modify the text checking process before it occurs.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func textView(_ view: NSTextView, willCheckTextIn range: NSRange, options: [NSSpellChecker.OptionKey : Any] = [:], types checkingTypes: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]
```

#### Return Value

A dictionary containing an alternative to the options `dictionary`.

#### Discussion

Invoked by [`checkText(in:types:options:)`](nstextview/checktext(in:types:options:).md), this method allows control over text checking `options`s (via the return value) or types (by modifying the flags pointed to by the inout parameter `checkingTypes`)

## Parameters

- `view`: The text view sending the message.
- `range`: The range to be checked.
- `options`: A dictionary of values used during the checking process to perform. See Spell Checking Option Dictionary Keys for the supported values.
- `checkingTypes`: You can change this parameter to alter the types of checking to be performed.

## See Also

- [func textView(NSTextView, shouldSetSpellingState: Int, range: NSRange) -> Int](nstextviewdelegate/textview(_:shouldsetspellingstate:range:).md)
  Sent when the spelling state is changed.
- [func textView(NSTextView, didCheckTextIn: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]](nstextviewdelegate/textview(_:didchecktextin:types:options:results:orthography:wordcount:).md)
  Invoked to allow the delegate to modify the text checking results after checking has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willchecktextin:options:types:))*