# kSecCodeInfoDigestAlgorithms

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a list of the kinds of cryptographic hash functions available within the signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoDigestAlgorithms: CFString
```

```c
extern CFStringRef const kSecCodeInfoDigestAlgorithms;
```

#### Discussion

The value is a [`CFArray`](../CoreFoundation/cfarray.md) of [`CFNumber`](../CoreFoundation/cfnumber.md) objects indicating the kinds of cryptographic hash functions available within the signature. The ordering of the items in the array has no significance in terms of priority, but determines the order in which the hashes appear in [`kSecCodeInfoCdHashes`](./kseccodeinfocdhashes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithms)*