# PKCS1SHA384

**Framework**: Security  
**Kind**: property

Data to be signed is a SHA384 hash.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static var PKCS1SHA384: SecPadding { get }
```

#### Discussion

Standard ASN.1 padding will be done, as well as PKCS1 padding of the underlying RSA operation. Used with [`SecKeyRawSign(_:_:_:_:_:_:)`](seckeyrawsign(_:_:_:_:_:_:).md) and [`SecKeyRawVerify(_:_:_:_:_:_:)`](seckeyrawverify(_:_:_:_:_:_:).md) only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpadding/pkcs1sha384)*