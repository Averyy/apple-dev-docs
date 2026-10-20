# kCFXMLTreeErrorDescription

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

Dictionary key whose value is a CFString containing a readable description of the error.

**Availability**:
- macOS

## Declaration

```swift
let kCFXMLTreeErrorDescription: CFString!
```

```c
extern CFStringRef const kCFXMLTreeErrorDescription;
```

## See Also

### Constants
- [let kCFXMLTreeErrorLineNumber: CFString!](./kcfxmltreeerrorlinenumber.md)
  Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.
- [let kCFXMLTreeErrorLocation: CFString!](./kcfxmltreeerrorlocation.md)
  Dictionary key whose value is a CFNumber containing the byte location where the error was detected.
- [let kCFXMLTreeErrorStatusCode: CFString!](./kcfxmltreeerrorstatuscode.md)
  Dictionary key whose value is a CFNumber containing the error status code. See [`CFXMLParser`](./cfxmlparser.md) for possible status code values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfxmltreeerrordescription)*