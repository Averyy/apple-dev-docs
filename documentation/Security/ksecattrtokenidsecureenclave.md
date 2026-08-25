# kSecAttrTokenIDSecureEnclave

**Framework**: Security  
**Kind**: var

Specifies an item should be protected by the device’s Secure Enclave.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrTokenIDSecureEnclave: CFString
```

## Mentions

- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)

#### Discussion

To generate a new key that’s protected by the Secure Enclave, call [`SecKeyGeneratePair(_:_:_:)`](seckeygeneratepair(_:_:_:).md), setting the [`kSecAttrTokenID`](ksecattrtokenid.md) key in the parameters dictionary to [`kSecAttrTokenIDSecureEnclave`](ksecattrtokenidsecureenclave.md). For an example, see [`Protecting keys with the Secure Enclave`](protecting-keys-with-the-secure-enclave.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave)*