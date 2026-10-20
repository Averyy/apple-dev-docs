# PDFViewDelegate

**Framework**: PDFKit  
**Kind**: protocol  
**Role**: Protocol

The delegate for the `PDFView` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
protocol PDFViewDelegate : NSObjectProtocol
```

```objc
@protocol PDFViewDelegate <NSObject>
```

## Topics

### Working with Annotation Actions
- [func pdfViewPerformFind(PDFView)](./pdfviewdelegate/pdfviewperformfind%28_%29.md)
  Performs a find operation.
- [func pdfViewPerformGo(toPage: PDFView)](./pdfviewdelegate/pdfviewperformgo%28topage%29.md)
  Performs a go-to operation.
- [func pdfViewPerformPrint(PDFView)](./pdfviewdelegate/pdfviewperformprint%28_%29.md)
  Prints the current document.
- [func pdfViewOpenPDF(PDFView, forRemoteGoToAction: PDFActionRemoteGoTo)](./pdfviewdelegate/pdfviewopenpdf%28_,forremotegotoaction%29.md)
  Opens a specified page.
### Scaling the View
- [func pdfViewWillChangeScaleFactor(PDFView, toScale: CGFloat) -> CGFloat](./pdfviewdelegate/pdfviewwillchangescalefactor%28_,toscale%29.md)
  Overrides changes to the scale factor.
### Linking in a View
- [func pdfViewWillClick(onLink: PDFView, with: URL)](./pdfviewdelegate/pdfviewwillclick%28onlink,with%29.md)
  Handle clicks on URL links in a view.
### Printing the View
- [func pdfViewPrintJobTitle(PDFView) -> String](./pdfviewdelegate/pdfviewprintjobtitle%28_%29.md)
  Overrides the job title used when the `PDFView` is printed.
### Instance Methods
- [func pdfViewParentViewController() -> UIViewController](./pdfviewdelegate/pdfviewparentviewcontroller%28%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting the Delegate
- [var delegate: (any PDFViewDelegate)?](./pdfview/delegate.md)
  Returns the view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfviewdelegate)*