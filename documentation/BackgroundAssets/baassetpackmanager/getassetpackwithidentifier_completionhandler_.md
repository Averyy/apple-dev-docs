# getAssetPackWithIdentifier:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets the asset pack with the given identifier.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.0
- tvOS 26.0+ - Deprecated in 27.0
- visionOS 26.0+ - Deprecated in 27.0

## Declaration

```objc
- (void) getAssetPackWithIdentifier:(NSString *) assetPackIdentifier completionHandler:(void (^)(BAAssetPack *assetPack, NSError *error)) completionHandler;
```

## Discussion

If no asset pack with the given identifier is found, then the block will receive an `NSError` object with [`BAManagedErrorCodeAssetPackNotFound`](../bamanagederrorcode/bamanagederrorcodeassetpacknotfound.md) as its code for the `error` parameter. This method may attempt to get the latest asset-pack information from the server. To force the system to get the latest information from the server unconditionally, send [`checkForUpdatesWithCompletionHandler:`](./checkforupdateswithcompletionhandler_.md) to the shared asset-pack manager.

## Parameters

- `assetPackIdentifier`: The asset pack’s identifier.
- `completionHandler`: A block that receives the asset pack or an error if one occurs.

## See Also

### Accessing asset packs
- [- getManifestWithCompletionHandler:](./getmanifestwithcompletionhandler_.md)
  Gets the manifest of asset packs that are available to download.
- [BAAssetPackManifest](../baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [- getAllAssetPacksWithCompletionHandler:](./getallassetpackswithcompletionhandler_.md)
  Gets the asset packs that are available to download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getassetpackwithidentifier:completionhandler:)*