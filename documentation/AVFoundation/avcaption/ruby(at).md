# ruby(at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the ruby text at the index position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
@nonobjc
func ruby(at index: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)
```

## Return Value

A tuple that contains the ruby text and range to which it applies.

## Parameters

- `index`: A character position in the caption text.

## See Also

### Accessing advanced typography
- [AVCaption.Ruby](./ruby.md)
  An object that presents ruby characters.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](./textcombine%28at%29.md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](./textcombine.md)
  The caption’s supported rendering policy options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/ruby(at:))*