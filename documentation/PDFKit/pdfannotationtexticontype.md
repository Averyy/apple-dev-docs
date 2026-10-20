# PDFAnnotationTextIconType

**Framework**: PDFKit  
**Kind**: struct  
**Role**: Structure

Constants for icon type values in text annotation property dictionaries.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct PDFAnnotationTextIconType
```

```c
typedef NSString * const PDFAnnotationTextIconType;
```

## Topics

### Choosing a Text Icon Type
- [static let comment: PDFAnnotationTextIconType](./pdfannotationtexticontype/comment.md)
  An icon that represents a comment.
- [static let key: PDFAnnotationTextIconType](./pdfannotationtexticontype/key.md)
  An icon that represents a key.
- [static let note: PDFAnnotationTextIconType](./pdfannotationtexticontype/note.md)
  An icon that represents a note.
- [static let help: PDFAnnotationTextIconType](./pdfannotationtexticontype/help.md)
  An icon that indicates help information is available.
- [static let newParagraph: PDFAnnotationTextIconType](./pdfannotationtexticontype/newparagraph.md)
  An icon that represents a new paragraph.
- [static let paragraph: PDFAnnotationTextIconType](./pdfannotationtexticontype/paragraph.md)
  An icon that represents a paragraph.
- [static let insert: PDFAnnotationTextIconType](./pdfannotationtexticontype/insert.md)
  An icon that represents an insertion command.
### Creating a Text Icon Type
- [init(rawValue: String)](./pdfannotationtexticontype/init%28rawvalue%29.md)
  Creates a text icon type using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring Text Annotations
- [var iconType: PDFTextAnnotationIconType](./pdfannotation/icontype.md)
  The type of icon to display for a pop-up text annotation.
- [enum PDFTextAnnotationIconType](./pdftextannotationicontype.md)
  The types of icons that a text annotation can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtexticontype)*