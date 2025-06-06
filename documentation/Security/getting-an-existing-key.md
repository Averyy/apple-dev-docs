# Getting an Existing Key

**Framework**: Security

Learn how to obtain an existing cryptographic key.

#### Overview

The Security framework defines the [`SecKey`](seckey.md) opaque type to hold key objects. You typically use a key reference to indicate the key to use for a particular cryptographic operation, such as encryption. How you get a key reference depends on where the key is stored. In particular, the source of a key might be one of the following:

-  When you read an identity from a password-protected file or from the keychain, you can extract the private key it contains, as described in [`Parsing an Identity`](parsing-an-identity.md). In macOS, you can also store a private key in an identity, along with its certificate, as described in [`Creating an Identity`](creating-an-identity.md).
-  When you have a trust object, as described in [`Evaluating a Trust and Parsing the Result`](evaluating-a-trust-and-parsing-the-result.md), you can extract the associated certificate’s public key with a call to [`SecTrustCopyPublicKey(_:)`](sectrustcopypublickey(_:).md):

-  When you have a private key, you can calculate the associated public key with the [`SecKeyCopyPublicKey(_:)`](seckeycopypublickey(_:).md) function:

-  You can export a key as a data blob that you can store on disk or send to someone else. Your app or another process can then do the reverse and restore the key from the data, possibly at a later time. See [`Storing Keys as Data`](storing-keys-as-data.md) for more details.
-  You can place a key in a keychain to securely store it for later use. See [`Storing Keys in the Keychain`](storing-keys-in-the-keychain.md) for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/getting-an-existing-key)*