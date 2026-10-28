# setSigningPublicKey(_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method

Sets the signing public key that the context requires to unlock a signed archive.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func setSigningPublicKey(_ key: P256.Signing.PublicKey) throws
```

## Discussion

The public signing key is necessary to unlock a signed archive. If you don’t provide a private key when you create a new archive, provide a public key to tie the encryption to the signing identity. In this case, you need to sign the archive offline using the corresponding signing private key.

## Parameters

- `key`: The recipient public key.

## See Also

### Setting and retrieving keys
- [var mainKey: SymmetricKey?](./mainkey.md)
  The main key used to append data to an existing archive.
- [var symmetricKey: SymmetricKey?](./symmetrickey.md)
  The symmetric encryption key used to encrypt or decrypt an archive.
- [func generateSymmetricKey() throws -> SymmetricKey](./generatesymmetrickey%28%29.md)
  Generates a symmetric encryption key.
- [func setSymmetricKey(SymmetricKey) throws](./setsymmetrickey%28_%29.md)
  Sets the symmetric encryption key that the context requires for symmetric encryption mode.
- [func setRecipientPrivateKey(P256.KeyAgreement.PrivateKey) throws](./setrecipientprivatekey%28_%29.md)
  Sets the recipient private key that the context requires to decrypt an archive to a specific recipient in ECDHE encryption profiles.
- [func setSigningPrivateKey(P256.Signing.PrivateKey) throws](./setsigningprivatekey%28_%29.md)
  Sets the signing private key that corresponds to the signing public key that you used to create the archive.
- [func setRecipientPublicKey(P256.KeyAgreement.PublicKey) throws](./setrecipientpublickey%28_%29.md)
  Sets the recipient public key that the context requires to encrypt an archive to a specific recipient in ECDHE encryption profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/setsigningpublickey(_:))*