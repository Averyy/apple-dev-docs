# errSecDuplicateItem

**Framework**: Security  
**Kind**: var

The item already exists.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var errSecDuplicateItem: OSStatus { get }
```

#### Discussion

The system considers an item to be a duplicate for a given keychain when that keychain already has an item of the same class with the same set of composite primary keys. Each class of keychain item has a different set of primary keys, although a few attributes are used in common across all classes. In particular, where applicable, [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) and [`kSecAttrAccessGroup`](ksecattraccessgroup.md) are part of the set of primary keys. The additional per-class primary keys are listed below:

For generic passwords, the primary keys include [`kSecAttrAccount`](ksecattraccount.md) and [`kSecAttrService`](ksecattrservice.md).

For internet passwords, the primary keys include [`kSecAttrAccount`](ksecattraccount.md), [`kSecAttrSecurityDomain`](ksecattrsecuritydomain.md), [`kSecAttrServer`](ksecattrserver.md), [`kSecAttrProtocol`](ksecattrprotocol.md), [`kSecAttrAuthenticationType`](ksecattrauthenticationtype.md), [`kSecAttrPort`](ksecattrport.md), and [`kSecAttrPath`](ksecattrpath.md).

For certificates, the primary keys include [`kSecAttrCertificateType`](ksecattrcertificatetype.md), [`kSecAttrIssuer`](ksecattrissuer.md), and [`kSecAttrSerialNumber`](ksecattrserialnumber.md).

For key items, the primary keys include [`kSecAttrKeyClass`](ksecattrkeyclass.md), [`kSecAttrKeyType`](ksecattrkeytype.md), [`kSecAttrApplicationLabel`](ksecattrapplicationlabel.md), [`kSecAttrApplicationTag`](ksecattrapplicationtag.md), [`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md), and [`kSecAttrEffectiveKeySize`](ksecattreffectivekeysize.md).

For identity items, which are a certificate and a private key bundled together, the primary keys are the same as for a certificate. Because a private key may be certified more than once, the uniqueness of the certificate determines that of the identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errsecduplicateitem)*