# kSecPaddingOAEPKey

**Framework**: Security  
**Kind**: var

PKCS7 padding will be used when encrypting or decrypting.

**Availability**:
- macOS 10.8+

## Declaration

```swift
let kSecPaddingOAEPKey: CFString
```

#### Discussion

When using this padding type, consider also setting the [`kSecOAEPMessageLengthAttributeName`](ksecoaepmessagelengthattributename.md), [`kSecOAEPEncodingParametersAttributeName`](ksecoaepencodingparametersattributename.md), and [`kSecOAEPMGF1DigestAlgorithmAttributeName`](ksecoaepmgf1digestalgorithmattributename.md) attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecpaddingoaepkey)*