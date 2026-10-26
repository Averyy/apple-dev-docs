# ASImportableCredential

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

A credential for use in import and export.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ASImportableCredential
```

#### Overview

A credential represents a piece of secure information associated with an item. `ASImportableCredential` currently supports the following kinds of credentials:

- Password (`BasicAuthentication`)
- Passkey
- Time-based one-time password (TOTP)
- Note
- Credit card

This type is a representation of `Credential` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `Credential` to initialize an instance of this struct by using a [`JSONDecoder`](../Foundation/jsondecoder.md) and calling [`decode(_:from:)`](../Foundation/jsondecoder/decode%28_,from%29.md).

## Topics

### Login credential types
- [case basicAuthentication(ASImportableCredential.BasicAuthentication)](./asimportablecredential/basicauthentication%28_%29.md)
  A password credential.
- [ASImportableCredential.BasicAuthentication](./asimportablecredential/basicauthentication.md)
  A type to represent a basic authentication password.
- [case passkey(ASImportableCredential.Passkey)](./asimportablecredential/passkey%28_%29.md)
  A passkey credential.
- [ASImportableCredential.Passkey](./asimportablecredential/passkey.md)
  A type to represent a passkey credential.
- [case totp(ASImportableCredential.TOTP)](./asimportablecredential/totp%28_%29.md)
  A time-based one-time password (TOTP) credential.
- [ASImportableCredential.TOTP](./asimportablecredential/totp.md)
  A type to represent a time-based one-time password generator (TOTP).
### Document credential types
- [case note(ASImportableCredential.Note)](./asimportablecredential/note%28_%29.md)
  A note credential.
- [ASImportableCredential.Note](./asimportablecredential/note.md)
  A piece of text used to store some information about an item.
### Identity credential types
- [case creditCard(ASImportableCredential.CreditCard)](./asimportablecredential/creditcard%28_%29.md)
  A credit card credential.
- [ASImportableCredential.CreditCard](./asimportablecredential/creditcard.md)
  A type to represent credit card information.
### Structures
- [ASImportableCredential.APIKey](./asimportablecredential/apikey.md)
  A representation of APIKey as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)
- [ASImportableCredential.Address](./asimportablecredential/address.md)
  A representation of Address as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a physical address.
- [ASImportableCredential.CustomFields](./asimportablecredential/customfields.md)
  A representation of CustomFields as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)
- [ASImportableCredential.DriversLicense](./asimportablecredential/driverslicense.md)
  A representation of DriversLicense as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)
- [ASImportableCredential.GeneratedPassword](./asimportablecredential/generatedpassword.md)
  A representation of GeneratedPassword as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a machine-generated password.
- [ASImportableCredential.IdentityDocument](./asimportablecredential/identitydocument.md)
  A representation of IdentityDocument as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents any kind of document that can be used for identification.
- [ASImportableCredential.ItemReference](./asimportablecredential/itemreference.md)
  A representation of ItemReference as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This is a pointer to another Item.
- [ASImportableCredential.Passport](./asimportablecredential/passport.md)
  A representation of Passport as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a passport document.
- [ASImportableCredential.PersonName](./asimportablecredential/personname.md)
  A representation of PersonName as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a person’s name.
- [ASImportableCredential.SSHKey](./asimportablecredential/sshkey.md)
  A representation of SSHKey as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html)
- [ASImportableCredential.WiFi](./asimportablecredential/wifi.md)
  A representation of Wi-Fi Passphrase as defined in the [CredentialExchange Format (CXF) specs](https://fidoalliance.org/specs/cx/cxf-v1.0-rd-20250313.html) This represents a credential for a WiFi network..
### Enumeration Cases
- [case address(ASImportableCredential.Address)](./asimportablecredential/address%28_%29.md)
- [case apiKey(ASImportableCredential.APIKey)](./asimportablecredential/apikey%28_%29.md)
- [case customFields(ASImportableCredential.CustomFields)](./asimportablecredential/customfields%28_%29.md)
- [case driversLicense(ASImportableCredential.DriversLicense)](./asimportablecredential/driverslicense%28_%29.md)
- [case generatedPassword(ASImportableCredential.GeneratedPassword)](./asimportablecredential/generatedpassword%28_%29.md)
- [case identityDocument(ASImportableCredential.IdentityDocument)](./asimportablecredential/identitydocument%28_%29.md)
- [case itemReference(ASImportableCredential.ItemReference)](./asimportablecredential/itemreference%28_%29.md)
- [case passport(ASImportableCredential.Passport)](./asimportablecredential/passport%28_%29.md)
- [case personName(ASImportableCredential.PersonName)](./asimportablecredential/personname%28_%29.md)
- [case sshKey(ASImportableCredential.SSHKey)](./asimportablecredential/sshkey%28_%29.md)
- [case wifi(ASImportableCredential.WiFi)](./asimportablecredential/wifi%28_%29.md)

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing item properties
- [var id: Data](./asimportableitem/id.md)
  A unique identifier for the item.
- [var created: Date?](./asimportableitem/created.md)
  The item’s creation date and time.
- [var lastModified: Date?](./asimportableitem/lastmodified.md)
  The item’s last modified date and time.
- [var subtitle: String?](./asimportableitem/subtitle.md)
  A subtitle or description of this item, if any.
- [var credentials: [ASImportableCredential]](./asimportableitem/credentials.md)
  The credentials associated with this item.
- [var tags: [String]](./asimportableitem/tags.md)
  The user-defined tags associated with this item, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential)*