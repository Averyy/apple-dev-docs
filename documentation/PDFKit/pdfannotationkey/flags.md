# flags

**Framework**: PDFKit  
**Kind**: property  
**Role**: Type Property

An integer value that specifies flags for the annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let flags: PDFAnnotationKey
```

```c
extern PDFAnnotationKey PDFAnnotationKeyFlags;
```

## Discussion

For a full description of annotation flags, see [Table 165](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf#page=393) in the [Adobe PDF 1.7 Specification](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf).

## See Also

### Configuring General Properties
- [static let contents: PDFAnnotationKey](./contents.md)
  The text that the annotation displays or represents.
- [static let date: PDFAnnotationKey](./date.md)
  The date, or string representation of a date, of the annotation’s most recent modification.
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
- [static let textLabel: PDFAnnotationKey](./textlabel.md)
  A string that represents the title of the annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey/flags)*