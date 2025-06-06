# attributeSet(for:)

**Framework**: Core Data  
**Kind**: method

Returns the searchable attributes for the specified managed object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func attributeSet(for object: NSManagedObject) -> CSSearchableItemAttributeSet?
```

#### Return Value

An instance of [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) that provides the searchable item’s attributes.

#### Discussion

> ❗ **Important**:  If you enable [`isIndexedBySpotlight`](nspropertydescription/isindexedbyspotlight.md) on a property description that describes a relationship, override this method and return the necessary set of attributes. Core Data doesn’t automatically infer indexable information for relationships.

 If you enable [`isIndexedBySpotlight`](nspropertydescription/isindexedbyspotlight.md) on a property description that describes a relationship, override this method and return the necessary set of attributes. Core Data doesn’t automatically infer indexable information for relationships.

To prevent Core Spotlight from indexing a specific managed object, override this method and return `nil` for that object.

## Parameters

- `object`: The managed object to index.

## See Also

- [func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)](nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:).md)
  Deletes all searchable items from the configured index.
- [func startSpotlightIndexing()](nscoredatacorespotlightdelegate/startspotlightindexing.md)
  Starts the indexing of the store’s entities.
- [func stopSpotlightIndexing()](nscoredatacorespotlightdelegate/stopspotlightindexing.md)
  Stops the indexing of the store’s entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/attributeset(for:))*