# modificationDate

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the modification date of the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var modificationDate: Date? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDate * modificationDate;
```

#### Return Value

The modification date of the annotation, or `NULL` if there is no modification date.

## See Also

### Related Documentation
- [class PDFAnnotation](../pdfannotation.md)
  An annotation in a PDF document.
### Accessing Information About an Annotation
- [var page: PDFPage?](./page.md)
  Returns the page that the annotation is associated with.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/modificationdate)*