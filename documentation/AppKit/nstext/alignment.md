# alignment

**Framework**: AppKit  
**Kind**: property

The alignment of all the receiver’s text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var alignment: NSTextAlignment { get set }
```

#### Discussion

The value of  `mode` must be one of the alignments described in [`NSTextAlignment`](nstextalignment.md).

Text using `NSNaturalTextAlignment` is actually displayed using one of the other alignments, depending on the natural alignment of the text’s script.

## See Also

- [func alignCenter(Any?)](nstext/aligncenter(_:).md)
  This action method applies center alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignLeft(Any?)](nstext/alignleft(_:).md)
  This action method applies left alignment to selected paragraphs (or all text if the receiver is a plain text object).
- [func alignRight(Any?)](nstext/alignright(_:).md)
  This action method applies right alignment to selected paragraphs (or all text if the receiver is a plain text object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/alignment)*