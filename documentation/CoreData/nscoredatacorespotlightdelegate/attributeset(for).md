# attributeSet(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CSSearchableItemAttributeSet *) attributeSetForObject:(NSManagedObject *) object;
```

## Return Value

An instance of [`CSSearchableItemAttributeSet`](../../CoreSpotlight/cssearchableitemattributeset.md) that provides the searchable item’s attributes.

## Discussion

> ❗ **Important**:  If you enable [`isIndexedBySpotlight`](../nspropertydescription/isindexedbyspotlight.md) on a property description that describes a relationship, override this method and return the necessary set of attributes. Core Data doesn’t automatically infer indexable information for relationships.

To prevent Core Spotlight from indexing a specific managed object, override this method and return `nil` for that object.

## Parameters

- `object`: The managed object to index.

## See Also

### Managing the Index
- [func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)](./deletespotlightindex%28completionhandler%29.md)
  Deletes all searchable items from the configured index.
- [func startSpotlightIndexing()](./startspotlightindexing%28%29.md)
  Starts the indexing of the store’s entities.
- [func stopSpotlightIndexing()](./stopspotlightindexing%28%29.md)
  Stops the indexing of the store’s entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/attributeset(for:))*