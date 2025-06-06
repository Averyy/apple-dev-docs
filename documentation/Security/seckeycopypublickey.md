# SecKeyCopyPublicKey(_:)

**Framework**: Security  
**Kind**: func

Gets the public key associated with the given private key.

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
func SecKeyCopyPublicKey(_ key: SecKey) -> SecKey?
```

## Mentions

- [Getting an Existing Key](getting-an-existing-key.md)
- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)
- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)

#### Return Value

The public key corresponding to the given private key. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this key’s memory when you are done with it.

#### Discussion

The returned public key may be `nil` if the app that created the private key didn’t also store the corresponding public key in the keychain, or if the system can’t reconstruct the corresponding public key.

## Parameters

- `key`: The private key for which you want the corresponding public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycopypublickey(_:))*