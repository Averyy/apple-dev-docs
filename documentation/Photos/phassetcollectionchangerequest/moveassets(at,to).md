# moveAssets(at:to:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Moves the assets at the specified indexes in the asset collection to a new index.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func moveAssets(at fromIndexes: IndexSet, to toIndex: Int)
```

```objc
- (void) moveAssetsAtIndexes:(NSIndexSet *) fromIndexes toIndex:(NSUInteger) toIndex;
```

#### Discussion

When you call this method, Photos first removes the items in the `indexes` parameter from the collection, and then inserts them at the location specified by the `toIndex` parameter.

To ensure that the index set you specify is valid even if the asset collection has changed since you fetched it, create a change request with a snapshot of the asset collection’s contents using the [`init(for:assets:)`](./init%28for,assets%29.md) method before rearranging assets.

## Parameters

- `fromIndexes`: The indexes of the assets to be moved in the asset collection.
- `toIndex`: The index at which to place the moved assets, relative to the collection’s ordering after removing the items at `indexes`.

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
- [func removeAssets(at: IndexSet)](./removeassets%28at%29.md)
  Removes the assets at the specified indexes from the asset collection.
- [func replaceAssets(at: IndexSet, withAssets: any NSFastEnumeration)](./replaceassets%28at,withassets%29.md)
  Replaces the assets at the specified indexes in the asset collection with the specified assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/moveassets(at:to:))*