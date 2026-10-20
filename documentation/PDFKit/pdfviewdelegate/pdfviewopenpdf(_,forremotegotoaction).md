# pdfViewOpenPDF(_:forRemoteGoToAction:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Opens a specified page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func pdfViewOpenPDF(_ sender: PDFView, forRemoteGoToAction action: PDFActionRemoteGoTo)
```

```objc
- (void) PDFViewOpenPDF:(PDFView *) sender forRemoteGoToAction:(PDFActionRemoteGoTo *) action;
```

## See Also

### Working with Annotation Actions
- [func pdfViewPerformFind(PDFView)](./pdfviewperformfind%28_%29.md)
  Performs a find operation.
- [func pdfViewPerformGo(toPage: PDFView)](./pdfviewperformgo%28topage%29.md)
  Performs a go-to operation.
- [func pdfViewPerformPrint(PDFView)](./pdfviewperformprint%28_%29.md)
  Prints the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfviewdelegate/pdfviewopenpdf(_:forremotegotoaction:))*