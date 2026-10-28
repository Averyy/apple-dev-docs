# ensureLocalAvailabilityOfAssetPacks:requireLatestVersions:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Ensures that the specified asset packs are available locally, performing a batch download if necessary.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) ensureLocalAvailabilityOfAssetPacks:(NSSet<BAAssetPack *> *) assetPacks requireLatestVersions:(BOOL) shouldUpdate completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Discussion

This method checks whether the asset packs are currently downloaded. If any aren’t, then the system schedules them to be downloaded and calls the completion handler with `nil` for the completion handler’s `error` parameter when all of the downloads finish. The framework guarantees that the requested asset packs are available locally after this method calls the completion handler with `nil` for the `error` parameter. If this method calls the completion handler with a non-`nil` value for `error`, then the asset packs *aren’t* all guaranteed to be available locally. You can optionally monitor download progress by attaching a delegate object to [`delegate`](./delegate.md).

## Parameters

- `assetPacks`: The asset packs the local availability of which to ensure.
- `shouldUpdate`: Whether to require that the respective latest versions be available locally. When `YES` is passed to this parameter, the method will wait for the updates (if there indeed are any available) to be downloaded before returning. When `NO` is passed, the method won’t check for updates and won’t attempt to download any.
- `completionHandler`: A block that’s called when the asset packs are all available locally or that receives an error if one occurs.

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

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/ensurelocalavailabilityofassetpacks:requirelatestversions:completionhandler:)*