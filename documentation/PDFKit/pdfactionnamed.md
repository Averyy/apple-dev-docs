# PDFActionNamed

**Framework**: PDFKit  
**Kind**: class

`PDFActionNamed` defines methods used to work with actions in PDF documents, some of which are named in the Adobe PDF Specification.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFActionNamed
```

#### Overview

A `PDFActionNamed` object represents an action with a defined name, such as “Go back” or “Zoom in.”

## Topics

### Accessing the Name of the Action
- [var name: PDFActionNamedName](pdfactionnamed/name.md)
  Returns the name of the named action.
### Initializing the Action
- [init(name: PDFActionNamedName)](pdfactionnamed/init(name:).md)
  Initializes the `PDFActionName` object with the specified named action.

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
- [class PDFActionRemoteGoTo](pdfactionremotegoto.md)
  `PDFActionRemoteGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action that targets another document.
- [class PDFActionResetForm](pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.
- [class PDFActionURL](pdfactionurl.md)
  `PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.
- [enum PDFActionNamedName](pdfactionnamedname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionnamed)*