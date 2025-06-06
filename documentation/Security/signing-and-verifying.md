# Signing and Verifying

**Framework**: Security

Create and evaluate digital signatures to establish the validity of code or data.

#### Overview

You create a cryptographic signature on a block of data by first creating a hash of the data and then encrypting this digest with your private key. A recipient uses your public key to decrypt the signature, while independently re-creating the hash of the original data. If the decrypted hash and the computed one match, the recipient can be sure the data is from the owner of the private key that corresponds to the public key.

Often, you sign a block of data as a side effect of performing some other operation. For example, as a final step in distributing your app, Xcode signs the code on your behalf using one of your cryptographic identities (see [`Code Signing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929)). When you want to sign or verify a block of data in your app, you use functions provided by the certificate, key, and trust services API.

##### Get Your Private Key

Begin by getting your private key, as described in [`Getting an Existing Key`](getting-an-existing-key.md), either from the keychain or from an identity (which itself probably resides in the keychain). Then, select one of the signing algorithms. For example:

This algorithm indicates that the signing function should first create an SHA-512 digest of the input data and then use RSA encryption with PKCS#1 padding. But you can choose different options, along a number of dimensions:

-  If you already have a digest of the data, you can use one of the `Digest` algorithms. For example, the above algorithm might become [`rsaSignatureDigestPKCS1v15SHA512`](seckeyalgorithm/rsasignaturedigestpkcs1v15sha512.md). If you do this, be sure that the actual hashing matches the named hashing algorithm.
-  If you have elliptic curve keys instead of RSA, you can use an Elliptic Curve Digital Signature Algorithm (ECDSA). For example, the above algorithm might become [`ecdsaSignatureMessageX962SHA512`](seckeyalgorithm/ecdsasignaturemessagex962sha512.md).

With a key and an algorithm selected, you can test the compatibility of these with the signing operation using the [`SecKeyIsAlgorithmSupported(_:_:_:)`](seckeyisalgorithmsupported(_:_:_:).md) function:

This function might return [`false`](https://developer.apple.com/documentation/swift/false), for example, if the key’s [`kSecAttrCanSign`](ksecattrcansign.md) attribute is set to [`false`](https://developer.apple.com/documentation/swift/false). This situation might happen if you used a public key instead of a private one (despite the variable name). Similarly, if you attempt to use an RSA key with one of the ECDSA algorithms, the check fails.

Finally, you can create the signature with a call to the [`SecKeyCreateSignature(_:_:_:_:)`](seckeycreatesignature(_:_:_:_:).md) function:

If something goes wrong, the function returns a `nil` signature and populates the error reference with a doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 object that explains the failure. In Objective-C, you transfer management of the error object, if it exists, to Automatic Reference Counting (ARC). In Swift, you transfer control of this unmanaged object’s memory to the system with a call to [`takeRetainedValue()`](https://developer.apple.com/documentation/Swift/Unmanaged/takeRetainedValue()) and recast as an [`Error`](https://developer.apple.com/documentation/Swift/Error).

##### Transmit the Data

After you successfully generate a signature, you transmit the data and signature to any interested party. Using your public key, the recipient then verifies the signature by performing a set of operations that resemble the signing process. As the receiver, you first retrieve the public key, possibly from a certificate, as described in [`Getting an Existing Key`](getting-an-existing-key.md). Then, using the same algorithm as was used for signing, you test that the key and algorithm are mutually compatible with the verification operation:

The [`SecKeyIsAlgorithmSupported(_:_:_:)`](seckeyisalgorithmsupported(_:_:_:).md) function returns [`false`](https://developer.apple.com/documentation/swift/false) if you use the wrong kind of key for the operation or algorithm. You then conduct the verification with a call to the [`SecKeyVerifySignature(_:_:_:_:_:)`](seckeyverifysignature(_:_:_:_:_:).md) function:

If the call succeeds and the signature and data are intact, the return value is [`true`](https://developer.apple.com/documentation/swift/true). If the function returns [`false`](https://developer.apple.com/documentation/swift/false), either the data or signature has been altered, the public key doesn’t match the private key, or some other error has occurred. Handle the error and transfer error object ownership to the system as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/signing-and-verifying)*