# rawRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

A data representation of the private key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var rawRepresentation: Data { get }
```

## See Also

### Representing the key
- [var derRepresentation: Data](./derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [var pemRepresentation: String](./pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the private key.
- [var x963Representation: Data](./x963representation.md)
  An ANSI x9.63 representation of the private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/privatekey/rawrepresentation)*