# init(for:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request for modifying the specified asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(for assetCollection: PHAssetCollection)
```

```objc
+ (instancetype) changeRequestForAssetCollection:(PHAssetCollection *) assetCollection;
```

## Return Value

An asset collection change request.

## Discussion

After you create a change request within a photo library change block, propose changes to the collection’s title or list of member assets with the properties and instance methods of the change request. After Photos runs your change block, the asset collection reflects your changes. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

Use this method when modifying an asset collection’s metadata or when adding or removing assets without regard to their arrangement. To work with indexes in the list of member assets, use the [`init(for:assets:)`](./init%28for,assets%29.md) method instead.

## Parameters

- `assetCollection`: The asset collection to be modified.

## See Also

### Modifying Asset Collections
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
- [func moveAssets(at: IndexSet, to: Int)](./moveassets%28at,to%29.md)
  Moves the assets at the specified indexes in the asset collection to a new index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/init(for:))*