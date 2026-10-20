# PKCS1MD2

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Data to be signed is an MD2 hash.

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
static var PKCS1MD2: SecPadding { get }
```

```c
kSecPaddingPKCS1MD2
```

#### Discussion

Standard ASN.1 padding is done, as well as PKCS1 padding of the underlying RSA operation. Used with [`SecKeyRawSign(_:_:_:_:_:_:)`](../seckeyrawsign%28_,_,_,_,_,_%29.md) and [`SecKeyRawVerify(_:_:_:_:_:_:)`](../seckeyrawverify%28_,_,_,_,_,_%29.md) only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpadding/pkcs1md2)*