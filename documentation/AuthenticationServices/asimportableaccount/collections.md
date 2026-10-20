# collections

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The collections stored in this account.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var collections: [ASImportableCollection]
```

## See Also

### Accessing account properties
- [var id: Data](./id.md)
  A unique identifier for the account.
- [var userName: String](./username.md)
  The username associated with the account.
- [var email: String](./email.md)
  The email address associated with this account.
- [var fullName: String?](./fullname.md)
  The full name of the account owner, if provided.
- [struct ASImportableCollection](../asimportablecollection.md)
  A collection of items and subcollections for use in import and export.
- [var items: [ASImportableItem]](./items.md)
  All items stored in the account.
- [struct ASImportableItem](../asimportableitem.md)
  An item for use in import and export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableaccount/collections)*