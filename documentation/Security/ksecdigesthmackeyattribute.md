# kSecDigestHMACKeyAttribute

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The key for HMAC operation.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecDigestHMACKeyAttribute: CFString
```

```c
extern CFStringRef const kSecDigestHMACKeyAttribute;
```

#### Discussion

The value is a [`CFData`](../CoreFoundation/cfdata.md) object that specifies the key when [`kSecDigestTypeAttribute`](./ksecdigesttypeattribute.md) attribute is set to one of the HMAC options listed in [Digest Types](./transform-attributes.md#Digest-Types). If this value is not set, the transform will assume a zero length key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecdigesthmackeyattribute)*