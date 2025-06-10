# NSMetadataQueryUpdateAddedItemsKey

**Framework**: Foundation  
**Kind**: var

The key for retrieving an array of items added to the query result. By default, this array contains [`NSMetadataItem`](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSMetadataQueryUpdateAddedItemsKey: String
```

## See Also

- [let NSMetadataQueryUpdateChangedItemsKey: String](nsmetadataqueryupdatechangeditemskey.md)
  The key for retrieving an array of items that have changed in the query result. By default, this array contains [`NSMetadataItem`](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
- [let NSMetadataQueryUpdateRemovedItemsKey: String](nsmetadataqueryupdateremoveditemskey.md)
  The key for retrieving an array of items removed from the query result. By default, this array contains [`NSMetadataItem`](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryupdateaddeditemskey)*