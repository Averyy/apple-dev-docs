# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Recovers a shared secret from an encapsulated representation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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