# searchableItems(forIdentifiers:searchableItemsHandler:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Requests that the delegate provide searchable items for the provided identifiers.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func searchableItems(forIdentifiers identifiers: [String], searchableItemsHandler: @escaping @Sendable ([CSSearchableItem]) -> Void)
```

```swift
optional func searchableItems(forIdentifiers identifiers: [String]) async -> [CSSearchableItem]
```

```objc
- (void) searchableItemsForIdentifiers:(NSArray<NSString *> *) identifiers searchableItemsHandler:(void (^)(NSArray<CSSearchableItem *> *items)) searchableItemsHandler;
```

#### Discussion

Use this method to provide the framework with a list of identifiers to search for.

## Parameters

- `identifiers`: An array of strings that represent the identifiers.
- `searchableItemsHandler`: A method the framework calls that provides an array of [`CSSearchableItem`](../cssearchableitem.md) objects.

## See Also

### Providing data for an item
- [func searchableItems(forIdentifiers: [String], protectionClass: FileProtectionType, searchableItemsHandler: ([CSSearchableItem]) -> Void)](./searchableitems%28foridentifiers,protectionclass,searchableitemshandler%29.md)
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](./data%28for,itemidentifier,typeidentifier%29.md)
  Returns the data for the requested item during a drag-and-drop operation.
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](./fileurl%28for,itemidentifier,typeidentifier,inplace%29.md)
  Returns a file URL for the requested item during a drag-and-drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:))*