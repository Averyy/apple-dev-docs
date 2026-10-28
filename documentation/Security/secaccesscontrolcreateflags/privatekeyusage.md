# privateKeyUsage

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Enable a private key to be used in signing a block of data or verifying a signed block.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var privateKeyUsage: SecAccessControlCreateFlags { get }
```

```c
kSecAccessControlPrivateKeyUsage
```

## Mentions

- [Protecting keys with the Secure Enclave](../protecting-keys-with-the-secure-enclave.md)

## Discussion

This option can be combined with any other access control flags.

You typically use this constraint when you create a key pair and store the private key inside a device’s Secure Enclave (by specifying the [`kSecAttrTokenID`](../ksecattrtokenid.md) attribute with a value of [`kSecAttrTokenIDSecureEnclave`](../ksecattrtokenidsecureenclave.md)). This makes the private key available for use in signing and verification tasks that happen inside the Secure Enclave with calls to the [`SecKeyRawSign(_:_:_:_:_:_:)`](../seckeyrawsign%28_,_,_,_,_,_%29.md) and [`SecKeyRawVerify(_:_:_:_:_:_:)`](../seckeyrawverify%28_,_,_,_,_,_%29.md) functions. An attempt to use this constraint while generating a key pair outside the Secure Enclave fails. Similarly, an attempt to sign a block with a private key generated without this constraint inside the Secure Enclave fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/privatekeyusage)*