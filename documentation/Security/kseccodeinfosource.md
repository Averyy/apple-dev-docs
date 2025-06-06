# kSecCodeInfoSource

**Framework**: Security  
**Kind**: var

The source of the code signature used for the code object in a format suitable for display.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoSource: CFString
```

#### Discussion

The value is a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) object. This string is for display purposes only. Don’t rely on the precise value returned.

This is generic information returned regardless of which [`Code Signing Information Flags`](code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfosource)*