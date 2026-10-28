# PDFActionNamed

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface PDFActionNamed : PDFAction
```

## Overview

A `PDFActionNamed` object represents an action with a defined name, such as “Go back” or “Zoom in.”

## Topics

### Accessing the Name of the Action
- [var name: PDFActionNamedName](./pdfactionnamed/name.md)
  Returns the name of the named action.
### Initializing the Action
- [init(name: PDFActionNamedName)](./pdfactionnamed/init%28name%29.md)
  Initializes the `PDFActionName` object with the specified named action.

## Relationships

### Inherits From
- [PDFAction](./pdfaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Action Types
- [class PDFActionGoTo](./pdfactiongoto.md)
  `PDFActionGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action.
- [class PDFActionRemoteGoTo](./pdfactionremotegoto.md)
  `PDFActionRemoteGoTo`, a subclass of `PDFAction`, defines methods for getting and setting the destination of a go-to action that targets another document.
- [class PDFActionResetForm](./pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.
- [class PDFActionURL](./pdfactionurl.md)
  `PDFActionURL`, a subclass of `PDFAction`, defines methods for getting and setting the URL associated with a URL action.
- [enum PDFActionNamedName](./pdfactionnamedname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionnamed)*