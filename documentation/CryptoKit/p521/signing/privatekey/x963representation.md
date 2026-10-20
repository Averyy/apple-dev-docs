# x963Representation

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

An ANSI x9.63 representation of the private key.

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
var x963Representation: Data { get }
```

## See Also

### Representing the key
- [var rawRepresentation: Data](./rawrepresentation.md)
  A data representation of the private key.
- [var derRepresentation: Data](./derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [var pemRepresentation: String](./pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing/privatekey/x963representation)*