# trailingPadding

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The amount of margin space reserved during paragraph layout between the end of the lines in the paragraph and the trailing edge of the text layout fragment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var trailingPadding: CGFloat { get }
```

```objc
@property (readonly) CGFloat trailingPadding;
```

## Discussion

This is with respect to the primary writing direction of the paragraph.

## See Also

### Defining margins and padding
- [var bottomMargin: CGFloat](./bottommargin.md)
  The amount of space reserved during paragraph layout between the bottom of the last line in the paragraph and the bottom of the text layout fragment.
- [var leadingPadding: CGFloat](./leadingpadding.md)
  The amount of margin space reserved during paragraph layout between the leading edge of the text layout fragment and the start of the lines in the paragraph.
- [var topMargin: CGFloat](./topmargin.md)
  The amount of space reserved during paragraph layout between the top of the text layout fragment and the top of the first line in the paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/trailingpadding)*