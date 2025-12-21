# id

**Framework**: Authentication Services  
**Kind**: property

A unique identifier for the account.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var id: Data
```

#### Discussion

This property isn’t displayed to the person using the app.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableaccount/id)*