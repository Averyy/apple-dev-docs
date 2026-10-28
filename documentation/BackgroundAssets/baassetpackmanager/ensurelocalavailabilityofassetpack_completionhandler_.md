# ensureLocalAvailabilityOfAssetPack:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Ensures that the specified asset pack is available locally, performing a download if necessary.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) ensureLocalAvailabilityOfAssetPack:(BAAssetPack *) assetPack completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Discussion

This method checks whether the asset pack is currently downloaded. If it isn’t, then the system schedules it to be downloaded and calls the completion handler with `nil` for the the completion handler’s `error` parameter when the download finishes. The framework guarantees that the requested asset pack is available locally after this method calls the completion handler with `nil` for the `error` parameter. If this method calls the completion handler with a non-`nil` value for `error`, then the asset pack *isn’t* guaranteed to be available locally. You can optionally monitor download progress by attaching a delegate object to [`delegate`](./delegate.md).

To download multiple asset packs at the same time, use [`ensureLocalAvailabilityOfAssetPacks:completionHandler:`](./ensurelocalavailabilityofassetpacks_completionhandler_.md).

> **Note**: This method doesn’t check for updates. It’s equivalent to calling [`ensureLocalAvailabilityOfAssetPack:requireLatestVersion:completionHandler:`](./ensurelocalavailabilityofassetpack_requirelatestversion_completionhandler_.md) and passing `NO` to the `shouldUpdate` parameter.

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.
- `completionHandler`: A block that’s called when the asset pack is available locally or that receives an error if one occurs.

## See Also

### Managing asset packs
- [- checkForUpdatesWithCompletionHandler:](./checkforupdateswithcompletionhandler_.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
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
- [- getStatusOfAssetPackWithIdentifier:completionHandler:](./getstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/ensurelocalavailabilityofassetpack:completionhandler:)*