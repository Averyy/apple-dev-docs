# index

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the index of the outline.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var index: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger index;
```

#### Discussion

The index of the outline object is relative to its siblings and from the perspective of the parent of the outline object. The root outline object, and any outline object without a parent, has an index value of `0`.

## See Also

### Getting Information About an Outline
- [var document: PDFDocument?](./document.md)
  Returns the document with which the outline is associated.
- [var numberOfChildren: Int](./numberofchildren.md)
  Returns the number of child outline objects in the outline.
- [var parent: PDFOutline?](./parent.md)
  Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).
- [func child(at: Int) -> PDFOutline?](./child%28at%29.md)
  Returns the child outline object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/index)*