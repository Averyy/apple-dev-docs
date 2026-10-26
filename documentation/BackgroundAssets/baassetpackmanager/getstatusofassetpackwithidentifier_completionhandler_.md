# getStatusOfAssetPackWithIdentifier:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets an asset pack’s status.

**Availability**:
- iOS 26.0+ - Deprecated in 26.4
- iPadOS 26.0+ - Deprecated in 26.4
- Mac Catalyst 26.0+ - Deprecated in 26.4
- macOS 26.0+ - Deprecated in 26.4
- tvOS 26.0+ - Deprecated in 26.4
- visionOS 26.0+ - Deprecated in 26.4

## Declaration

```objc
- (void) getStatusOfAssetPackWithIdentifier:(NSString *) assetPackIdentifier completionHandler:(void (^)(BAAssetPackStatus status, NSError *error)) completionHandler;
```

#### Discussion

If no asset pack with the specified identifier is found, then the block will receive an `NSError` object with [`BAManagedErrorCodeAssetPackNotFound`](../bamanagederrorcode/bamanagederrorcodeassetpacknotfound.md) as its code for the `error` parameter. This method attempts to get the latest asset-pack information from the server. It doesn’t automatically trigger any downloads, updates, or removals.

## Parameters

- `assetPackIdentifier`: The asset pack’s identifier.
- `completionHandler`: A block that receives the asset pack’s status or an error if one occurs.

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
- [- getLocalStatusOfAssetPackWithIdentifier:completionHandler:](./getlocalstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s local status.
- [- removeAssetPackWithIdentifier:completionHandler:](./removeassetpackwithidentifier_completionhandler_.md)
  Removes the specified asset pack from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getstatusofassetpackwithidentifier:completionhandler:)*