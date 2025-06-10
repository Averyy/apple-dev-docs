# child(at:)

**Framework**: PDFKit  
**Kind**: method

Returns the child outline object at the specified index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func child(at index: Int) -> PDFOutline?
```

#### Discussion

The index is zero-based. This method throws an exception if `index` is out of range.

> ❗ **Important**:  In macOS 10.5 and later, a `PDFOutline` object retains all its children, so `childAtIndex:` returns the same retained child outline object every time it’s called. This means that you do not need to retain the object returned by `childAtIndex:`. This differs from the behavior of `PDFOutline` in OS X v10.4. In Tiger, `childAtIndex:` returns an auto-released, one-off child outline object, when meant that you had to include code to retain the child.

## See Also

- [var document: PDFDocument?](pdfoutline/document.md)
  Returns the document with which the outline is associated.
- [var numberOfChildren: Int](pdfoutline/numberofchildren.md)
  Returns the number of child outline objects in the outline.
- [var parent: PDFOutline?](pdfoutline/parent.md)
  Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).
- [var index: Int](pdfoutline/index.md)
  Returns the index of the outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/child(at:))*