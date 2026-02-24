# fileURL(for:itemIdentifier:typeIdentifier:inPlace:)

**Framework**: Core Spotlight  
**Kind**: method

Returns a file URL for the requested item during a drag-and-drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func fileURL(for searchableIndex: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL
```

#### Return Value

A data object with the requested type of data.

#### Discussion

If the attributes of your [`CSSearchableItem`](cssearchableitem.md) contain one or more provider data types, the system may call this method to request one of those types. Use your implementation of this method to return the file URL for the requested item. The system calls this method on your index’s delegate if your app is running, or the delegate in your Core delegate app extension if your app isn’t running.

Produce the URL as quickly as possible so the app receiving the data can update its interface. The system calls this method at the end of a drag-and-drop operation, while the receiving app waits.

## Parameters

- `searchableIndex`: The index containing the requested searchable item.
- `itemIdentifier`: The unique identifier of the searchable item. Use this value to locate the item in your content.
- `typeIdentifier`: The type of data that you must provide. This parameter contains one of the values from the [`providerFileTypeIdentifiers`](cssearchableitemattributeset/providerfiletypeidentifiers.md) or [`providerInPlaceFileTypeIdentifiers`](cssearchableitemattributeset/providerinplacefiletypeidentifiers.md) property of the item’s attribute set.
- `inPlace`: A Boolean that indicates whether to return the URL of the original file or a copy of the original file. This parameter is `true` for types you specified in the [`providerInPlaceFileTypeIdentifiers`](cssearchableitemattributeset/providerinplacefiletypeidentifiers.md) property of the item’s attributes. If this parameter is `false`, create a copy of the file and return its URL.

## See Also

- [func searchableItems(forIdentifiers: [String], searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:).md)
  Requests that the delegate provide searchable items for the provided identifiers.
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:).md)
  Returns the data for the requested item during a drag-and-drop operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/fileurl(for:itemidentifier:typeidentifier:inplace:))*