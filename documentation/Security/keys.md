# Keys

**Framework**: Security

Generate, store, and use cryptographic keys.

#### Overview

Cryptographic keys are strings of bytes that you combine with other data in specialized mathematical operations to enhance security. At the lowest level, this usually means participating in either encryption and decryption or digital signing and verification. You can use these basic operations directly, such as when you encrypt data before sending it through an insecure channel. You also use them implicitly, such as when you verify the digital signature on a certificate as a byproduct of a trust evaluation.

Keys vary based on the operations they support. For example, you use public and private key pairs to perform asymmetric encryption, whereas you use symmetric keys to conduct symmetric encryption. Similarly, one key might work for a 1024-bit RSA algorithm, while another might be suitable for a 256-bit elliptic curve algorithm. Use the functions in this section when you need to handle cryptographic keys.

## Topics

### Essentials
- [Getting an Existing Key](getting-an-existing-key.md)
  Learn how to obtain an existing cryptographic key.
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)
  Store and access cryptographic keys in the keychain.
- [class SecKey](seckey.md)
  An object that represents a cryptographic key.
- [func SecKeyGetTypeID() -> CFTypeID](seckeygettypeid().md)
  Returns the unique identifier of the opaque type to which a key object belongs.
### Key Generation
- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)
  Create both asymmetric and symmetric cryptographic keys.
- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)
  Create an extra layer of security for your private keys.
