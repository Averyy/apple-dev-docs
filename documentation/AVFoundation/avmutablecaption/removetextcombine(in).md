# removeTextCombine(in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes text combine from a range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func removeTextCombine(in range: NSRange)
```

## Parameters

- `range`: The range from which the system removes text combine.

## See Also

### Configuring advanced typography
- [AVCaption.Ruby](../avcaption/ruby.md)
  An object that presents ruby characters.
- [func setRuby(AVCaption.Ruby, in: NSRange)](./setruby%28_,in%29.md)
  Sets ruby text for a range.
- [func removeRuby(in: NSRange)](./removeruby%28in%29.md)
  Removes ruby text from a range.
- [AVCaption.TextCombine](../avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [func setTextCombine(AVCaption.TextCombine, in: NSRange)](./settextcombine%28_,in%29.md)
  Sets text combine for a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption/removetextcombine(in:))*