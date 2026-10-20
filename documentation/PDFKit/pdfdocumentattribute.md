# PDFDocumentAttribute

**Framework**: PDFKit  
**Kind**: struct  
**Role**: Structure

A structure that specifies document attributes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct PDFDocumentAttribute
```

```c
typedef NSString * PDFDocumentAttribute;
```

## Topics

### Creating Document Attributes
- [init(rawValue: String)](./pdfdocumentattribute/init%28rawvalue%29.md)
  Initialize a `PDFDocumentAttribute` structure.
### Getting Document Attributes
- [static let authorAttribute: PDFDocumentAttribute](./pdfdocumentattribute/authorattribute.md)
  An optional text string containing the name of the author of the document.
- [static let creationDateAttribute: PDFDocumentAttribute](./pdfdocumentattribute/creationdateattribute.md)
  An optional text string containing the document’s creation date.
- [static let creatorAttribute: PDFDocumentAttribute](./pdfdocumentattribute/creatorattribute.md)
  An optional text string containing the name of the application that created the document content.
- [static let keywordsAttribute: PDFDocumentAttribute](./pdfdocumentattribute/keywordsattribute.md)
  An optional array of text strings containing keywords for the document.
- [static let modificationDateAttribute: PDFDocumentAttribute](./pdfdocumentattribute/modificationdateattribute.md)
  An optional text string containing the document’s last-modified date.
- [static let producerAttribute: PDFDocumentAttribute](./pdfdocumentattribute/producerattribute.md)
  An optional text string containing the name of the application that produced the PDF data for the document.
- [static let subjectAttribute: PDFDocumentAttribute](./pdfdocumentattribute/subjectattribute.md)
  An optional text string containing a description of the subject of the document.
- [static let titleAttribute: PDFDocumentAttribute](./pdfdocumentattribute/titleattribute.md)
  An optional text string containing the title of the document.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum PDFDocumentPermissions](./pdfdocumentpermissions.md)
  An enumeration that specifies document permissions status.
- [struct PDFDocumentWriteOption](./pdfdocumentwriteoption.md)
  A structure that specifies file writing options for a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentattribute)*