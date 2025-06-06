# ArchiveEncryptionContext

**Framework**: Apple Archive  
**Kind**: class

An object that encapsulates all parameters, keys, and data necessary to open an encrypted archive for both encryption and decryption streams.

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
class ArchiveEncryptionContext
```

## Topics

### Creating an archive encryption context
- [init?(from: ArchiveByteStream)](archiveencryptioncontext/init(from:).md)
  Returns a new encryption context from the specified encrypted stream.
- [init(profile: ArchiveEncryptionContext.Profile, compressionAlgorithm: ArchiveCompression, compressionBlockSize: Int)](archiveencryptioncontext/init(profile:compressionalgorithm:compressionblocksize:).md)
  Returns a new encryption context from the specified profile, compression algorithm, and block size.
### Setting and retrieving keys
- [var mainKey: SymmetricKey?](archiveencryptioncontext/mainkey.md)
  The main key used to append data to an existing archive.
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
### Signing an encryption context
- [static func sign(encryptedStream: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext) throws](archiveencryptioncontext/sign(encryptedstream:encryptioncontext:).md)
  Signs an encrypted archive using the credentials stored in the specified encryption context.
- [var signatureMode: ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.property.md)
  The signature mode, such as an ECDSA Nist P-256 signature.
- [ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.struct.md)
  Constants that describe the signature modes of an encryption context.
### Getting and setting encryption context properties
- [func decryptAttributes() -> Bool](archiveencryptioncontext/decryptattributes.md)
  Validates decryption keys, collects archive attributes, and updates the context with decrypted archive attributes.
- [var archiveIdentifier: Data?](archiveencryptioncontext/archiveidentifier.md)
  An optional set of data that represents the archive identifier.
- [var authData: Data?](archiveencryptioncontext/authdata.md)
  An optional, unencrypted set of data that’s stored in the archive prologue.
- [var checksumMode: ArchiveEncryptionContext.ChecksumMode](archiveencryptioncontext/checksummode-swift.property.md)
  The checksum mode, such as the 256-bit SHA-256 checksum.
- [ArchiveEncryptionContext.ChecksumMode](archiveencryptioncontext/checksummode-swift.struct.md)
  Constants that describe the checksum modes of an encryption context.
- [var containerSize: Int](archiveencryptioncontext/containersize.md)
  The size of the compressed and encrypted archive.
- [var encryptionMode: ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.property.md)
  The encryption mode, such as symmetric key encryption.
- [ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.struct.md)
  Constants that describe the checksum modes of an encryption context.
- [var compressionAlgorithm: ArchiveCompression](archiveencryptioncontext/compressionalgorithm.md)
  The compression algorithm, such as LZFSE.
- [struct ArchiveCompression](archivecompression.md)
  Constants that describe compression algorithms.
- [var compressionBlockSize: Int](archiveencryptioncontext/compressionblocksize.md)
  The compression block size that defines the size of the blocks, in bytes, that the context splits data into.
- [var paddingSize: Int](archiveencryptioncontext/paddingsize.md)
  An integer value that, if not zero, specifies that the size of the final archive is a multiple of the padding size.
- [var profile: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.property.md)
  The profile of the archve.
- [ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct.md)
  Constants that describe the profile of an encryption context.
- [var rawSize: Int](archiveencryptioncontext/rawsize.md)
  The size of the archive raw data.
- [var signatureEncryptionKey: SymmetricKey?](archiveencryptioncontext/signatureencryptionkey.md)
  The signature encryption key that the context requires to sign an encrypted archive.
### Setting a password
- [var password: String?](archiveencryptioncontext/password.md)
  The password used to encrypt or decrypt an archive.
- [func generatePassword() throws -> String](archiveencryptioncontext/generatepassword.md)
  Generates a new password.
- [func setPassword(String) throws](archiveencryptioncontext/setpassword(_:).md)
  Sets the password from the supplied string.

## See Also

- [Encrypting and Decrypting a String](encrypting-and-decrypting-a-string.md)
  Encrypt the contents of a string and save the result to the file system, then decrypt and recreate the string from the archive file using Apple Encrypted Archive.
- [Encrypting and Decrypting a Single File](encrypting-and-decrypting-a-single-file.md)
  Encrypt a single file and save the result to the file system, then decrypt and recreate the original file from the archive file using Apple Encrypted Archive.
- [Encrypting and Decrypting Directories](encrypting-and-decrypting-directories.md)
  Compress and encrypt the contents of an entire directory or decompress and decrypt an archived directory  using Apple Encrypted Archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext)*