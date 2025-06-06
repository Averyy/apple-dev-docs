# kSecCodeInfoCdHashes

**Framework**: Security  
**Kind**: var

A key whose value is an array containing the unique binary identifier for every digest algorithm supported in the signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoCdHashes: CFString
```

#### Discussion

The corresponding [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) contains the values of the [`kSecCodeInfoUnique`](kseccodeinfounique.md) binary identifier for every digest algorithm supported in the signature in the same order as in the [`kSecCodeInfoDigestAlgorithms`](kseccodeinfodigestalgorithms.md) array. The [`kSecCodeInfoUnique`](kseccodeinfounique.md) value contained in this array corresponds to the [`kSecCodeInfoDigestAlgorithm`](kseccodeinfodigestalgorithm.md) value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfocdhashes)*