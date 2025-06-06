# kSecCodeInfoDigestAlgorithm

**Framework**: Security  
**Kind**: var

A key whose value is a number indicating the cryptographic hash function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoDigestAlgorithm: CFString
```

#### Discussion

The value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) indicating the kind of cryptographic hash function used within the signature to seal its pieces together. See [`SecCSDigestAlgorithm`](seccsdigestalgorithm.md) for possible value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithm)*