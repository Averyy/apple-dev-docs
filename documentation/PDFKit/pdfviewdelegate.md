# PDFViewDelegate

**Framework**: PDFKit  
**Kind**: protocol

The delegate for the `PDFView` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol PDFViewDelegate : NSObjectProtocol
```

## Topics

### Working with Annotation Actions
- [func pdfViewPerformFind(PDFView)](pdfviewdelegate/pdfviewperformfind(_:).md)
  Performs a find operation.
- [func pdfViewPerformGo(toPage: PDFView)](pdfviewdelegate/pdfviewperformgo(topage:).md)
  Performs a go-to operation.
- [func pdfViewPerformPrint(PDFView)](pdfviewdelegate/pdfviewperformprint(_:).md)
  Prints the current document.
- [func pdfViewOpenPDF(PDFView, forRemoteGoToAction: PDFActionRemoteGoTo)](pdfviewdelegate/pdfviewopenpdf(_:forremotegotoaction:).md)
  Opens a specified page.
### Scaling the View
- [func pdfViewWillChangeScaleFactor(PDFView, toScale: CGFloat) -> CGFloat](pdfviewdelegate/pdfviewwillchangescalefactor(_:toscale:).md)
  Overrides changes to the scale factor.
### Linking in a View
- [func pdfViewWillClick(onLink: PDFView, with: URL)](pdfviewdelegate/pdfviewwillclick(onlink:with:).md)
  Handle clicks on URL links in a view.
### Printing the View
- [func pdfViewPrintJobTitle(PDFView) -> String](pdfviewdelegate/pdfviewprintjobtitle(_:).md)
  Overrides the job title used when the `PDFView` is printed.
### Instance Methods
- [func pdfViewParentViewController() -> UIViewController](pdfviewdelegate/pdfviewparentviewcontroller.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any PDFViewDelegate)?](pdfview/delegate.md)
  Returns the view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfviewdelegate)*