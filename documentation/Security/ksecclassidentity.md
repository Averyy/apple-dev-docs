# kSecClassIdentity

**Framework**: Security  
**Kind**: var

The value that indicates an identity item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecClassIdentity: CFString
```

## Mentions

- [Storing an Identity in the Keychain](storing-an-identity-in-the-keychain.md)

#### Discussion

An identity is a certificate paired with its associated private key. Keychain services stores the certificate and the private key separately; it represents the pair as an identity if the certificate’s [`kSecAttrPublicKeyHash`](ksecattrpublickeyhash.md) attribute matches the key’s [`kSecAttrApplicationLabel`](ksecattrapplicationlabel.md) attribute.

Because an identity is the combination of a private key and a certificate, this class shares attributes of both [`kSecClassKey`](ksecclasskey.md) and [`kSecClassCertificate`](ksecclasscertificate.md). Multiple certificates can all attest the identity of the same private key, so the attributes that form an identity’s composite primary key are the same as those for a certificate.

The set of identity items available to your app in the keychain can change without explicitly adding, updating, or deleting identity items. For example, if the keychain contains a cryptographic key item and certificate item that form an identity and you delete the key, the identity no longer exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecclassidentity)*