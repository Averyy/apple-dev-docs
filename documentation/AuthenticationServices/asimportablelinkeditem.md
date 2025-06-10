# ASImportableLinkedItem

**Framework**: Authentication Services  
**Kind**: struct

A linked item for use in import and export.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ASImportableLinkedItem
```

#### Overview

A linked item serves as a reference to an item, and contains no data of its own.

This type is a representation of `LinkedItem` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `Item` to initialize an instance of this struct by using a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) and calling [`decode(_:from:)`](https://developer.apple.com/documentation/Foundation/JSONDecoder/decode(_:from:)).

## Topics

### Creating a linked item
- [init(item: Data, account: Data?)](asimportablelinkeditem/init(item:account:).md)
  Creates a linked item from the identifiers of an item and an account.
### Accessing linked item properties
- [var item: Data](asimportablelinkeditem/item.md)
  The unique identifier of the item linked by this linked item.
- [var account: Data?](asimportablelinkeditem/account.md)
  The unique identifier of the account, if any, to which the linked item belongs.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var id: Data](asimportablecollection/id.md)
  A unique identifier for the collection.
- [var title: String](asimportablecollection/title.md)
  The title of the collection.
- [var subtitle: String?](asimportablecollection/subtitle.md)
  The subtitle of the collection, if any.
- [var items: [ASImportableLinkedItem]](asimportablecollection/items.md)
  The items that are part of the collection.
- [var subcollections: [ASImportableCollection]](asimportablecollection/subcollections.md)
  Subcollections that are part of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablelinkeditem)*