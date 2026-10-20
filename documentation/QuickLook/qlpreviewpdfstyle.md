# QLPreviewPDFStyle

**Framework**: Quick Look  
**Kind**: struct  
**Role**: Structure

A value you use to configure the appearance of previews for PDF files.

**Availability**:
- macOS 10.5+

## Declaration

```swift
struct QLPreviewPDFStyle
```

```c
typedef enum { ... } QLPreviewPDFStyle;
```

## Topics

### Creating a Preview Style for PDF Files
- [init(UInt32)](./qlpreviewpdfstyle/init%28_%29.md)
  Creates a PDF style instance that configures the layout of previews for PDF files.
- [init(rawValue: UInt32)](./qlpreviewpdfstyle/init%28rawvalue%29.md)
  Creates a PDF style instance that configures the layout of previews for PDF files.
- [var rawValue: UInt32](./qlpreviewpdfstyle/rawvalue.md)
  The raw value that represents the layout of previews for PDF files.
### Styles for PDF Previews
- [var kQLPreviewPDFStandardStyle: QLPreviewPDFStyle](./kqlpreviewpdfstandardstyle.md)
  The PDF appears in the operating system’s standard style.
- [var kQLPreviewPDFPagesWithThumbnailsOnLeftStyle: QLPreviewPDFStyle](./kqlpreviewpdfpageswiththumbnailsonleftstyle.md)
  The content of the PDF appears with thumbnails of all pages on the left side of the current page’s content.
- [var kQLPreviewPDFPagesWithThumbnailsOnRightStyle: QLPreviewPDFStyle](./kqlpreviewpdfpageswiththumbnailsonrightstyle.md)
  The content of the PDF appears with thumbnails of all pages on the right side of the current page’s content.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewpdfstyle)*