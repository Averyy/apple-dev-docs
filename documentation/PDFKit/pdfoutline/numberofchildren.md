# numberOfChildren

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the number of child outline objects in the outline.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var numberOfChildren: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger numberOfChildren;
```

## See Also

### Getting Information About an Outline
- [var document: PDFDocument?](./document.md)
  Returns the document with which the outline is associated.
- [var parent: PDFOutline?](./parent.md)
  Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).
- [func child(at: Int) -> PDFOutline?](./child%28at%29.md)
  Returns the child outline object at the specified index.
- [var index: Int](./index.md)
  Returns the index of the outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/numberofchildren)*