# PDFDisplayBox

**Framework**: PDFKit  
**Kind**: enum  
**Role**: Enumeration

The following box types may be used with `PDFPage` drawing and bounds-setting methods. See the Adobe PDF Specification for more information on box types, units, and coordinate systems.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PDFDisplayBox
```

```c
enum PDFDisplayBox : NSInteger;
```

## Topics

### Constants
- [PDFDisplayBox.mediaBox](./pdfdisplaybox/mediabox.md)
  A rectangle defining the boundaries of the physical medium for display or printing, expressed in default user-space units.
- [PDFDisplayBox.cropBox](./pdfdisplaybox/cropbox.md)
  A rectangle defining the boundaries of the visible region , expressed in default user-space units. Default value equal to `kPDFDisplayBoxMediaBox`.
- [PDFDisplayBox.bleedBox](./pdfdisplaybox/bleedbox.md)
  A rectangle defining the boundaries of the clip region for the page contents in a production environment. Default value equal to `kPDFDisplayBoxCropBox`.
- [PDFDisplayBox.trimBox](./pdfdisplaybox/trimbox.md)
  A rectangle defining the intended boundaries of the finished page. Default value equal to `kPDFDisplayBoxCropBox`.
- [PDFDisplayBox.artBox](./pdfdisplaybox/artbox.md)
  A rectangle defining the boundaries of the page’s meaningful content including surrounding white space intended for display. Default value equal to `kPDFDisplayBoxCropBox`.
### Initializers
- [init?(rawValue: Int)](./pdfdisplaybox/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting Types
- [enum PDFDisplayDirection](./pdfdisplaydirection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdisplaybox)*