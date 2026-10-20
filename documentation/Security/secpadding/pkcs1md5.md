# PKCS1MD5

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Data to be signed is an MD5 hash.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.6+ - Deprecated in 12.0
- tvOS 4.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 8.0

> **Deprecated**: Replaced with SecKeyAlgorithm

## Declaration

```swift
static var PKCS1MD5: SecPadding { get }
```

```c
kSecPaddingPKCS1MD5
```

#### Discussion

Standard ASN.1 padding is done, as well as PKCS1 padding of the underlying RSA operation. Used with [`SecKeyRawSign(_:_:_:_:_:_:)`](../seckeyrawsign%28_,_,_,_,_,_%29.md) and [`SecKeyRawVerify(_:_:_:_:_:_:)`](../seckeyrawverify%28_,_,_,_,_,_%29.md) only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpadding/pkcs1md5)*