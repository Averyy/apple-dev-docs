# textView(_:shouldSetSpellingState:range:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the spelling state is changed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldSetSpellingState value: Int, range affectedCharRange: NSRange) -> Int
```

```objc
- (NSInteger) textView:(NSTextView *) textView shouldSetSpellingState:(NSInteger) value range:(NSRange) affectedCharRange;
```

## Return Value

The actual spelling state to set.

## Discussion

Delegate only. Allows delegate to control the setting of spelling and grammar indicators.

## Parameters

- `textView`: The text view sending the message.
- `value`: The proposed spelling state value to set. Possible values, for the temporary attribute on the layout manager using the key NSSpellingStateAttributeName, are:

  - [`NSSpellingStateSpellingFlag`](../nsspellingstate/nsspellingstatespellingflag.md) to highlight spelling issues.
  - [`NSSpellingStateGrammarFlag`](../nsspellingstate/nsspellingstategrammarflag.md) to highlight grammar issues.
- `affectedCharRange`: The character range over which to set the given spelling state.

## See Also

### Related Documentation
- [func setSpellingState(Int, range: NSRange)](../nstextview/setspellingstate%28_,range%29.md)
  Sets the spelling state, which controls the display of the spelling and grammar indicators on the given text range.
### Working With the Spelling Checker
- [func textView(NSTextView, willCheckTextIn: NSRange, options: [NSSpellChecker.OptionKey : Any], types: UnsafeMutablePointer<NSTextCheckingTypes>) -> [NSSpellChecker.OptionKey : Any]](./textview%28_,willchecktextin,options,types%29.md)
  Invoked to allow the delegate to modify the text checking process before it occurs.
- [func textView(NSTextView, didCheckTextIn: NSRange, types: NSTextCheckingTypes, options: [NSSpellChecker.OptionKey : Any], results: [NSTextCheckingResult], orthography: NSOrthography, wordCount: Int) -> [NSTextCheckingResult]](./textview%28_,didchecktextin,types,options,results,orthography,wordcount%29.md)
  Invoked to allow the delegate to modify the text checking results after checking has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldsetspellingstate:range:))*