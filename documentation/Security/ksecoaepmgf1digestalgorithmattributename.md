# kSecOAEPMGF1DigestAlgorithmAttributeName

**Framework**: Security  
**Kind**: var

The OAEP MGF1 digest algorithm.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecOAEPMGF1DigestAlgorithmAttributeName: CFString
```

#### Discussion

Set this value to one of the digest algorithms listed in [`Digest Types`](transform-attributes#Digest-Types.md) when the [`kSecPaddingKey`](ksecpaddingkey.md) attribute is set to [`kSecPaddingOAEPKey`](ksecpaddingoaepkey.md). If you don’t set this attribute, [`kSecDigestSHA1`](ksecdigestsha1.md) is used by default.

This attribute is ignored when padding is not set to OAEP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecoaepmgf1digestalgorithmattributename)*