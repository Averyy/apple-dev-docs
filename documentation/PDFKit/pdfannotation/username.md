# userName

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the name of the user who created the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var userName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * userName;
```

## Return Value

The name of the user who created the annotation, or NULL if no user name is set.

## See Also

### Related Documentation
- [class PDFAnnotation](../pdfannotation.md)
  An annotation in a PDF document.
### Accessing Information About an Annotation
- [var page: PDFPage?](./page.md)
  Returns the page that the annotation is associated with.
- [var modificationDate: Date?](./modificationdate.md)
  Returns the modification date of the annotation.
- [var type: String?](./type.md)
  Returns the type of the annotation.
- [var action: PDFAction?](./action.md)
  An object that represents an action for a PDF element, such as a link annotation.
- [class PDFAction](../pdfaction.md)
  An action that is performed when, for example, a PDF annotation is activated or an outline item is clicked.
- [class PDFDestination](../pdfdestination.md)
  A `PDFDestination` object describes a point on a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/username)*