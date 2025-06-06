# ASImportableItem.ItemType

**Framework**: Authentication Services  
**Kind**: enum

The type of an importable item.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
enum ItemType
```

## Topics

### Item types
- [ASImportableItem.ItemType.login](asimportableitem/itemtype/login.md)
  The type for an item that contains login-related credential information.
- [ASImportableItem.ItemType.document](asimportableitem/itemtype/document.md)
  The type for an item that contains document-related credential information.
- [ASImportableItem.ItemType.identity](asimportableitem/itemtype/identity.md)
  The type for an item that contains identity-related credential information.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [var subtitle: String?](asimportableitem/subtitle.md)
  A subtitle or description of this item, if any.
- [var credentials: [ASImportableCredential]](asimportableitem/credentials.md)
  The credentials associated with this item.
- [enum ASImportableCredential](asimportablecredential.md)
  A credential for use in import and export.
- [var tags: [String]](asimportableitem/tags.md)
  The user-defined tags associated with this item, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableitem/itemtype)*