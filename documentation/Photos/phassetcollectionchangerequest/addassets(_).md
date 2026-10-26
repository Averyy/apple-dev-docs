# addAssets(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Adds the specified assets to the asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func addAssets(_ assets: any NSFastEnumeration)
```

```objc
- (void) addAssets:(id<NSFastEnumeration>) assets;
```

## Mentions

- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Discussion

If you created the change request with a snapshot of the asset collection’s contents using the [`init(for:assets:)`](./init%28for,assets%29.md) method, Photos inserts the new assets after the existing assets in the collection. Otherwise, the arrangement of the new assets relative to others in the collection is undefined.

> **Note**:  Assets from My Photo Stream or iCloud Shared Albums and assets synced to the device through iTunes cannot be added to collections. Transient asset collections (such as those created with the [`transientAssetCollection(with:title:)`](../phassetcollection/transientassetcollection%28with,title%29.md) method) do not support adding or removing content.

## Parameters

- `assets`: An array of [`PHAsset`](../phasset.md) objects to be added to the asset collection.

## See Also

### Modifying Asset Collections
- [convenience init?(for: PHAssetCollection)](./init%28for%29.md)
  Creates a request for modifying the specified asset collection.
- [convenience init?(for: PHAssetCollection, assets: PHFetchResult<PHAsset>?)](./init%28for,assets%29.md)
  Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [var title: String](./title.md)
  The displayed name of the asset collection.
- [func insertAssets(any NSFastEnumeration, at: IndexSet)](./insertassets%28_,at%29.md)
  Inserts the specified assets into the collection at the specified indexes.
- [func removeAssets(any NSFastEnumeration)](./removeassets%28_%29.md)
  Removes the specified assets from the asset collection.
- [func removeAssets(at: IndexSet)](./removeassets%28at%29.md)
  Removes the assets at the specified indexes from the asset collection.
- [func replaceAssets(at: IndexSet, withAssets: any NSFastEnumeration)](./replaceassets%28at,withassets%29.md)
  Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [func moveAssets(at: IndexSet, to: Int)](./moveassets%28at,to%29.md)
  Moves the assets at the specified indexes in the asset collection to a new index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/addassets(_:))*