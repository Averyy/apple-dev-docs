# ensureLocalAvailabilityOfAssetPack:requireLatestVersion:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Ensures that the specified asset pack is available locally, performing a download if necessary.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```objc
- (void) ensureLocalAvailabilityOfAssetPack:(BAAssetPack *) assetPack requireLatestVersion:(BOOL) shouldUpdate completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

This method checks whether the asset pack is currently downloaded. If it isn’t, then the system schedules it to be downloaded and calls the completion handler with `nil` for the completion handler’s `error` parameter when the download finishes. The framework guarantees that the requested asset pack is available locally after this method calls the completion handler with `nil` for the `error` parameter. If this method calls the completion handler with a non-`nil` value for `error`, then the asset pack *isn’t* guaranteed to be available locally. You can optionally monitor download progress by attaching a delegate object to [`delegate`](./delegate.md).

To download multiple asset packs at the same time, use [`ensureLocalAvailabilityOfAssetPack:requireLatestVersion:completionHandler:`](./ensurelocalavailabilityofassetpack_requirelatestversion_completionhandler_.md).

## Parameters

- `assetPack`: The asset pack the local availability of which to ensure.
- `shouldUpdate`: Whether to require that the latest version be available locally. When `YES` is passed to this parameter, the method will wait for the update (if there indeed is one available) to be downloaded before returning. When `NO` is passed, the method won’t check for updates and won’t attempt to download any.
- `completionHandler`: A block that’s called when the asset pack is available locally or that receives an error if one occurs.

## See Also

### Managing asset packs
- [- checkForUpdatesWithCompletionHandler:](./checkforupdateswithcompletionhandler_.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [- ensureLocalAvailabilityOfAssetPack:completionHandler:](./ensurelocalavailabilityofassetpack_completionhandler_.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.
- [- ensureLocalAvailabilityOfAssetPacks:completionHandler:](./ensurelocalavailabilityofassetpacks_completionhandler_.md)
  Ensures that the specified asset packs are available locally.
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

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/ensurelocalavailabilityofassetpack:requirelatestversion:completionhandler:)*