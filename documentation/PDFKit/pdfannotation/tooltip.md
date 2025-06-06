# toolTip

**Framework**: PDFKit  
**Kind**: property

Returns text for display as a help tag.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var toolTip: String? { get }
```

#### Return Value

A string that contains help tag content, or `NULL` if there is no text associated with the annotation.

#### Discussion

This method is equivalent to sending the message `[self contents]`. PDF Kit’s annotation subclasses override this behavior as appropriate. For example, a `PDFAnnotationLink` object displays a URL or page destination for its help tag.

## See Also

- [var mouseUpAction: PDFAction?](pdfannotation/mouseupaction.md)
  The action to perform when a user releases the mouse button within an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/tooltip)*