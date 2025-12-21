# kSecClassCertificate

**Framework**: Security  
**Kind**: var

The value that indicates a certificate item.

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
let kSecClassCertificate: CFString
```

## Mentions

- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)
- [Storing an Identity in the Keychain](storing-an-identity-in-the-keychain.md)

#### Discussion

The following keychain item attributes form the composite primary key of a certificate password item:

- [`kSecAttrAccessGroup`](ksecattraccessgroup.md) (on macOS, this key only applies if you set [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) or [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) to [`true`](https://developer.apple.com/documentation/Swift/true))
- [`kSecAttrCertificateType`](ksecattrcertificatetype.md)
- [`kSecAttrIssuer`](ksecattrissuer.md)
- [`kSecAttrSerialNumber`](ksecattrserialnumber.md)
- [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) (on iOS 14 and newer, iOS 11 newer, and watchOS 7 and newer)

Calls to [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) that add a certificate item with the same values for all of these attributes as an existing item result in [`errSecDuplicateItem`](errsecduplicateitem.md).

The following keychain item attributes apply to a certificate item, and don’t form part of its composite primary key:

- [`kSecAttrAccess`](ksecattraccess.md) (macOS only)
- [`kSecAttrAccessible`](ksecattraccessible.md) (on macOS, this key only applies if you set [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) or [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) to [`true`](https://developer.apple.com/documentation/Swift/true))
- [`kSecAttrCertificateEncoding`](ksecattrcertificateencoding.md)
- [`kSecAttrLabel`](ksecattrlabel.md)
- [`kSecAttrSubject`](ksecattrsubject.md)
- [`kSecAttrSubjectKeyID`](ksecattrsubjectkeyid.md)
- [`kSecAttrPublicKeyHash`](ksecattrpublickeyhash.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecclasscertificate)*