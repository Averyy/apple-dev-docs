# PDFActionURL

**Framework**: PDFKit  
**Kind**: class

`PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFActionURL
```

## Topics

### Initializing a URL Action
- [init(url: URL)](pdfactionurl/init(url:)-5wtb3.md)
  Initializes a URL action with the specified URL.
### Accessing and Changing the URL
- [var url: URL?](pdfactionurl/url.md)
  Returns the URL associated with the URL action.
### Initializers
- [init(URL: URL)](pdfactionurl/init(url:)-1e0qw.md)

## Relationships

### Inherits From
- [PDFAction](pdfaction.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class PDFActionGoTo](pdfactiongoto.md)
  `PDFActionGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action.
- [class PDFActionNamed](pdfactionnamed.md)
  `PDFActionNamed` defines methods used to work with actions in PDF documents, some of which are named in the Adobe PDF Specification.
- [class PDFActionRemoteGoTo](pdfactionremotegoto.md)
  `PDFActionRemoteGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action that targets another document.
- [class PDFActionResetForm](pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.
- [enum PDFActionNamedName](pdfactionnamedname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionurl)*