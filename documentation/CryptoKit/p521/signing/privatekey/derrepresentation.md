# derRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

A Distinguished Encoding Rules (DER) encoded representation of the private key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var derRepresentation: Data { get }
```

## See Also

### Representing the key
- [var rawRepresentation: Data](./rawrepresentation.md)
  A data representation of the private key.
- [var pemRepresentation: String](./pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the private key.
- [var x963Representation: Data](./x963representation.md)
  An ANSI x9.63 representation of the private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing/privatekey/derrepresentation)*