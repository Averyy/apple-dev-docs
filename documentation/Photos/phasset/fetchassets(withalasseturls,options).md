# fetchAssets(withALAssetURLs:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves assets using URLs provided by the Assets Library framework.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 8.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Will be removed in a future release

## Declaration

```swift
class func fetchAssets(withALAssetURLs assetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>
```

```objc
+ (PHFetchResult<PHAsset *> *) fetchAssetsWithALAssetURLs:(NSArray<NSURL *> *) assetURLs options:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHAsset`](../phasset.md) objects, or an empty fetch result if no objects match the request.

#### Discussion

The Assets Library framework is deprecated in iOS 8.0 and later, replaced by the Photos framework. Use this method if your app has previously stored URLs from [`ALAsset`](../../AssetsLibrary/alasset.md) objects and you need to retrieve the corresponding Photos framework objects.

## Parameters

- `assetURLs`: An array of [`NSURL`](../../Foundation/nsurl.md) objects, each an asset URL previously retrieved from an [`ALAsset`](../../AssetsLibrary/alasset.md) object.
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
- [class func fetchKeyAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>?](./fetchkeyassets%28in,options%29.md)
  Retrieves assets marked as key assets in the specified asset collection.
- [class func fetchAssets(with: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28with%29.md)
  Retrieves all assets matching the specified options.
- [class func fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withburstidentifier,options%29.md)
  Retrieves assets with the specified burst photo sequence identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/fetchassets(withalasseturls:options:))*