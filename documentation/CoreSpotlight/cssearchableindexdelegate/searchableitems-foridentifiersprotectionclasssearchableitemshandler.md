# searchableItems(forIdentifiers:protectionClass:searchableItemsHandler:)

**Framework**: Core Spotlight  
**Kind**: method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func searchableItems(forIdentifiers identifiers: [String], protectionClass: FileProtectionType) async -> [CSSearchableItem]
```

## See Also

- [func searchableItems(forIdentifiers: [String], searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:).md)
  Requests that the delegate provide searchable items for the provided identifiers.
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:).md)
  Returns the data for the requested item during a drag-and-drop operation.
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](cssearchableindexdelegate/fileurl(for:itemidentifier:typeidentifier:inplace:).md)
  Returns a file URL for the requested item during a drag-and-drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitems(foridentifiers:protectionclass:searchableitemshandler:))*