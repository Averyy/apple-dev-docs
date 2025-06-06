# setRuby(_:in:)

**Framework**: AVFoundation  
**Kind**: method

Sets ruby text for a range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func setRuby(_ rubyText: AVCaption.Ruby, in range: NSRange)
```

## Parameters

- `rubyText`: The ruby text.
- `range`: The range to which the ruby text applies.

## See Also

- [AVCaption.Ruby](avcaption/ruby.md)
  An object that presents ruby characters.
- [func removeRuby(in: NSRange)](avmutablecaption/removeruby(in:).md)
  Removes ruby text from a range.
- [AVCaption.TextCombine](avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [func setTextCombine(AVCaption.TextCombine, in: NSRange)](avmutablecaption/settextcombine(_:in:).md)
  Sets text combine for a range.
- [func removeTextCombine(in: NSRange)](avmutablecaption/removetextcombine(in:).md)
  Removes text combine from a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption/setruby(_:in:))*