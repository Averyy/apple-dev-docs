# fetchAssets(with:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves all assets matching the specified options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchAssets(with options: PHFetchOptions?) -> PHFetchResult<PHAsset>
```

```objc
+ (PHFetchResult<PHAsset *> *) fetchAssetsWithOptions:(PHFetchOptions *) options;
```

## Mentions

- [Observing Changes in the Photo Library](../../PhotoKit/observing-changes-in-the-photo-library.md)

## Return Value

A fetch result that contains the requested [`PHAsset`](../phasset.md) objects, or an empty fetch result if no objects match the request.

## Discussion

By default, fetch results do not include photos synced to the device through iTunes or stored in iCloud Shared Albums. To change this behavior, use the [`includeAssetSourceTypes`](../phfetchoptions/includeassetsourcetypes.md) property in the `options` parameter.

## Parameters

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
- [class func fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withburstidentifier,options%29.md)
  Retrieves assets with the specified burst photo sequence identifier.
- [class func fetchAssets(withALAssetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](./fetchassets%28withalasseturls,options%29.md)
  Retrieves assets using URLs provided by the Assets Library framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/fetchassets(with:))*