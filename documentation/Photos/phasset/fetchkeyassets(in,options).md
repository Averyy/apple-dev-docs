# fetchKeyAssets(in:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves assets marked as key assets in the specified asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchKeyAssets(in assetCollection: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>?
```

```objc
+ (PHFetchResult<PHAsset *> *) fetchKeyAssetsInAssetCollection:(PHAssetCollection *) assetCollection options:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHAsset`](../phasset.md) objects, or an empty fetch result or `nil` if no objects match the request.

#### Discussion

Most asset collections contain a *key asset*, which the Photos app displays as a proxy for the collection. Different types of asset collections have different ways of specifying one or more key assets. For example, in the Camera Roll collection, the most recently captured photo or video is the key asset.

This method returns `nil` if the `assetCollection` parameter references a transient asset collection (such as one created with the [`transientAssetCollection(with:title:)`](../phassetcollection/transientassetcollection%28with,title%29.md) method).

## Parameters

- `assetCollection`: The asset collection from which to fetch assets.
- `options`: Options that specify a filter predicate and sort order for the fetched assets, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Assets
- [Fetching Assets](../../PhotoKit/fetching-assets.md)
  Retrieve asset metadata or request full asset content.
- [class func fetchAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28in,options%29.md)
  Retrieves assets from the specified asset collection.
- [class func fetchAssets(with: PHAssetMediaType, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28with,options%29.md)
  Retrieves assets with the specified media type.
- [class func fetchAssets(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withlocalidentifiers,options%29.md)
  Retrieves assets with the specified local-device-specific unique identifiers.
- [class func fetchAssets(with: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28with%29.md)
  Retrieves all assets matching the specified options.
- [class func fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withburstidentifier,options%29.md)
  Retrieves assets with the specified burst photo sequence identifier.
- [class func fetchAssets(withALAssetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withalasseturls,options%29.md)
  Retrieves assets using URLs provided by the Assets Library framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/fetchkeyassets(in:options:))*