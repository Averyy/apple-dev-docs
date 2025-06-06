# PDFDisplayMode

**Framework**: PDFKit  
**Kind**: enum

A wrapper for the chosen display mode constant.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PDFDisplayMode
```

## Topics

### Constants
- [PDFDisplayMode.singlePage](pdfdisplaymode/singlepage.md)
  A display mode where the document displays one page at a time horizontally and vertically.
- [PDFDisplayMode.singlePageContinuous](pdfdisplaymode/singlepagecontinuous.md)
  A display mode where the document displays in continuous mode vertically, with single-page width horizontally.
- [PDFDisplayMode.twoUp](pdfdisplaymode/twoup.md)
  A display mode where the document displays two pages side-by-side.
- [PDFDisplayMode.twoUpContinuous](pdfdisplaymode/twoupcontinuous.md)
  A display mode where the document displays in continuous mode vertically and displays two pages side-by-side horizontally.
### Initializers
- [init?(rawValue: Int)](pdfdisplaymode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var displayMode: PDFDisplayMode](pdfview/displaymode.md)
  The current display mode.
- [Additional Display Configurations](additional-display-configurations.md)
  Operations for setting up page breaks, a display box, and display direction.
- [Book Display](book-display.md)
  Operations to setup a book display for a PDF view.
- [Graphics Properties](graphics-properties.md)
  Operations to define the background color, antialiasing, and greeking for a PDF view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdisplaymode)*