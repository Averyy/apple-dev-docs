# Generating New Cryptographic Keys

**Framework**: Security

Create both asymmetric and symmetric cryptographic keys.

#### Overview

Very often, you retrieve a key from an identity, a certificate, or the keychain, or with some other method described in [`Getting an Existing Key`](getting-an-existing-key.md). Sometimes, however, you need to create your own keys.

##### Creating an Asymmetric Key Pair

An asymmetric cryptographic key pair is composed of a public and a private key that are generated together. You distribute the public key freely, but you keep the private key secret. One or both may be stored in a keychain for safekeeping.

You create an asymmetric key pair by first creating an attributes dictionary:

At a minimum, you specify the type and size of keys to create using the [`kSecAttrKeyType`](ksecattrkeytype.md) and [`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md) parameters, respectively. The above example indicates 2048-bit RSA keys, though other options are available.

You then optionally add a [`kSecPrivateKeyAttrs`](ksecprivatekeyattrs.md) parameter with a subdictionary that characterizes the private key. By assigning a value of [`true`](https://developer.apple.com/documentation/swift/true) to the private key’s [`kSecAttrIsPermanent`](ksecattrispermanent.md) attribute, you store it in the default keychain while creating it. You also specify the [`kSecAttrApplicationTag`](ksecattrapplicationtag.md) attribute with a unique [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) value so that you can find and retrieve it from the keychain later. The tag data is constructed from a string, using reverse DNS notation, though any unique tag will do.

You could add a [`kSecPublicKeyAttrs`](ksecpublickeyattrs.md) attribute to the attributes dictionary, specifying a distinct tag and keychain storage for the public key. However, it’s typically easier to store only the private key and then generate the public key from it when needed. That way you don’t need to keep track of another tag or clutter your keychain.

For a complete list of available key attributes, see [`Key Generation Attributes`](key-generation-attributes.md).

> **Note**:  Be sure that you don’t generate multiple, identically tagged keys. These are difficult to tell apart during retrieval, unless they differ in some other, searchable characteristic. Instead, use a unique tag for each key generation operation, or delete old keys with a given tag using [`SecItemDelete(_:)`](secitemdelete(_:).md) before creating a new one with that tag.

 Be sure that you don’t generate multiple, identically tagged keys. These are difficult to tell apart during retrieval, unless they differ in some other, searchable characteristic. Instead, use a unique tag for each key generation operation, or delete old keys with a given tag using [`SecItemDelete(_:)`](secitemdelete(_:).md) before creating a new one with that tag.

You then call the [`SecKeyCreateRandomKey(_:_:)`](seckeycreaterandomkey(_:_:).md) function with the attributes dictionary:

If the function fails to create a key, as indicated by a `NULL` return value, it fills in the `error` parameter to indicate the reason for failure. Otherwise, the key reference points to a new private key that’s ready for use. The key is also stored in the default keychain, from where you can read it later, as described in [`Storing Keys in the Keychain`](storing-keys-in-the-keychain.md). If you need the corresponding public key (now or later), call the [`SecKeyCopyPublicKey(_:)`](seckeycopypublickey(_:).md) function with the private key reference:

In Objective-C, when you’re done with these key references, however you obtained them, you are responsible for releasing the associated memory:

```objc
if (publicKey)  { CFRelease(publicKey);  }
if (privateKey) { CFRelease(privateKey); }
```

##### Creating a Symmetric Key

Asymmetric key cryptography is useful because it enables secure communication between two players who don’t share a secret ahead of time. However, it’s not ideal for bulk data transfer, because it’s computationally expensive and because it operates on small, fixed-sized chunks of data. Symmetric key cryptography, on the other hand, is computationally efficient. It allows you to handle data streams of arbitrary length but requires that both sender and receiver, and no one else, know the secret key.

To get the best of both worlds, you often use asymmetric cryptography to communicate a symmetric cryptographic key that you then use for bulk data transfer. When you do this with the certificate, key, and trust services API, you don’t explicitly create the symmetric key yourself. Instead, you call [`SecKeyCreateEncryptedData(_:_:_:_:)`](seckeycreateencrypteddata(_:_:_:_:).md) to create a symmetric key for you. This function creates the symmetric key, uses it to encrypt your data, and then encrypts the key itself with the public key that you provide. It then packages all of this data together and returns it to you. You then transmit it to a receiver, who uses the corresponding private key in a call to [`SecKeyCreateDecryptedData(_:_:_:_:)`](seckeycreatedecrypteddata(_:_:_:_:).md) to reverse the operation. For more details, see [`Using Keys for Encryption`](using-keys-for-encryption.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/generating-new-cryptographic-keys)*