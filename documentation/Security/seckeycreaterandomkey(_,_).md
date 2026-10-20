# SecKeyCreateRandomKey(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

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

```c
SecKeyRefSecKeyCreateRandomKey(CFDictionaryRef parameters, CFErrorRef*error);
```

## Mentions

- [Generating New Cryptographic Keys](./generating-new-cryptographic-keys.md)
- [Protecting keys with the Secure Enclave](./protecting-keys-with-the-secure-enclave.md)

#### Return Value

The newly generated private key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the key when you are done with it.

#### Discussion

To get the associated public key, use [`SecKeyCopyPublicKey(_:)`](./seckeycopypublickey%28_%29.md). [`SecKeyCreateRandomKey(_:_:)`](./seckeycreaterandomkey%28_,_%29.md) fails and returns [`errSecInteractionNotAllowed`](./errsecinteractionnotallowed.md) if you call it in the background on iPhone or iPad while the device is locked.

## Parameters

- `parameters`: A dictionary you use to specify the attributes of the generated keys. See [Key Generation Attributes](./key-generation-attributes.md) for details.
- `error`: An error reference pointer that [`SecKeyCreateRandomKey(_:_:)`](./seckeycreaterandomkey%28_,_%29.md) populates with a suitable error instance on failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreaterandomkey(_:_:))*