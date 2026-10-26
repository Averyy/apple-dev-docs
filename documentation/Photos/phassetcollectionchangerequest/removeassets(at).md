# removeAssets(at:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Removes the assets at the specified indexes from the asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func removeAssets(at indexes: IndexSet)
```

```objc
- (void) removeAssetsAtIndexes:(NSIndexSet *) indexes;
```

#### Discussion

To ensure that the index set you specify is valid even if the asset collection has changed since you fetched it, create a change request with a snapshot of the asset collection’s contents using the [`init(for:assets:)`](./init%28for,assets%29.md) method before removing assets. To remove objects based on their identities (without regard to their indexes in the collection), use the [`removeAssets(_:)`](./removeassets%28_%29.md) method.

> **Note**:  Transient asset collections (such as those created with the [`transientAssetCollection(with:title:)`](../phassetcollection/transientassetcollection%28with,title%29.md) method) do not support adding or removing content.

## Parameters

- `indexes`: The indexes of the assets to be removed from the asset collection.

## See Also

### Modifying Asset Collections
- [convenience init?(for: PHAssetCollection)](./init%28for%29.md)
  Creates a request for modifying the specified asset collection.
- [convenience init?(for: PHAssetCollection, assets: PHFetchResult<PHAsset>?)](./init%28for,assets%29.md)
  Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [var title: String](./title.md)
  The displayed name of the asset collection.
- [func addAssets(any NSFastEnumeration)](./addassets%28_%29.md)
  Adds the specified assets to the asset collection.
- [func insertAssets(any NSFastEnumeration, at: IndexSet)](./insertassets%28_,at%29.md)
  Inserts the specified assets into the collection at the specified indexes.
- [func removeAssets(any NSFastEnumeration)](./removeassets%28_%29.md)
  Removes the specified assets from the asset collection.
- [func replaceAssets(at: IndexSet, withAssets: any NSFastEnumeration)](./replaceassets%28at,withassets%29.md)
  Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [func moveAssets(at: IndexSet, to: Int)](./moveassets%28at,to%29.md)
  Moves the assets at the specified indexes in the asset collection to a new index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/removeassets(at:))*