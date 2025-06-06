# annotationsChanged(on:)

**Framework**: PDFKit  
**Kind**: method

Tells the PDF view that an annotation on the specified page has changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func annotationsChanged(on page: PDFPage)
```

#### Discussion

When the `PDFView` object receives this message, it rescans for tool tips and pop-ups and informs the `PDFThumbailView` objects so the thumbnail images can be redrawn.

## See Also

- [Link Annotations](link-annotations.md)
  Validate and handle links in a PDF view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/annotationschanged(on:))*