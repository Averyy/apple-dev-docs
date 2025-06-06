# kSecCodeInfoDigestAlgorithms

**Framework**: Security  
**Kind**: var

A key whose value is a list of the kinds of cryptographic hash functions available within the signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoDigestAlgorithms: CFString
```

#### Discussion

The value is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) of [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) objects indicating the kinds of cryptographic hash functions available within the signature. The ordering of the items in the array has no significance in terms of priority, but determines the order in which the hashes appear in [`kSecCodeInfoCdHashes`](kseccodeinfocdhashes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithms)*