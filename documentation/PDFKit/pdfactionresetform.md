# PDFActionResetForm

**Framework**: PDFKit  
**Kind**: class

`PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFActionResetForm
```

#### Overview

A `PDFActionResetForm` object represents an action associated with a PDF form.

## Topics

### Initializing a Reset Form Action
- [init()](pdfactionresetform/init.md)
  Initializes a reset form action.
### Accessing and Changing Fields
- [var fields: [String]?](pdfactionresetform/fields.md)
  Returns an array of fields associated with the reset action.
### Determining Whether Fields are Cleared When the Action is Performed
- [var fieldsIncludedAreCleared: Bool](pdfactionresetform/fieldsincludedarecleared.md)
  Sets whether the fields associated with the reset action are cleared when the action is performed.

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
- [class PDFActionRemoteGoTo](pdfactionremotegoto.md)
  `PDFActionRemoteGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action that targets another document.
- [class PDFActionURL](pdfactionurl.md)
  `PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.
- [enum PDFActionNamedName](pdfactionnamedname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionresetform)*