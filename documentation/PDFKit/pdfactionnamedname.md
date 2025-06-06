# PDFActionNamedName

**Framework**: PDFKit  
**Kind**: enum

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PDFActionNamedName
```

## Topics

### Constants
- [PDFActionNamedName.find](pdfactionnamedname/find.md)
  The Find action.
- [PDFActionNamedName.firstPage](pdfactionnamedname/firstpage.md)
  The First Page action.
- [PDFActionNamedName.goBack](pdfactionnamedname/goback.md)
  The Go Back action.
- [PDFActionNamedName.goForward](pdfactionnamedname/goforward.md)
  The Go Forward action.
- [PDFActionNamedName.goToPage](pdfactionnamedname/gotopage.md)
  The Go to Page action.
- [PDFActionNamedName.lastPage](pdfactionnamedname/lastpage.md)
  The Last Page action.
- [PDFActionNamedName.nextPage](pdfactionnamedname/nextpage.md)
  The Next Page action.
- [PDFActionNamedName.none](pdfactionnamedname/none.md)
  The action has no name.
- [PDFActionNamedName.previousPage](pdfactionnamedname/previouspage.md)
  The Previous Page action.
- [PDFActionNamedName.print](pdfactionnamedname/print.md)
  The Print action.
- [PDFActionNamedName.zoomIn](pdfactionnamedname/zoomin.md)
  The Zoom In action.
- [PDFActionNamedName.zoomOut](pdfactionnamedname/zoomout.md)
  The Zoom Out action.
### Initializers
- [init?(rawValue: Int)](pdfactionnamedname/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class PDFActionGoTo](pdfactiongoto.md)
  `PDFActionGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action.
- [class PDFActionNamed](pdfactionnamed.md)
  `PDFActionNamed` defines methods used to work with actions in PDF documents, some of which are named in the Adobe PDF Specification.
- [class PDFActionRemoteGoTo](pdfactionremotegoto.md)
  `PDFActionRemoteGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action that targets another document.
- [class PDFActionResetForm](pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.
- [class PDFActionURL](pdfactionurl.md)
  `PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionnamedname)*