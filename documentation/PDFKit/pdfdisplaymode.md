# PDFDisplayMode

**Framework**: PDFKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum PDFDisplayMode : NSInteger;
```

## Topics

### Constants
- [PDFDisplayMode.singlePage](./pdfdisplaymode/singlepage.md)
  A display mode where the document displays one page at a time horizontally and vertically.
- [PDFDisplayMode.singlePageContinuous](./pdfdisplaymode/singlepagecontinuous.md)
  A display mode where the document displays in continuous mode vertically, with single-page width horizontally.
- [PDFDisplayMode.twoUp](./pdfdisplaymode/twoup.md)
  A display mode where the document displays two pages side-by-side.
- [PDFDisplayMode.twoUpContinuous](./pdfdisplaymode/twoupcontinuous.md)
  A display mode where the document displays in continuous mode vertically and displays two pages side-by-side horizontally.
### Initializers
- [init?(rawValue: Int)](./pdfdisplaymode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Display Modes and Characteristics
- [var displayMode: PDFDisplayMode](./pdfview/displaymode.md)
  The current display mode.
- [Additional Display Configurations](./additional-display-configurations.md)
  Operations for setting up page breaks, a display box, and display direction.
- [Book Display](./book-display.md)
  Operations to setup a book display for a PDF view.
- [Graphics Properties](./graphics-properties.md)
  Operations to define the background color, antialiasing, and greeking for a PDF view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdisplaymode)*