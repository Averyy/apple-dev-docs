# kSecCodeInfoFormat

**Framework**: Security  
**Kind**: var

A key whose value is a string representing the type and format of the code in a form suitable for display to a knowledgeable user.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoFormat: CFString
```

#### Discussion

The value is a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) object.

This is generic information returned regardless of which [`Code Signing Information Flags`](code-signing-information-flags.md)  you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoformat)*