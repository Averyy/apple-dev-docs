# data(for:itemIdentifier:typeIdentifier:)

**Framework**: Core Spotlight  
**Kind**: method

Returns the data for the requested item during a drag-and-drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func data(for searchableIndex: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data
```

#### Return Value

A data object with the requested type of data.

#### Discussion

If the attributes of your [`CSSearchableItem`](cssearchableitem.md) contain one or more provider data types, the system may call this method to request one of those types. Use your implementation of this method to generate a data object with the requested type of data for the specified item. The system calls this method on your index’s delegate if your app is running, or the delegate in your Core delegate app extension if your app isn’t running.

Produce the data as quickly as possible so the app receiving the data can update its interface. The system calls this method at the end of a drag-and-drop operation, while the receiving app waits.

## Parameters

- `searchableIndex`: The index containing the requested searchable item.
- `itemIdentifier`: The unique identifier of the searchable item. Use this value to locate   the item in your content.
- `typeIdentifier`: The type of data that you must provide. This parameter contains one of   the values from the   property   of the item’s attribute set.

## See Also

- [func searchableItems(forIdentifiers: [String], searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:).md)
  Requests that the delegate provide searchable items for the provided identifiers.
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](cssearchableindexdelegate/fileurl(for:itemidentifier:typeidentifier:inplace:).md)
  Returns a file URL for the requested item during a drag-and-drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:))*