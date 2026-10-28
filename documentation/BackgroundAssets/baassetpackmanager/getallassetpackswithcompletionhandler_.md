# getAllAssetPacksWithCompletionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets the asset packs that are available to download.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.0
- tvOS 26.0+ - Deprecated in 27.0
- visionOS 26.0+ - Deprecated in 27.0

## Declaration

```objc
- (void) getAllAssetPacksWithCompletionHandler:(void (^)(NSSet<BAAssetPack *> *assetPacks, NSError *error)) completionHandler;
```

## Discussion

This method may attempt to get the latest asset-pack information from the server.

## Parameters

- `completionHandler`: A block that receives the asset packs or an error if one occurs.

## See Also

### Accessing asset packs
- [- getManifestWithCompletionHandler:](./getmanifestwithcompletionhandler_.md)
  Gets the manifest of asset packs that are available to download.
- [BAAssetPackManifest](../baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [- getAssetPackWithIdentifier:completionHandler:](./getassetpackwithidentifier_completionhandler_.md)
  Gets the asset pack with the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getallassetpackswithcompletionhandler:)*