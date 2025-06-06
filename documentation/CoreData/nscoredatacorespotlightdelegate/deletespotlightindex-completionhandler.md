# deleteSpotlightIndex(completionHandler:)

**Framework**: Coredata  
**Kind**: method

Deletes all searchable items from the configured index.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func deleteSpotlightIndex() async throws
```

#### Discussion

The closure returns no value and takes only a single parameter, which is an error object that contains information about issues preventing the deletion of searchable items, or `nil` if Core Spotlight successfully deletes all searchable items.

Depending on the cause of the issue, an error can originate from Core Data or from Core Spotlight. Make sure your app can handle both scenarios.

> **Note**:  You must call [`stopSpotlightIndexing()`](nscoredatacorespotlightdelegate/stopspotlightindexing().md) before you call this method; otherwise, Core Data immediately recreates the index.

## See Also

- [func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?](nscoredatacorespotlightdelegate/attributeset(for:).md)
  Returns the searchable attributes for the specified managed object.
- [func startSpotlightIndexing()](nscoredatacorespotlightdelegate/startspotlightindexing.md)
  Starts the indexing of the store’s entities.
- [func stopSpotlightIndexing()](nscoredatacorespotlightdelegate/stopspotlightindexing.md)
  Stops the indexing of the store’s entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:))*