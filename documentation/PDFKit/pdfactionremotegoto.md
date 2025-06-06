# PDFActionRemoteGoTo

**Framework**: PDFKit  
**Kind**: class

`PDFActionRemoteGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action that targets another document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFActionRemoteGoTo
```

## Topics

### Initializing the Remote Go-to Action
- [init(pageIndex: Int, at: CGPoint, fileURL: URL)](pdfactionremotegoto/init(pageindex:at:fileurl:).md)
  Initializes the remote go-to action with the specified page index, point, and document URL.
### Accessing the Page Index of the Referenced Document
- [var pageIndex: Int](pdfactionremotegoto/pageindex.md)
  Returns the zero-based page index referenced by the remote go-to action.
### Accessing a Point on the Referenced Page
- [var point: CGPoint](pdfactionremotegoto/point.md)
  Sets the point, in page space, on the page referenced by the remote go-to action.
### Accessing the URL of the Referenced Document
- [var url: URL](pdfactionremotegoto/url.md)
  Returns the URL of the document referenced by the remote go-to action.

## Relationships

### Inherits From
- [PDFAction](pdfaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PDFActionGoTo](pdfactiongoto.md)
  `PDFActionGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action.
- [class PDFActionNamed](pdfactionnamed.md)
  `PDFActionNamed` defines methods used to work with actions in PDF documents, some of which are named in the Adobe PDF Specification.
- [class PDFActionResetForm](pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.
- [class PDFActionURL](pdfactionurl.md)
  `PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.
- [enum PDFActionNamedName](pdfactionnamedname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionremotegoto)*