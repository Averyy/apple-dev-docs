# kSecAttrTokenID

**Framework**: Security  
**Kind**: var

A key whose value indicates that a cryptographic key is in an external store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrTokenID: CFString
```

## Mentions

- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString), and may only be one of the constants specified in [`Token ID Values`](item-attribute-keys-and-values#Token-ID-Values.md). Presence of this key indicates that the item is backed by an external store, as uniquely identified by the value. An item without this attribute is stored as normal in the keychain database.

> ❗ **Important**:  You can’t change this attribute after creating the keychain item. It isn’t possible to migrate existing items between stores. Setting `kSecAttrTokenID` when creating a keychain item in macOS makes it behave like an iOS keychain item, as if [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) were also set.

 You can’t change this attribute after creating the keychain item. It isn’t possible to migrate existing items between stores. Setting `kSecAttrTokenID` when creating a keychain item in macOS makes it behave like an iOS keychain item, as if [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) were also set.

Use this attribute only in the top-level parameter dictionary during key creation and not in one of the private or public key sub-dictionaries given by [`kSecPrivateKeyAttrs`](ksecprivatekeyattrs.md) or [`kSecPublicKeyAttrs`](ksecpublickeyattrs.md), respectively. For an example, see [`Protecting keys with the Secure Enclave`](protecting-keys-with-the-secure-enclave.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrtokenid)*