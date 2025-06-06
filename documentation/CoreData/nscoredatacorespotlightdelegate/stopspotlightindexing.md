# stopSpotlightIndexing()

**Framework**: Core Data  
**Kind**: method

Stops the indexing of the store’s entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func stopSpotlightIndexing()
```

#### Discussion

After you call this method, the delegate no longer posts notifications about index changes.

## See Also

- [func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?](nscoredatacorespotlightdelegate/attributeset(for:).md)
  Returns the searchable attributes for the specified managed object.
- [func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)](nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:).md)
  Deletes all searchable items from the configured index.
- [func startSpotlightIndexing()](nscoredatacorespotlightdelegate/startspotlightindexing.md)
  Starts the indexing of the store’s entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/stopspotlightindexing())*