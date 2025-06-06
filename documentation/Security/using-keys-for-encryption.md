# Using Keys for Encryption

**Framework**: Security

Perform asymmetric and symmetric encryption and decryption using cryptographic keys.

#### Overview

Cryptography enables secure data exchange through an untrusted channel. One important component of this activity is encryption. A transmitter encodes data on one side of a link, rendering it gibberish to anyone without the key to decode it. The data then passes through the channel—exposed to the world, but meaningless to all but the intended receiver. That receiver, the only holder of the decryption key, reverses the encryption process to reveal the original message.

As with cryptographic keys, there are two main types of encryption:

-  Asymmetric encryption doesn’t require a shared secret. On the other hand, it’s computationally expensive and works only on small, discrete blocks of data. Therefore, it’s most suitable for small transfers when sender and receiver have no established relationship.
-  Symmetric encryption is good for bulk data transfer because it’s computationally efficient and operates on streams of data. But it works only when the transmitter and the receiver share a secret key. So you typically rely on some other technique, such as asymmetric encryption or the Diffie-Hellman key exchange, to share a key and establish a session.

##### Use Asymmetric Encryption

To perform asymmetric encryption, a transmitter encrypts its data with a public key. Only the holder of the matching private key can then decrypt the obscured message. You begin by obtaining a public key that corresponds to your intended recipient’s private key. Depending on the situation, you might read it from your keychain or from a certificate, or you might use one of the other methods described in [`Getting an Existing Key`](getting-an-existing-key.md). However you obtain the key, the kind of encryption you can perform depends on the key itself.

For example, consider a 2048-bit RSA key pair, like the one generated in [`Creating an Asymmetric Key Pair`](generating-new-cryptographic-keys#Creating-an-Asymmetric-Key-Pair.md). Either using a signed certificate or some other trusted (but not necessarily secure) channel, the receiver transfers the public key to the transmitter. The transmitter and receiver then negotiate an appropriate encryption algorithm (or rely on a prearranged one) corresponding to the capabilities of the key pair. In this case, suppose you choose this [`rsaEncryptionOAEPSHA512`](seckeyalgorithm/rsaencryptionoaepsha512.md) algorithm:

This setting specifies RSA encryption, employing the Optimal Asymmetric Encryption Padding (OAEP) scheme using SHA512 hashing. The selected algorithm must suit the key’s capabilities. But rather than trust that the key works with the algorithm, you can explicitly test for compatibility with the [`SecKeyOperationType.encrypt`](seckeyoperationtype/encrypt.md) operation, using the [`SecKeyIsAlgorithmSupported(_:_:_:)`](seckeyisalgorithmsupported(_:_:_:).md) function:

This call might return false if the key were not actually of type RSA or if the `publicKey` reference actually referred to a private key (despite its name). Private keys typically have the [`kSecAttrCanEncrypt`](ksecattrcanencrypt.md) attribute set false, marking them ineligible for encryption.

As an additional check before encrypting, because asymmetric encryption restricts the length of the data that you can encrypt, verify that the data is short enough. For this particular algorithm, the plain text data must be 130 bytes smaller than the key’s block size, as reported by [`SecKeyGetBlockSize(_:)`](seckeygetblocksize(_:).md). You therefore further condition the proceedings on a length test:

Finally, you conduct the encryption with a call to the [`SecKeyCreateEncryptedData(_:_:_:_:)`](seckeycreateencrypteddata(_:_:_:_:).md) function:

Despite the pretests, something may still go wrong with the encryption call. When it does, the function returns `nil` cipher text and produces an error object that indicates the cause of failure. In Objective-C, you transfer ownership of the error object to Automatic Reference Counting (ARC) with a call to doc://com.apple.documentation/documentation/foundation/1587932-cfbridgingrelease and handle the error. In Swift, you convert the optional, unmanaged doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 to a managed [`Error`](https://developer.apple.com/documentation/Swift/Error) and throw it.

Assuming that the encryption succeeds, you send the `cipherText` data object to the receiver through the channel. The receiver then uses its private key to decrypt the data. As described in [`Getting an Existing Key`](getting-an-existing-key.md), you’ll typically get a reference to your private key from either the keychain or an identity (which might itself be stored in the keychain). You can again test the key for its suitability, using the same algorithm as before, but for the [`SecKeyOperationType.decrypt`](seckeyoperationtype/decrypt.md) operation:

You can again test the length, though in this case, the cipher text should be the same length as the key’s block size, because that’s what the encryption operation should have produced:

With the tests out of the way, the decryption proceeds much like the encryption, only now with a call to [`SecKeyCreateDecryptedData(_:_:_:_:)`](seckeycreatedecrypteddata(_:_:_:_:).md):

As before, you handle a failure and the corresponding error object, if applicable. If the call succeeds, the `clearText` object exactly matches the `plainText` object from the transmitter.

##### Use Symmetric Encryption

When the sender and receiver share a single, secret key, they can perform symmetric encryption, in which the same key both encrypts and decrypts the message. Even though the operations in this case are computationally efficient, initially sharing the key poses its own challenge. For that reason, you’ll usually want to use another method, such as asymmetric encryption, to exchange a symmetric key at the time you begin communicating.

In fact, the certificate, key, and trust services API provides a simple way to accomplish this. You follow all of the steps outlined in [`Use Asymmetric Encryption`](using-keys-for-encryption#Use-Asymmetric-Encryption.md), with only the following adjustments:

-  When you choose an algorithm of [`rsaEncryptionOAEPSHA512AESGCM`](seckeyalgorithm/rsaencryptionoaepsha512aesgcm.md) or one of the other symmetric encryption algorithms, the encryption and decryption function calls change their behavior.
-  Because the input data is encrypted by the AES session key, that data is no longer restricted to a particular length. Similarly, the block of encrypted data is no longer expected to be the key’s block size. In fact, it’s the key’s block size plus the (variable) length of the encrypted data plus 16 bytes.

On the encryption side, instead of simply padding and encoding the given block of data with the key, the [`SecKeyCreateEncryptedData(_:_:_:_:)`](seckeycreateencrypteddata(_:_:_:_:).md) function first generates a random Advanced Encryption Standard (AES) session key. It uses this key to encrypt the input data, and then RSA encrypts the AES key using the input public key you provide. It finally assembles the RSA encrypted session key, the AES encrypted data, and a 16-byte AES-GCM tag into a block of data that it returns to you.

On the decryption side, the process is reversed. The function decrypts the AES session key using the private key you provide as input and then uses that to decrypt the data.

If you use elliptic curve keys, then use one of the elliptic curve algorithms, such as [`eciesEncryptionCofactorX963SHA256AESGCM`](seckeyalgorithm/eciesencryptioncofactorx963sha256aesgcm.md). The precise details of this key exchange are different, compared with the RSA exchange described above. Still, the effective behavior you see as a consumer of the API is the same.

With these small changes, you switch from asymmetric encryption to symmetric encryption supported by asymmetric encryption. You can now efficiently transmit arbitrarily large blocks of encrypted data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/using-keys-for-encryption)*