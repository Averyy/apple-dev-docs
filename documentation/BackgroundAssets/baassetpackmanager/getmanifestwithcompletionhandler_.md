# getManifestWithCompletionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets the manifest of asset packs that are available to download.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) getManifestWithCompletionHandler:(void (^)(BAAssetPackManifest *manifest, NSError *error)) completionHandler;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Parameters

- `completionHandler`: A block that receives the manifest or an error if one occurs.

## See Also

### Accessing asset packs
- [BAAssetPackManifest](../baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [- getAllAssetPacksWithCompletionHandler:](./getallassetpackswithcompletionhandler_.md)
  Gets the asset packs that are available to download.
- [- getAssetPackWithIdentifier:completionHandler:](./getassetpackwithidentifier_completionhandler_.md)
  Gets the asset pack with the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getmanifestwithcompletionhandler:)*