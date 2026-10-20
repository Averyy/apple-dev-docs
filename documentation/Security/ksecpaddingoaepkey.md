# kSecPaddingOAEPKey

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

PKCS7 padding will be used when encrypting or decrypting.

**Availability**:
- macOS 10.8+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecPaddingOAEPKey: CFString
```

```c
extern CFStringRef const kSecPaddingOAEPKey;
```

#### Discussion

When using this padding type, consider also setting the [`kSecOAEPMessageLengthAttributeName`](./ksecoaepmessagelengthattributename.md), [`kSecOAEPEncodingParametersAttributeName`](./ksecoaepencodingparametersattributename.md), and [`kSecOAEPMGF1DigestAlgorithmAttributeName`](./ksecoaepmgf1digestalgorithmattributename.md) attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecpaddingoaepkey)*