# init(for:assets:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(for assetCollection: PHAssetCollection, assets: PHFetchResult<PHAsset>?)
```

```objc
+ (instancetype) changeRequestForAssetCollection:(PHAssetCollection *) assetCollection assets:(PHFetchResult<PHAsset *> *) assets;
```

#### Return Value

An asset collection change request.

#### Discussion

After you create a change request within a photo library change block, you propose changes to the collection’s title or list of member assets with the properties and instance methods of the change request. After Photos runs your change block, the asset collection reflects your changes. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

Use this method when you need to insert, remove, or rearrange assets at specified indexes in the asset collection’s list of member assets. By passing in a fetch result reflecting what your app sees as the current state of the collection’s membership, the Photos framework can ensure that the indexes you specify are valid even if the collection has changed since you last fetched it. If you don’t need to work with indexes in the list of member assets, you can use the [`init(for:)`](./init%28for%29.md) method instead.

## Parameters

- `assetCollection`: The asset collection to be modified.
- `assets`: A fetch result listing the assets in the collection.

## See Also

### Modifying Asset Collections
- [convenience init?(for: PHAssetCollection)](./init%28for%29.md)
  Creates a request for modifying the specified asset collection.
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
- [func moveAssets(at: IndexSet, to: Int)](./moveassets%28at,to%29.md)
  Moves the assets at the specified indexes in the asset collection to a new index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/init(for:assets:))*