# setTextCombine(_:in:)

**Framework**: AVFoundation  
**Kind**: method

Sets text combine for a range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func setTextCombine(_ textCombine: AVCaption.TextCombine, in range: NSRange)
```

## Parameters

- `textCombine`: The text combine.
- `range`: The range to which the text combine applies.

## See Also

- [AVCaption.Ruby](avcaption/ruby.md)
  An object that presents ruby characters.
- [func setRuby(AVCaption.Ruby, in: NSRange)](avmutablecaption/setruby(_:in:).md)
  Sets ruby text for a range.
- [func removeRuby(in: NSRange)](avmutablecaption/removeruby(in:).md)
  Removes ruby text from a range.
- [AVCaption.TextCombine](avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [func removeTextCombine(in: NSRange)](avmutablecaption/removetextcombine(in:).md)
  Removes text combine from a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption/settextcombine(_:in:))*