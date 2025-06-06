# mainKey

**Framework**: Apple Archive  
**Kind**: property

The main key used to append data to an existing archive.

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
var mainKey: SymmetricKey? { get set }
```

#### Discussion

Use the main key to append data to an existing AEA archive with the [`encryptionStream(appendingTo:encryptionContext:flags:threadCount:)`](archivebytestream/encryptionstream(appendingto:encryptioncontext:flags:threadcount:).md) function.

You can use the original credentials for symmetric key or password encryption. You need this key to reopen archives created with the ECDHE profiles.

The main key can’t be used to open the stream for decryption.

## See Also

- [var symmetricKey: SymmetricKey?](archiveencryptioncontext/symmetrickey.md)
  The symmetric encryption key used to encrypt or decrypt an archive.
- [func generateSymmetricKey() throws -> SymmetricKey](archiveencryptioncontext/generatesymmetrickey.md)
  Generates a symmetric encryption key.
- [func setSymmetricKey(SymmetricKey) throws](archiveencryptioncontext/setsymmetrickey(_:).md)
  Sets the symmetric encryption key that the context requires for symmetric encryption mode.
- [func setRecipientPrivateKey(P256.KeyAgreement.PrivateKey) throws](archiveencryptioncontext/setrecipientprivatekey(_:).md)
  Sets the recipient private key that the context requires to decrypt an archive to a specific recipient in ECDHE encryption profiles.
- [func setSigningPrivateKey(P256.Signing.PrivateKey) throws](archiveencryptioncontext/setsigningprivatekey(_:).md)
  Sets the signing private key that corresponds to the signing public key that you used to create the archive.
- [func setRecipientPublicKey(P256.KeyAgreement.PublicKey) throws](archiveencryptioncontext/setrecipientpublickey(_:).md)
  Sets the recipient public key that the context requires to encrypt an archive to a specific recipient in ECDHE encryption profiles.
- [func setSigningPublicKey(P256.Signing.PublicKey) throws](archiveencryptioncontext/setsigningpublickey(_:).md)
  Sets the signing public key that the context requires to unlock a signed archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/mainkey)*