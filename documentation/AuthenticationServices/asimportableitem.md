# ASImportableItem

**Framework**: Authentication Services  
**Kind**: struct

An item for use in import and export.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
struct ASImportableItem
```

#### Overview

An item represents an account for a service stored by the password manager. One item can store multiple credentials. For example, to represent an account with a password and a passkey, use an item with two credentials: a [`ASImportableCredential.BasicAuthentication`](asimportablecredential/basicauthentication.md) password and a [`ASImportableCredential.Passkey`](asimportablecredential/passkey.md).

This type is a representation of `Item` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `Item` to initialize an instance of this struct by using a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) and calling [`decode(_:from:)`](https://developer.apple.com/documentation/foundation/jsondecoder/2895189-decode).

## Topics

### Creating an item
- [init(id: Data, created: Date, lastModified: Date, type: ASImportableItem.ItemType, title: String, subtitle: String?, credentials: [ASImportableCredential], tags: [String])](asimportableitem/init(id:created:lastmodified:type:title:subtitle:credentials:tags:).md)
  Creates an importable item.
### Accessing item properties
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
- [enum ASImportableCredential](asimportablecredential.md)
  A credential for use in import and export.
- [var tags: [String]](asimportableitem/tags.md)
  The user-defined tags associated with this item, if any.
### Instance Properties
- [var title: String](asimportableitem/title.md)
  The user-defined name or title of this item.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var id: Data](asimportableaccount/id.md)
  A unique identifier for the account.
- [var userName: String](asimportableaccount/username.md)
  The username associated with the account.
- [var email: String](asimportableaccount/email.md)
  The email address associated with this account.
- [var fullName: String?](asimportableaccount/fullname.md)
  The full name of the account owner, if provided.
- [var collections: [ASImportableCollection]](asimportableaccount/collections.md)
  The collections stored in this account.
- [struct ASImportableCollection](asimportablecollection.md)
  A collection of items and subcollections for use in import and export.
- [var items: [ASImportableItem]](asimportableaccount/items.md)
  All items stored in the account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableitem)*