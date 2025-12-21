# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Parses a public key from a serialized representation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init<D>(rawRepresentation: D) throws where D : DataProtocol
```

#### Return Value

The deserialized public key.

## Parameters

- `rawRepresentation`: The public key, in the FIPS 204 standard serialization format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/publickey/init(rawrepresentation:))*