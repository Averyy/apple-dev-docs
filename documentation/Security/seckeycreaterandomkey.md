# SecKeyCreateRandomKey(_:_:)

**Framework**: Security  
**Kind**: func

Generates a new public-private key pair.

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
func SecKeyCreateRandomKey(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Mentions

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md)
- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)

#### Return Value

The newly generated private key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the key when you are done with it.

#### Discussion

To get the associated public key, use [`SecKeyCopyPublicKey(_:)`](seckeycopypublickey(_:).md). [`SecKeyCreateRandomKey(_:_:)`](seckeycreaterandomkey(_:_:).md) fails and returns [`errSecInteractionNotAllowed`](errsecinteractionnotallowed.md) if you call it in the background on iPhone or iPad while the device is locked.

## Parameters

- `parameters`: A dictionary you use to specify the attributes of the generated keys. See   for details.
- `error`: An error reference pointer that   populates with a suitable error instance on failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreaterandomkey(_:_:))*