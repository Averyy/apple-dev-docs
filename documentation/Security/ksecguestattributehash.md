# kSecGuestAttributeHash

**Framework**: Security  
**Kind**: var

A key whose value is a data object containing the SHA-1 hash of the code directory.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecGuestAttributeHash: CFString
```

#### Discussion

This hash can be used as a unique identifier to recognize this specific code in the future. This identifier is tied to the current version of the code, unlike the [`kSecCodeInfoIdentifier`](kseccodeinfoidentifier.md) identifier, which remains stable across developer-approved updates. If you are not passing this hash in the attribute dictionary when you call the [`SecHostCreateGuest`](sechostcreateguest.md) function, then you must pass the [`kSecCSGenerateGuestHash`](kseccsgenerateguesthash.md) flag to the function as well.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecguestattributehash)*