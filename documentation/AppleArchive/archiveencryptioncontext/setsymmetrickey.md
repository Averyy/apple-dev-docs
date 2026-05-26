# setSymmetricKey(_:)

**Framework**: Apple Archive  
**Kind**: method

Sets the symmetric encryption key that the context requires for symmetric encryption mode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func setSymmetricKey(_ key: SymmetricKey) throws
```

#### Discussion

Use this function to set the encryption key for a context with a symmetric [`profile`](archiveencryptioncontext/profile-swift.property.md).

## Parameters

- `key`: The symmetric encryption key.

## See Also

- [struct SymmetricKey](../CryptoKit/SymmetricKey.md)
  A symmetric cryptographic key.
- [var mainKey: SymmetricKey?](archiveencryptioncontext/mainkey.md)
  The main key used to append data to an existing archive.
- [var symmetricKey: SymmetricKey?](archiveencryptioncontext/symmetrickey.md)
  The symmetric encryption key used to encrypt or decrypt an archive.
- [func generateSymmetricKey() throws -> SymmetricKey](archiveencryptioncontext/generatesymmetrickey.md)
  Generates a symmetric encryption key.
- [func setRecipientPrivateKey(P256.KeyAgreement.PrivateKey) throws](archiveencryptioncontext/setrecipientprivatekey(_:).md)
  Sets the recipient private key that the context requires to decrypt an archive to a specific recipient in ECDHE encryption profiles.
- [func setSigningPrivateKey(P256.Signing.PrivateKey) throws](archiveencryptioncontext/setsigningprivatekey(_:).md)
  Sets the signing private key that corresponds to the signing public key that you used to create the archive.
- [func setRecipientPublicKey(P256.KeyAgreement.PublicKey) throws](archiveencryptioncontext/setrecipientpublickey(_:).md)
  Sets the recipient public key that the context requires to encrypt an archive to a specific recipient in ECDHE encryption profiles.
- [func setSigningPublicKey(P256.Signing.PublicKey) throws](archiveencryptioncontext/setsigningpublickey(_:).md)
  Sets the signing public key that the context requires to unlock a signed archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/setsymmetrickey(_:))*