# ASImportableCredential

**Framework**: Authentication Services  
**Kind**: enum

A credential for use in import and export.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

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

This type is a representation of `Credential` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `Credential` to initialize an instance of this struct by using a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) and calling [`decode(_:from:)`](https://developer.apple.com/documentation/foundation/jsondecoder/2895189-decode).

## Topics

### Login credential types
- [case basicAuthentication(ASImportableCredential.BasicAuthentication)](asimportablecredential/basicauthentication(_:).md)
  A password credential.
- [ASImportableCredential.BasicAuthentication](asimportablecredential/basicauthentication.md)
  A type to represent a basic authentication password.
- [case passkey(ASImportableCredential.Passkey)](asimportablecredential/passkey(_:).md)
  A passkey credential.
- [ASImportableCredential.Passkey](asimportablecredential/passkey.md)
  A type to represent a passkey credential.
- [case totp(ASImportableCredential.TOTP)](asimportablecredential/totp(_:).md)
  A time-based one-time password (TOTP) credential.
- [ASImportableCredential.TOTP](asimportablecredential/totp.md)
  A type to represent a time-based one-time password generator (TOTP).
### Document credential types
- [case note(ASImportableCredential.Note)](asimportablecredential/note(_:).md)
  A note credential.
- [ASImportableCredential.Note](asimportablecredential/note.md)
  A piece of text used to store some information about an item.
### Identity credential types
- [case creditCard(ASImportableCredential.CreditCard)](asimportablecredential/creditcard(_:).md)
  A credit card credential.
- [ASImportableCredential.CreditCard](asimportablecredential/creditcard.md)
  A type to represent credit card information.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var id: Data](asimportableitem/id.md)
  A unique identifier for the item.
- [var created: Date](asimportableitem/created.md)
  The item’s creation date and time.
- [var lastModified: Date](asimportableitem/lastmodified.md)
  The item’s last modified date and time.
- [var type: ASImportableItem.ItemType](asimportableitem/type.md)
  The type of the item.
- [ASImportableItem.ItemType](asimportableitem/itemtype.md)
  The type of an importable item.
- [var subtitle: String?](asimportableitem/subtitle.md)
  A subtitle or description of this item, if any.
- [var credentials: [ASImportableCredential]](asimportableitem/credentials.md)
  The credentials associated with this item.
- [var tags: [String]](asimportableitem/tags.md)
  The user-defined tags associated with this item, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential)*