# searchableItems(forIdentifiers:searchableItemsHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Requests that the delegate provide searchable items for the provided identifiers.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 41.4+ (Beta)

## Declaration

```swift
optional func searchableItems(forIdentifiers identifiers: [String]) async -> [CSSearchableItem]
```

#### Discussion

Use this method to provide the framework with a list of identifiers to search for.

## Parameters

- `identifiers`: An array of strings that represent the identifiers.
- `searchableItemsHandler`: A method the framework calls that provides an array of [`CSSearchableItem`](cssearchableitem.md) objects.

## See Also

- [func searchableItems(forIdentifiers: [String], protectionClass: FileProtectionType, searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:protectionclass:searchableitemshandler:).md)
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:).md)
  Returns the data for the requested item during a drag-and-drop operation.
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](cssearchableindexdelegate/fileurl(for:itemidentifier:typeidentifier:inplace:).md)
  Returns a file URL for the requested item during a drag-and-drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:))*