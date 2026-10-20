# alignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alignment of all the receiver’s text.

**Availability**:
- macOS

## Declaration

```swift
var alignment: NSTextAlignment { get set }
```

```objc
@property NSTextAlignment alignment;
```

#### Discussion

The value of  `mode` must be one of the alignments described in [`NSTextAlignment`](../nstextalignment.md).

Text using `NSNaturalTextAlignment` is actually displayed using one of the other alignments, depending on the natural alignment of the text’s script.

## See Also

### Setting text alignment
- [func alignCenter(Any?)](./aligncenter%28_%29.md)
  This action method applies center alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignLeft(Any?)](./alignleft%28_%29.md)
  This action method applies left alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignRight(Any?)](./alignright%28_%29.md)
  This action method applies right alignment to selected paragraphs (or all text if the receiver is a plain text object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/alignment)*