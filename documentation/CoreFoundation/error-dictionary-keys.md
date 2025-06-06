# Error Dictionary Keys

**Framework**: Core Foundation

The keys used in an error dictionary returned by some functions to provide more information about XML parse errors.

#### Overview

These keys are used in the error dictionary returned by the [`CFXMLTreeCreateFromDataWithError`](cfxmltreecreatefromdatawitherror.md) function.

## Topics

### Constants
- [let kCFXMLTreeErrorDescription: CFString!](kcfxmltreeerrordescription.md)
  Dictionary key whose value is a CFString containing a readable description of the error.
- [let kCFXMLTreeErrorLineNumber: CFString!](kcfxmltreeerrorlinenumber.md)
  Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.
- [let kCFXMLTreeErrorLocation: CFString!](kcfxmltreeerrorlocation.md)
  Dictionary key whose value is a CFNumber containing the byte location where the error was detected.
- [let kCFXMLTreeErrorStatusCode: CFString!](kcfxmltreeerrorstatuscode.md)
  Dictionary key whose value is a CFNumber containing the error status code. See [`CFXMLParser`](cfxmlparser.md) for possible status code values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/error-dictionary-keys)*