# ASImportableAccount

**Framework**: Authentication Services  
**Kind**: struct

An account for use in importing and exporting credentials.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ASImportableAccount
```

#### Overview

This type is a representation of `Account` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `Account` to initialize an instance of this struct by using a [`JSONDecoder`](https://developer.apple.com/documentation/foundation/jsondecoder) and calling [`decode(_:from:)`](https://developer.apple.com/documentation/foundation/jsondecoder/decode(_:from:)). When using a [`JSONDecoder`](https://developer.apple.com/documentation/foundation/jsondecoder), set the [`dateDecodingStrategy`](https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.property) property of the decoder to [`JSONDecoder.DateDecodingStrategy.secondsSince1970`](https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum/secondssince1970).

The account represents the user of the password manager app itself. You can export multiple accounts together by including them in an [`ASExportedCredentialData`](asexportedcredentialdata.md) instance.

## Topics

### Creating an account
- [init(id: Data, userName: String, email: String, fullName: String?, collections: [ASImportableCollection], items: [ASImportableItem])](asimportableaccount/init(id:username:email:fullname:collections:items:).md)
  Creates an account instance from its required and optional properties.
### Accessing account properties
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
- [struct ASImportableItem](asimportableitem.md)
  An item for use in import and export.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var accounts: [ASImportableAccount]](asexportedcredentialdata/accounts.md)
  An array of importable accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableaccount)*