# kSecPublicKeyAttrs

**Framework**: Security  
**Kind**: var

A key whose value is a dictionary of cryptographic key attributes specific to a public key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
let kSecPublicKeyAttrs: CFString
```

## Mentions

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)

#### Discussion

The corresponding value is a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) containing key-value pairs for attributes specific to the public key to be generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecpublickeyattrs)*