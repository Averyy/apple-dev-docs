# kSecCodeInfoUnique

**Framework**: Security  
**Kind**: var

A key whose value is a binary number that uniquely identifies static code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoUnique: CFString
```

#### Discussion

The value is a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object. This identifier can be used to recognize this specific code in the future. This identifier is tied to the current version of the code, unlike the [`kSecCodeInfoIdentifier`](kseccodeinfoidentifier.md) identifier, which remains stable across developer-approved updates. The algorithm used for the [`kSecCodeInfoUnique`](kseccodeinfounique.md) identifier may change over time. However, the identifier remains stable for existing, signed code.

This is generic information returned regardless of which [`Code Signing Information Flags`](code-signing-information-flags.md) you pass to the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfounique)*