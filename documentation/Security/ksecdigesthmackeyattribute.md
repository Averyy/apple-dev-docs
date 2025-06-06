# kSecDigestHMACKeyAttribute

**Framework**: Security  
**Kind**: var

The key for HMAC operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecDigestHMACKeyAttribute: CFString
```

#### Discussion

The value is a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object that specifies the key when [`kSecDigestTypeAttribute`](ksecdigesttypeattribute.md) attribute is set to one of the HMAC options listed in [`Digest Types`](transform-attributes#Digest-Types.md). If this value is not set, the transform will assume a zero length key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecdigesthmackeyattribute)*