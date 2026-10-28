# page

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the page that the annotation is associated with.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var page: PDFPage? { get set }
```

```objc
@property (nonatomic, weak, nullable) PDFPage * page;
```

## Return Value

The PDF page associated with the annotation.

## Discussion

The [`addAnnotation(_:)`](../pdfpage/addannotation%28_%29.md) method in the `PDFPage` class lets you associate an annotation with a page.

## See Also

### Accessing Information About an Annotation
- [var modificationDate: Date?](./modificationdate.md)
  Returns the modification date of the annotation.
- [var userName: String?](./username.md)
  Returns the name of the user who created the annotation.
- [var type: String?](./type.md)
  Returns the type of the annotation.
- [var action: PDFAction?](./action.md)
  An object that represents an action for a PDF element, such as a link annotation.
- [class PDFAction](../pdfaction.md)
  An action that is performed when, for example, a PDF annotation is activated or an outline item is clicked.
- [class PDFDestination](../pdfdestination.md)
  A `PDFDestination` object describes a point on a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/page)*