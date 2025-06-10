# kSecAttrTokenIDSecureEnclave

**Framework**: Security  
**Kind**: var

Specifies an item should be stored in the device’s Secure Enclave.

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

The only keychain items supported by the Secure Enclave are 256-bit elliptic curve private keys (those that have key type [`kSecAttrKeyTypeEC`](ksecattrkeytypeec.md)). Such keys must be generated directly on the Secure Enclave using the [`SecKeyGeneratePair(_:_:_:)`](seckeygeneratepair(_:_:_:).md) function with the [`kSecAttrTokenID`](ksecattrtokenid.md) key set to [`kSecAttrTokenIDSecureEnclave`](ksecattrtokenidsecureenclave.md) in the parameters dictionary.

> ❗ **Important**:  It is not possible to import pre-existing keys into the Secure Enclave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave)*