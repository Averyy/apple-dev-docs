# compressedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

A compressed representation of the public key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var compressedRepresentation: Data { get }
```

## See Also

### Representing the key
- [var rawRepresentation: Data](./rawrepresentation.md)
  A full representation of the public key.
- [var compactRepresentation: Data?](./compactrepresentation.md)
  A compact representation of the public key.
- [var derRepresentation: Data](./derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [var pemRepresentation: String](./pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the public key.
- [var x963Representation: Data](./x963representation.md)
  An ANSI x9.63 representation of the public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/keyagreement/publickey/compressedrepresentation)*