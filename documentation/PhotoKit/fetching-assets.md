# Fetching Assets

**Framework**: PhotoKit  
**Role**: Article

Retrieve asset metadata or request full asset content.

## Overview

You fetch assets to begin working with them. Use the class methods listed in Fetching Assets to retrieve one or more [`PHAsset`](../Photos/phasset.md) instances representing the assets you want to display or edit. For example, to fetch all the assets in an asset collection (such as an album or moment), use the [`fetchAssets(in:options:)`](../Photos/phasset/fetchassets%28in,options%29.md) method. Each fetch method takes a [`PHFetchOptions`](../Photos/phfetchoptions.md) parameter that you use to specify the assets to retrieve and how to sort them.

> ❗ **Important**:  Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in Fetching Assets, Photos automatically prompts the user for authorization. Alternatively, you can use the [`PHPhotoLibrary`](../Photos/phphotolibrary.md) [`requestAuthorization(_:)`](../Photos/phphotolibrary/requestauthorization%28_%29.md) method to prompt the user at a time of your choosing. For more information, see `Requesting Authorization to Access Photos`.

## See Also

### Fetching Assets
- [class func fetchAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](../Photos/phasset/fetchassets%28in,options%29.md)
  Retrieves assets from the specified asset collection.
- [class func fetchAssets(with: PHAssetMediaType, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](../Photos/phasset/fetchassets%28with,options%29.md)
  Retrieves assets with the specified media type.
- [class func fetchAssets(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](../Photos/phasset/fetchassets%28withlocalidentifiers,options%29.md)
  Retrieves assets with the specified local-device-specific unique identifiers.
- [class func fetchKeyAssets(in: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>?](../Photos/phasset/fetchkeyassets%28in,options%29.md)
  Retrieves assets marked as key assets in the specified asset collection.
- [class func fetchAssets(with: PHFetchOptions?) -> PHFetchResult<PHAsset>](../Photos/phasset/fetchassets%28with%29.md)
  Retrieves all assets matching the specified options.
- [class func fetchAssets(withBurstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>](../Photos/phasset/fetchassets%28withburstidentifier,options%29.md)
  Retrieves assets with the specified burst photo sequence identifier.
- [class func fetchAssets(withALAssetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>](../Photos/phasset/fetchassets%28withalasseturls,options%29.md)
  Retrieves assets using URLs provided by the Assets Library framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/fetching-assets)*