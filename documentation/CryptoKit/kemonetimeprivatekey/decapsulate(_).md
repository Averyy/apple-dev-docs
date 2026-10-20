# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Recovers a shared secret from an encapsulated representation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
consuming func decapsulate(_ encapsulated: Data) throws -> SymmetricKey
```

#### Return Value

The decapsulated shared secret.

## Parameters

- `encapsulated`: The encapsulated shared secret that someone created using this key’s [`publicKey`](kemonetimeprivatekey/publickey-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey/decapsulate(_:))*