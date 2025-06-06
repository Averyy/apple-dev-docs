# open(_:using:authenticating:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decrypts the message and verifies the authenticity of both the encrypted message and additional data.

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
static func open<AuthenticatedData>(_ sealedBox: AES.GCM.SealedBox, using key: SymmetricKey, authenticating authenticatedData: AuthenticatedData) throws -> Data where AuthenticatedData : DataProtocol
```

#### Return Value

The original plaintext message that was sealed in the box, as long as the correct key is used and authentication succeeds. The call throws an error if decryption or authentication fail.

## Parameters

- `sealedBox`: The sealed box to open.
- `key`: The cryptographic key that was used to seal the message.
- `authenticatedData`: Additional data that was authenticated.

## See Also

- [static func open(AES.GCM.SealedBox, using: SymmetricKey) throws -> Data](aes/gcm/open(_:using:).md)
  Decrypts the message and verifies its authenticity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/open(_:using:authenticating:))*