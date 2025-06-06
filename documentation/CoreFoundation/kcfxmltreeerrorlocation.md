# kCFXMLTreeErrorLocation

**Framework**: Core Foundation  
**Kind**: var

Dictionary key whose value is a CFNumber containing the byte location where the error was detected.

**Availability**:
- macOS ?+

## Declaration

```swift
let kCFXMLTreeErrorLocation: CFString!
```

## See Also

- [let kCFXMLTreeErrorDescription: CFString!](kcfxmltreeerrordescription.md)
  Dictionary key whose value is a CFString containing a readable description of the error.
- [let kCFXMLTreeErrorLineNumber: CFString!](kcfxmltreeerrorlinenumber.md)
  Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.
- [let kCFXMLTreeErrorStatusCode: CFString!](kcfxmltreeerrorstatuscode.md)
  Dictionary key whose value is a CFNumber containing the error status code. See [`CFXMLParser`](cfxmlparser.md) for possible status code values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfxmltreeerrorlocation)*