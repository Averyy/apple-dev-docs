# rubyAtIndex:range:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the ruby text at the index position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```objc
- (AVCaptionRuby *) rubyAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

#### Return Value

The ruby text.

## Parameters

- `index`: A character position in the caption text.
- `outRange`: A pointer that stores the range to which the returned ruby text applies.

## See Also

### Accessing advanced typography
- [AVCaption.Ruby](./ruby.md)
  An object that presents ruby characters.
- [- textCombineAtIndex:range:](./textcombineatindex_range_.md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](./textcombine.md)
  The caption’s supported rendering policy options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/rubyatindex:range:)*