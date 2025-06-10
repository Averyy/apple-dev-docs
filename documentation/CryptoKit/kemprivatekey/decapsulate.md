# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Recovers a shared secret from an encapsulated representation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func decapsulate(_ encapsulated: Data) throws -> SymmetricKey
```

#### Return Value

The decapsulated shared secret.

## Parameters

- `encapsulated`: The encapsulated shared secret that someone created using this key’s  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemprivatekey/decapsulate(_:))*