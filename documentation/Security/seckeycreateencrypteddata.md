# SecKeyCreateEncryptedData(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Encrypts a block of data using a public key and specified algorithm.

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
func SecKeyCreateEncryptedData(_ key: SecKey, _ algorithm: SecKeyAlgorithm, _ plaintext: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

## Mentions

- [Using Keys for Encryption](using-keys-for-encryption.md)
- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)

#### Return Value

The encrypted data or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the data’s memory when you are done with it.

#### Discussion

You can decrypt this data with the corresponding private key and a call to [`SecKeyCreateDecryptedData(_:_:_:_:)`](seckeycreatedecrypteddata(_:_:_:_:).md).

## Parameters

- `key`: The public key to use to perform the encryption.
- `algorithm`: The encryption algorithm to use. Use one of the encryption algorithms listed in  . You can use the   function to test that the key is suitable for the algorithm.
- `plaintext`: The data to be encrypted.
- `error`: The address of a   object. If an error occurs, this is set to point at an error instance that describes the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreateencrypteddata(_:_:_:_:))*