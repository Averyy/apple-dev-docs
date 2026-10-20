# searchableItems(forIdentifiers:protectionClass:searchableItemsHandler:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func searchableItems(forIdentifiers identifiers: [String], protectionClass: FileProtectionType, searchableItemsHandler: @escaping @Sendable ([CSSearchableItem]) -> Void)
```

```swift
optional func searchableItems(forIdentifiers identifiers: [String], protectionClass: FileProtectionType) async -> [CSSearchableItem]
```

```objc
- (void) searchableItemsForIdentifiers:(NSArray<NSString *> *) identifiers protectionClass:(NSFileProtectionType) protectionClass searchableItemsHandler:(void (^)(NSArray<CSSearchableItem *> *items)) searchableItemsHandler;
```

## See Also

### Providing data for an item
- [func searchableItems(forIdentifiers: [String], searchableItemsHandler: ([CSSearchableItem]) -> Void)](./searchableitems%28foridentifiers,searchableitemshandler%29.md)
  Requests that the delegate provide searchable items for the provided identifiers.
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](./data%28for,itemidentifier,typeidentifier%29.md)
  Returns the data for the requested item during a drag-and-drop operation.
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](./fileurl%28for,itemidentifier,typeidentifier,inplace%29.md)
  Returns a file URL for the requested item during a drag-and-drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitems(foridentifiers:protectionclass:searchableitemshandler:))*