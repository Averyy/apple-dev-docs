# kSecCodeInfoCdHashes

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is an array containing the unique binary identifier for every digest algorithm supported in the signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoCdHashes: CFString
```

```c
extern CFStringRef const kSecCodeInfoCdHashes;
```

#### Discussion

The corresponding [`CFArray`](../CoreFoundation/cfarray.md) contains the values of the [`kSecCodeInfoUnique`](./kseccodeinfounique.md) binary identifier for every digest algorithm supported in the signature in the same order as in the [`kSecCodeInfoDigestAlgorithms`](./kseccodeinfodigestalgorithms.md) array. The [`kSecCodeInfoUnique`](./kseccodeinfounique.md) value contained in this array corresponds to the [`kSecCodeInfoDigestAlgorithm`](./kseccodeinfodigestalgorithm.md) value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfocdhashes)*