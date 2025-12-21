# SecKeyCreateDecryptedData(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Decrypts a block of data using a private key and specified algorithm.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SecKeyCreateDecryptedData(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ ciphertext: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Mentions

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)
- [Using Keys for Encryption](using-keys-for-encryption.md)

#### Return Value

The decrypted data or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the data’s memory when you are done with it.

## Parameters

- `key`: The private key to use to perform the decryption.
- `algorithm`: The algorithm that was used to encrypt the data in the first place. Use one of the encryption algorithms listed in  . You can use the   function to test that the key is suitable for the algorithm.
- `ciphertext`: The data, produced with the corresponding public key and a call to the   function, that you want to decrypt.
- `error`: The address of a   object. If an error occurs, this is set to point at an error instance that describes the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreatedecrypteddata(_:_:_:_:))*