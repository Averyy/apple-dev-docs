# textLabel

**Framework**: PDFKit  
**Kind**: property  
**Role**: Type Property

A string that represents the title of the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let textLabel: PDFAnnotationKey
```

```c
extern PDFAnnotationKey PDFAnnotationKeyTextLabel;
```

## See Also

### Configuring General Properties
- [static let contents: PDFAnnotationKey](./contents.md)
  The text that the annotation displays or represents.
- [static let date: PDFAnnotationKey](./date.md)
  The date, or string representation of a date, of the annotation’s most recent modification.
- [static let flags: PDFAnnotationKey](./flags.md)
  An integer value that specifies flags for the annotation.
- [static let name: PDFAnnotationKey](./name.md)
  A string that uniquely identifies the annotation among all annotations on the same page.
- [static let page: PDFAnnotationKey](./page.md)
  A dictionary or PDF page object that includes the annotation.
- [static let parent: PDFAnnotationKey](./parent.md)
  A dictionary or annotation object that a pop-up or widget belongs to.
- [static let quadPoints: PDFAnnotationKey](./quadpoints.md)
  An array of floating point values that specifies a rectangular region of a page.
- [static let rect: PDFAnnotationKey](./rect.md)
  The rectangle that the annotation occupies on the page, in page-space coordinates.
- [static let subtype: PDFAnnotationKey](./subtype.md)
  The type of annotation that the entries in a dictionary describe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey/textlabel)*