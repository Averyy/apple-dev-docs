# kSecOAEPEncodingParametersAttributeName

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The OAEP encoding parameters.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecOAEPEncodingParametersAttributeName: CFString
```

```c
extern CFStringRef const kSecOAEPEncodingParametersAttributeName;
```

## Discussion

Set this value to a [`CFData`](../CoreFoundation/cfdata.md) object when the [`kSecPaddingKey`](./ksecpaddingkey.md) attribute is set to [`kSecPaddingOAEPKey`](./ksecpaddingoaepkey.md). If you don’t set this attribute, a zero length data object is used by default.

This attribute is ignored when padding is not set to OAEP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecoaepencodingparametersattributename)*