# leadingPadding

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The amount of margin space reserved during paragraph layout between the leading edge of the text layout fragment and the start of the lines in the paragraph.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var leadingPadding: CGFloat { get }
```

```objc
@property (readonly) CGFloat leadingPadding;
```

#### Discussion

This is with respect to according to the primary writing direction of the paragraph and the start of the lines in the paragraph.

## See Also

### Defining margins and padding
- [var bottomMargin: CGFloat](./bottommargin.md)
  The amount of space reserved during paragraph layout between the bottom of the last line in the paragraph and the bottom of the text layout fragment.
- [var topMargin: CGFloat](./topmargin.md)
  The amount of space reserved during paragraph layout between the top of the text layout fragment and the top of the first line in the paragraph.
- [var trailingPadding: CGFloat](./trailingpadding.md)
  The amount of margin space reserved during paragraph layout between the end of the lines in the paragraph and the trailing edge of the text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/leadingpadding)*