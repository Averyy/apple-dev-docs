# getLocalStatusOfAssetPackWithIdentifier:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets an asset pack’s local status.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```objc
- (void) getLocalStatusOfAssetPackWithIdentifier:(NSString *) assetPackIdentifier completionHandler:(void (^)(BAAssetPackStatus status)) completionHandler;
```

## Discussion

This method checks only status values that are determinable offline. It doesn’t induce any network traffic or automatically trigger any downloads, updates, or removals. The following status values are determinable offline:

- [`BAAssetPackStatusOutOfDate`](../baassetpackstatus/baassetpackstatusoutofdate.md) (in some situations)
- [`BAAssetPackStatusObsolete`](../baassetpackstatus/baassetpackstatusobsolete.md) (in some situations)
- [`BAAssetPackStatusDownloaded`](../baassetpackstatus/baassetpackstatusdownloaded.md)

Because this method doesn’t communicate with the server, it can’t determine whether a particular asset pack exists in the first place. Instead, it returns an empty status value when provided a nonexistent asset-pack ID, which is indistinguishable from the situation in which the asset pack does indeed exist but hasn’t yet been downloaded. Use [`getStatusRelativeToAssetPack:completionHandler:`](./getstatusrelativetoassetpack_completionhandler_.md) to get a full view of the current status.

## Parameters

- `assetPackIdentifier`: The asset pack’s identifier.
- `completionHandler`: A block that receives the asset pack’s local status.

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
- [- getStatusRelativeToAssetPack:completionHandler:](./getstatusrelativetoassetpack_completionhandler_.md)
  Gets the current status relative to a particular asset pack.
- [- removeAssetPackWithIdentifier:completionHandler:](./removeassetpackwithidentifier_completionhandler_.md)
  Removes the specified asset pack from the device.
- [- getStatusOfAssetPackWithIdentifier:completionHandler:](./getstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getlocalstatusofassetpackwithidentifier:completionhandler:)*