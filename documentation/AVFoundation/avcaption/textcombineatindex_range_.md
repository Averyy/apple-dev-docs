# textCombineAtIndex:range:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the text combine at the index position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS

## Declaration

```objc
- (AVCaptionTextCombine) textCombineAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

#### Return Value

The text combine.

## Parameters

- `index`: A character position in the caption text.
- `outRange`: A pointer that stores the range to which the returned text combine applies.

## See Also

### Accessing advanced typography
- [- rubyAtIndex:range:](./rubyatindex_range_.md)
  Returns the ruby text at the index position.
- [AVCaption.Ruby](./ruby.md)
  An object that presents ruby characters.
- [AVCaption.TextCombine](./textcombine.md)
  The caption’s supported rendering policy options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/textcombineatindex:range:)*