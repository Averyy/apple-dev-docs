# ASImportableCollection

**Framework**: Authentication Services  
**Kind**: struct

A collection of items and subcollections for use in import and export.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ASImportableCollection
```

#### Overview

A collection represents a group of items such as a vault or folder.

This type is a representation of `Collection` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `Collection` to initialize an instance of this struct by using a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) and calling [`decode(_:from:)`](https://developer.apple.com/documentation/Foundation/JSONDecoder/decode(_:from:)).

## Topics

### Accessing collection properties
- [var id: Data](asimportablecollection/id.md)
  A unique identifier for the collection.
- [var title: String](asimportablecollection/title.md)
  The title of the collection.
- [var subtitle: String?](asimportablecollection/subtitle.md)
  The subtitle of the collection, if any.
- [var items: [ASImportableLinkedItem]](asimportablecollection/items.md)
  The items that are part of the collection.
- [struct ASImportableLinkedItem](asimportablelinkeditem.md)
  A linked item for use in import and export.
- [var subcollections: [ASImportableCollection]](asimportablecollection/subcollections.md)
  Subcollections that are part of the collection.
### Initializers
- [init(id: Data, created: Date?, lastModified: Date?, title: String, subtitle: String?, items: [ASImportableLinkedItem], subcollections: [ASImportableCollection])](asimportablecollection/init(id:created:lastmodified:title:subtitle:items:subcollections:).md)
### Instance Properties
- [var created: Date?](asimportablecollection/created.md)
  The date and time when the collection was created.
- [var lastModified: Date?](asimportablecollection/lastmodified.md)
  The date and time when the collection was last modified.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var items: [ASImportableItem]](asimportableaccount/items.md)
  All items stored in the account.
- [struct ASImportableItem](asimportableitem.md)
  An item for use in import and export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecollection)*