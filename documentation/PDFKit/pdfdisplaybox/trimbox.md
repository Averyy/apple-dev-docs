# PDFDisplayBox.trimBox

**Framework**: PDFKit  
**Kind**: case  
**Role**: Case

A rectangle defining the intended boundaries of the finished page. Default value equal to `kPDFDisplayBoxCropBox`.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case trimBox
```

```c
kPDFDisplayBoxTrimBox
```

## See Also

### Constants
- [PDFDisplayBox.mediaBox](./mediabox.md)
  A rectangle defining the boundaries of the physical medium for display or printing, expressed in default user-space units.
- [PDFDisplayBox.cropBox](./cropbox.md)
  A rectangle defining the boundaries of the visible region , expressed in default user-space units. Default value equal to `kPDFDisplayBoxMediaBox`.
- [PDFDisplayBox.bleedBox](./bleedbox.md)
  A rectangle defining the boundaries of the clip region for the page contents in a production environment. Default value equal to `kPDFDisplayBoxCropBox`.
- [PDFDisplayBox.artBox](./artbox.md)
  A rectangle defining the boundaries of the page’s meaningful content including surrounding white space intended for display. Default value equal to `kPDFDisplayBoxCropBox`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdisplaybox/trimbox)*