- [func SecKeyCreateRandomKey(CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](seckeycreaterandomkey(_:_:).md)
  Generates a new public-private key pair.
- [func SecKeyCopyPublicKey(SecKey) -> SecKey?](seckeycopypublickey(_:).md)
  Gets the public key associated with the given private key.
- [Key Generation Attributes](key-generation-attributes.md)
  Use attribute dictionary keys during cryptographic key generation.
### Examining Keys
- [func SecKeyIsAlgorithmSupported(SecKey, SecKeyOperationType, SecKeyAlgorithm) -> Bool](seckeyisalgorithmsupported(_:_:_:).md)
  Returns a Boolean indicating whether a key is suitable for an operation using a certain algorithm.
- [func SecKeyGetBlockSize(SecKey) -> Int](seckeygetblocksize(_:).md)
  Gets the block length associated with a cryptographic key.
- [func SecKeyCopyAttributes(SecKey) -> CFDictionary?](seckeycopyattributes(_:).md)
  Gets the attributes of a given key.
- [struct SecKeyAlgorithm](seckeyalgorithm.md)
  The algorithms that cryptographic keys enable.
- [enum SecKeyOperationType](seckeyoperationtype.md)
  The types of operations that you can use a cryptographic key to perform.
### Import and Export
- [Storing Keys as Data](storing-keys-as-data.md)
  Create an external representation of a key for transmission.
- [func SecKeyCopyExternalRepresentation(SecKey, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seckeycopyexternalrepresentation(_:_:).md)
  Returns an external representation of the given key suitable for the key’s type.
- [func SecKeyCreateWithData(CFData, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](seckeycreatewithdata(_:_:_:).md)
  Restores a key from an external representation of that key.
### Key Exchange
- [func SecKeyCopyKeyExchangeResult(SecKey, SecKeyAlgorithm, SecKey, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seckeycopykeyexchangeresult(_:_:_:_:_:).md)
  Performs the Diffie-Hellman style of key exchange with optional key-derivation steps.
- [struct SecKeyKeyExchangeParameter](seckeykeyexchangeparameter.md)
  The dictionary keys used to specify Diffie-Hellman key exchange parameters.
### Encryption
- [Using Keys for Encryption](using-keys-for-encryption.md)
  Perform asymmetric and symmetric encryption and decryption using cryptographic keys.
- [func SecKeyCreateEncryptedData(SecKey, SecKeyAlgorithm, CFData, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seckeycreateencrypteddata(_:_:_:_:).md)
  Encrypts a block of data using a public key and specified algorithm.
- [func SecKeyCreateDecryptedData(SecKey, SecKeyAlgorithm, CFData, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seckeycreatedecrypteddata(_:_:_:_:).md)
  Decrypts a block of data using a private key and specified algorithm.
### Digital Signatures
- [Signing and Verifying](signing-and-verifying.md)
  Create and evaluate digital signatures to establish the validity of code or data.
- [func SecKeyCreateSignature(SecKey, SecKeyAlgorithm, CFData, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seckeycreatesignature(_:_:_:_:).md)
  Creates the cryptographic signature for a block of data using a private key and specified algorithm.
- [func SecKeyVerifySignature(SecKey, SecKeyAlgorithm, CFData, CFData, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](seckeyverifysignature(_:_:_:_:_:).md)
  Verifies the cryptographic signature of a block of data using a public key and specified algorithm.
### Legacy iOS Key Operations
- [func SecKeyGeneratePair(CFDictionary, UnsafeMutablePointer<SecKey?>?, UnsafeMutablePointer<SecKey?>?) -> OSStatus](seckeygeneratepair(_:_:_:).md)
  Creates an asymmetric key pair.
- [func SecKeyEncrypt(SecKey, SecPadding, UnsafePointer<UInt8>, Int, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Int>) -> OSStatus](seckeyencrypt(_:_:_:_:_:_:).md)
  Encrypts a block of plaintext.
- [func SecKeyDecrypt(SecKey, SecPadding, UnsafePointer<UInt8>, Int, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Int>) -> OSStatus](seckeydecrypt(_:_:_:_:_:_:).md)
  Decrypts a block of ciphertext.
- [func SecKeyRawSign(SecKey, SecPadding, UnsafePointer<UInt8>, Int, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Int>) -> OSStatus](seckeyrawsign(_:_:_:_:_:_:).md)
  Generates a digital signature for a block of data.
- [func SecKeyRawVerify(SecKey, SecPadding, UnsafePointer<UInt8>, Int, UnsafePointer<UInt8>, Int) -> OSStatus](seckeyrawverify(_:_:_:_:_:_:).md)
  Verifies a digital signature.
- [struct SecPadding](secpadding.md)
  The types of padding to use when you create or verify a digital signature.
### Legacy macOS Key Operations
- [func SecKeyGeneratePairAsync(CFDictionary, dispatch_queue_t, SecKeyGeneratePairBlock)](seckeygeneratepairasync(_:_:_:).md)
  Generates a public/private key pair.
- [func SecKeyGenerateSymmetric(CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](seckeygeneratesymmetric(_:_:).md)
  Generates a random symmetric key.
- [func SecKeyCreateFromData(CFDictionary, CFData, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](seckeycreatefromdata(_:_:_:).md)
  Constructs a SecKeyRef object for a symmetric key.
- [func SecKeyDeriveFromPassword(CFString, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](seckeyderivefrompassword(_:_:_:).md)
  Returns a key object in which the key data is derived from a password.
- [func SecKeyWrapSymmetric(SecKey, SecKey, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seckeywrapsymmetric(_:_:_:_:).md)
  Wraps a symmetric key with another key.
- [func SecKeyUnwrapSymmetric(UnsafeMutablePointer<Unmanaged<CFData>?>, SecKey, CFDictionary, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?](seckeyunwrapsymmetric(_:_:_:_:).md)
  Unwraps a wrapped symmetric key.
- [enum SecKeySizes](seckeysizes.md)
  The supported sizes for keys of various common types.
- [struct SecKeyUsage](seckeyusage.md)
  The flags that indicate key usage in the `KeyUsage` extension of a certificate.
- [typealias SecPublicKeyHash](secpublickeyhash.md)
  A container for a 20-byte public key hash.
- [typealias SecKeyGeneratePairBlock](seckeygeneratepairblock.md)
  A block called with the results of a call to [`SecKeyGeneratePairAsync(_:_:_:)`](seckeygeneratepairasync(_:_:_:).md).
- [enum SecCredentialType](seccredentialtype.md)
  The credential type to be returned by [`SecKeyGetCredentials`](seckeygetcredentials.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/keys)*