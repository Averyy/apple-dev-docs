# setRuby(_:in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

### Configuring advanced typography
- [AVCaption.Ruby](../avcaption/ruby.md)
  An object that presents ruby characters.
- [func removeRuby(in: NSRange)](./removeruby%28in%29.md)
  Removes ruby text from a range.
- [AVCaption.TextCombine](../avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [func setTextCombine(AVCaption.TextCombine, in: NSRange)](./settextcombine%28_,in%29.md)
  Sets text combine for a range.
- [func removeTextCombine(in: NSRange)](./removetextcombine%28in%29.md)
  Removes text combine from a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption/setruby(_:in:))*