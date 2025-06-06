# kSecAttrEffectiveKeySize

**Framework**: Security  
**Kind**: var

A key whose value indicates the effective number of bits in a cryptographic key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrEffectiveKeySize: CFString
```

#### Discussion

The corresponding value is of type [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) and indicates the effective number of bits in this cryptographic key. For example, a DES key has a [`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md) of 64, but a [`kSecAttrEffectiveKeySize`](ksecattreffectivekeysize.md) of 56 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattreffectivekeysize)*