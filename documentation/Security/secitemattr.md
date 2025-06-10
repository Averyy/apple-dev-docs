# SecItemAttr

**Framework**: Security  
**Kind**: enum

Specifies a keychain item’s attributes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecItemAttr
```

#### Overview

Not all of these attributes are used for all types of items. Which set of attributes exist for each type of item is documented in the “Data Storage Library Services” chapter of  from The Open Group ([`http://www.opengroup.org/security/cdsa.htm`](https://developer.apple.comhttp://www.opengroup.org/security/cdsa.htm)) for standard items and in the DL section of the  for Apple-defined item types (if any).

To obtain information about a certificate, use the CDSA Certificate Library (CL) API. To obtain information about a key, use the `SecKeyGetCSSMKey` function and the CDSA Cryptographic Service Provider (CSP) API.

For attributes for keys, see [`Keychain Item Attribute Constants For Keys`](keychain-item-attribute-constants-for-keys.md).

## Topics

### Constants
- [SecItemAttr.creationDateItemAttr](secitemattr/creationdateitemattr.md)
  Identifies the creation date attribute.
- [SecItemAttr.modDateItemAttr](secitemattr/moddateitemattr.md)
  Identifies the modification date attribute.
- [SecItemAttr.descriptionItemAttr](secitemattr/descriptionitemattr.md)
  Identifies the description attribute.
- [SecItemAttr.commentItemAttr](secitemattr/commentitemattr.md)
  Identifies the comment attribute.
- [SecItemAttr.creatorItemAttr](secitemattr/creatoritemattr.md)
  Identifies the creator attribute.
- [SecItemAttr.typeItemAttr](secitemattr/typeitemattr.md)
  Identifies the type attribute.
- [SecItemAttr.scriptCodeItemAttr](secitemattr/scriptcodeitemattr.md)
  Identifies the script code attribute.
- [SecItemAttr.labelItemAttr](secitemattr/labelitemattr.md)
  Identifies the label attribute.
- [SecItemAttr.invisibleItemAttr](secitemattr/invisibleitemattr.md)
  Identifies the invisible attribute.
- [SecItemAttr.negativeItemAttr](secitemattr/negativeitemattr.md)
  Identifies the negative attribute.
- [SecItemAttr.customIconItemAttr](secitemattr/customiconitemattr.md)
  Identifies the custom icon attribute.
- [SecItemAttr.accountItemAttr](secitemattr/accountitemattr.md)
  Identifies the account attribute.
- [SecItemAttr.serviceItemAttr](secitemattr/serviceitemattr.md)
  Identifies the service attribute.
- [SecItemAttr.genericItemAttr](secitemattr/genericitemattr.md)
  Identifies the generic attribute.
- [SecItemAttr.securityDomainItemAttr](secitemattr/securitydomainitemattr.md)
  Identifies the security domain attribute.
- [SecItemAttr.serverItemAttr](secitemattr/serveritemattr.md)
  Identifies the server attribute.
- [SecItemAttr.authenticationTypeItemAttr](secitemattr/authenticationtypeitemattr.md)
  Identifies the authentication type attribute.
- [SecItemAttr.portItemAttr](secitemattr/portitemattr.md)
  Identifies the port attribute.
- [SecItemAttr.pathItemAttr](secitemattr/pathitemattr.md)
  Identifies the path attribute.
- [SecItemAttr.volumeItemAttr](secitemattr/volumeitemattr.md)
  Identifies the volume attribute.
- [SecItemAttr.addressItemAttr](secitemattr/addressitemattr.md)
  Identifies the address attribute.
- [SecItemAttr.signatureItemAttr](secitemattr/signatureitemattr.md)
  Identifies the server signature attribute.
- [SecItemAttr.protocolItemAttr](secitemattr/protocolitemattr.md)
  Identifies the protocol attribute.
- [SecItemAttr.certificateType](secitemattr/certificatetype.md)
  Indicates a `CSSM_CERT_TYPE` type.
- [SecItemAttr.certificateEncoding](secitemattr/certificateencoding.md)
  Indicates a `CSSM_CERT_ENCODING` type.
- [SecItemAttr.crlType](secitemattr/crltype.md)
  Indicates a `CSSM_CRL_TYPE` type.
- [SecItemAttr.crlEncoding](secitemattr/crlencoding.md)
  Indicates a `CSSM_CRL_ENCODING` type.
- [SecItemAttr.alias](secitemattr/alias.md)
  Indicates an alias.
### Initializers
- [init?(rawValue: FourCharCode)](secitemattr/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemattr)*