# getStatusRelativeToAssetPack:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets the current status relative to a particular asset pack.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```objc
- (void) getStatusRelativeToAssetPack:(BAAssetPack *) assetPack completionHandler:(void (^)(BAAssetPackStatus status, NSError *error)) completionHandler;
```

#### Discussion

This method checks whether any version of the specified asset pack is currently downloaded. If one is, then it determines the version relationship between the downloaded asset pack and the specified asset pack. If they have different version numbers, then the status value that it passes to the completion handler will contain [`BAAssetPackStatusOutOfDate`](../baassetpackstatus/baassetpackstatusoutofdate.md). The status value will contain [`BAAssetPackStatusUpdateAvailable`](../baassetpackstatus/baassetpackstatusupdateavailable.md) only if the relevant asset pack on the server hasn’t been further updated since the initialization of the provided [`BAAssetPack`](../baassetpack.md) instance.

For example, consider the following sequence of events, assuming that version 1 of the relevant asset pack is already available locally:

1. Your application calls [`assetPackWithIdentifier:`](../baassetpackmanifest/assetpackwithidentifier_.md) on the [`BAAssetPackManifest`](../baassetpackmanifest.md) object that [`getManifestWithCompletionHandler:`](./getmanifestwithcompletionhandler_.md) passes to its completion handler to obtain a [`BAAssetPack`](../baassetpack.md) instance.
2. The asset pack is updated to version 2 on the server.
3. Your application calls this method, passing the [`BAAssetPack`](../baassetpack.md) instance from step 1.

In this case, the status value will indicate that the downloaded asset pack is up to date. Generally, you shouldn’t need to handle this type of situation explicitly because the system automatically polls for updates periodically in the background.

This method doesn’t automatically trigger any downloads, updates, or removals.

## Parameters

- `assetPack`: The asset pack.
- `completionHandler`: A block that receives the current status relative to the asset pack or an error if one occurs.

## See Also

### Managing asset packs
- [- checkForUpdatesWithCompletionHandler:](./checkforupdateswithcompletionhandler_.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [- ensureLocalAvailabilityOfAssetPack:completionHandler:](./ensurelocalavailabilityofassetpack_completionhandler_.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.
- [- ensureLocalAvailabilityOfAssetPacks:completionHandler:](./ensurelocalavailabilityofassetpacks_completionhandler_.md)
  Ensures that the specified asset packs are available locally.
- [- ensureLocalAvailabilityOfAssetPack:requireLatestVersion:completionHandler:](./ensurelocalavailabilityofassetpack_requirelatestversion_completionhandler_.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.
- [- ensureLocalAvailabilityOfAssetPacks:requireLatestVersions:completionHandler:](./ensurelocalavailabilityofassetpacks_requirelatestversions_completionhandler_.md)
  Ensures that the specified asset packs are available locally, performing a batch download if necessary.
- [- assetPackIsAvailableLocallyWithIdentifier:](./assetpackisavailablelocallywithidentifier_.md)
  Checks whether the asset pack with the specified identifier is available locally.
- [- getLocalStatusOfAssetPackWithIdentifier:completionHandler:](./getlocalstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s local status.
- [- removeAssetPackWithIdentifier:completionHandler:](./removeassetpackwithidentifier_completionhandler_.md)
  Removes the specified asset pack from the device.
- [- getStatusOfAssetPackWithIdentifier:completionHandler:](./getstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getstatusrelativetoassetpack:completionhandler:)*