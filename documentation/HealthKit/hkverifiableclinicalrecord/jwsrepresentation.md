# jwsRepresentation

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A raw representation of the SMART Health Card’s contents.

**Availability**:
- iOS 15.0+ - Deprecated in 15.4
- iPadOS 15.0+ - Deprecated in 15.4
- Mac Catalyst 15.0+ - Deprecated in 15.4
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`dataRepresentation`](./datarepresentation.md) instead.

## Declaration

```swift
var jwsRepresentation: Data { get }
```

```objc
@property (copy, readonly) NSData * JWSRepresentation;
```

#### Discussion

This property contains a JSON Web Signature (JWS) Compact Serialization of the card. The data is cryptographically signed by the issuer, and compressed.

> ❗ **Important**:  To ensure that the data is authentic and that no one has tampered with it, decompress the data and then use a public key from the issuer to verify their signature.

## See Also

### Accessing the Raw Payload
- [var dataRepresentation: Data](./datarepresentation.md)
  A raw representation of the record’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/jwsrepresentation)*