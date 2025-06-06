# kSecOAEPEncodingParametersAttributeName

**Framework**: Security  
**Kind**: var

The OAEP encoding parameters.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecOAEPEncodingParametersAttributeName: CFString
```

#### Discussion

Set this value to a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object when the [`kSecPaddingKey`](ksecpaddingkey.md) attribute is set to [`kSecPaddingOAEPKey`](ksecpaddingoaepkey.md). If you don’t set this attribute, a zero length data object is used by default.

This attribute is ignored when padding is not set to OAEP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecoaepencodingparametersattributename)*