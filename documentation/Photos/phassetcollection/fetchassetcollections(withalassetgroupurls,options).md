# fetchAssetCollections(withALAssetGroupURLs:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves asset collections using URLs provided by the Assets Library framework.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 10.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Will be removed in a future release

## Declaration

```swift
class func fetchAssetCollections(withALAssetGroupURLs assetGroupURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

```objc
+ (PHFetchResult<PHAssetCollection *> *) fetchAssetCollectionsWithALAssetGroupURLs:(NSArray<NSURL *> *) assetGroupURLs options:(PHFetchOptions *) options;
```

## Return Value

A fetch result that contains the requested [`PHAssetCollection`](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Assets Library framework is deprecated in iOS 8.0 and later, replaced by the Photos framework. Use this method if your app has previously stored URLs from [`ALAssetsGroup`](../../AssetsLibrary/alassetsgroup.md) objects and you need to retrieve the corresponding Photos framework objects.

## Parameters

- `assetGroupURLs`: An array of [`NSURL`](../../Foundation/nsurl.md) objects, each an asset group URL that was previously retrieved from an [`ALAssetsGroup`](../../AssetsLibrary/alassetsgroup.md) object.
- `options`: Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Asset Collections
- [class func fetchAssetCollections(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollections%28withlocalidentifiers,options%29.md)
  Retrieves asset collections with the specified unique identifiers.
- [class func fetchAssetCollections(with: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollections%28with,subtype,options%29.md)
  Retrieves asset collections of the specified type and subtype.
- [class func fetchAssetCollectionsContaining(PHAsset, with: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollectionscontaining%28_,with,options%29.md)
  Retrieves asset collections of the specified type containing the specified asset.
- [class func fetchMoments(inMomentList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchmoments%28inmomentlist,options%29.md)
  Retrieves asset collections in the specified moment list collection.
- [class func fetchMoments(with: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchmoments%28with%29.md)
  Retrieves asset collections corresponding to moments seen in the Photos app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollections(withalassetgroupurls:options:))*