# PDFDocumentPermissions

**Framework**: PDFKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that specifies document permissions status.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PDFDocumentPermissions
```

```c
enum PDFDocumentPermissions : NSInteger;
```

## Topics

### Enumeration Cases
- [PDFDocumentPermissions.none](./pdfdocumentpermissions/none.md)
  The status that indicates no document permissions.
- [PDFDocumentPermissions.user](./pdfdocumentpermissions/user.md)
  The status that indicates user document permissions.
- [PDFDocumentPermissions.owner](./pdfdocumentpermissions/owner.md)
  The status that indicates owner document permissions.
### Initializers
- [init?(rawValue: Int)](./pdfdocumentpermissions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct PDFDocumentAttribute](./pdfdocumentattribute.md)
  A structure that specifies document attributes.
- [struct PDFDocumentWriteOption](./pdfdocumentwriteoption.md)
  A structure that specifies file writing options for a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocumentpermissions)*