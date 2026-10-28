# fetchAssets(withBurstIdentifier:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves assets with the specified burst photo sequence identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchAssets(withBurstIdentifier burstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>
```

```objc
+ (PHFetchResult<PHAsset *> *) fetchAssetsWithBurstIdentifier:(NSString *) burstIdentifier options:(PHFetchOptions *) options;
```

## Return Value

A fetch result that contains the requested [`PHAsset`](../phasset.md) objects, or an empty fetch result if no objects match the request.

## Discussion

A burst photo sequence, as seen in the Photos app, corresponds to a group of Photos assets that share the same [`burstIdentifier`](./burstidentifier.md) string.

By default, the returned [`PHFetchResult`](../phfetchresult.md) object contains only the representative asset and any user-picked photos from the burst sequence. To retrieve all photos in the burst sequence, provide a [`PHFetchOptions`](../phfetchoptions.md) object containing a filter predicate.

## Parameters

- `burstIdentifier`: A burst identifier string, as provided by the [`burstIdentifier`](./burstidentifier.md) property of an asset.
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
- [class func fetchAssets(withALAssetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withalasseturls,options%29.md)
  Retrieves assets using URLs provided by the Assets Library framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/fetchassets(withburstidentifier:options:))*