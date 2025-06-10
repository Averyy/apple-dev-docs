# PDFDocumentWriteOption

**Framework**: PDFKit  
**Kind**: struct

A structure that specifies file writing options for a document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct PDFDocumentWriteOption
```

## Topics

### Creating Write Options
- [init(rawValue: String)](pdfdocumentwriteoption/init(rawvalue:).md)
  Initialize a `PDFDocumentWriteOption` structure.
### Getting Write Option Properties
- [static let ownerPasswordOption: PDFDocumentWriteOption](pdfdocumentwriteoption/ownerpasswordoption.md)
  An `NSString` object for the owner’s password which is required for encryption.
- [static let userPasswordOption: PDFDocumentWriteOption](pdfdocumentwriteoption/userpasswordoption.md)
  An `NSString` object for the user’s password which is optional for encryption.
### Type Properties
- [static let accessPermissionsOption: PDFDocumentWriteOption](pdfdocumentwriteoption/accesspermissionsoption.md)
- [static let burnInAnnotationsOption: PDFDocumentWriteOption](pdfdocumentwriteoption/burninannotationsoption.md)
- [static let optimizeImagesForScreenOption: PDFDocumentWriteOption](pdfdocumentwriteoption/optimizeimagesforscreenoption.md)
- [static let saveImagesAsJPEGOption: PDFDocumentWriteOption](pdfdocumentwriteoption/saveimagesasjpegoption.md)
- [static let saveTextFromOCROption: PDFDocumentWriteOption](pdfdocumentwriteoption/savetextfromocroption.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum PDFDocumentPermissions](pdfdocumentpermissions.md)
  An enumeration that specifies document permissions status.
- [struct PDFDocumentAttribute](pdfdocumentattribute.md)
  A structure that specifies document attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentwriteoption)*