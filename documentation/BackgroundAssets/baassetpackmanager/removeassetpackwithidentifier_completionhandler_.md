# removeAssetPackWithIdentifier:completionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Removes the specified asset pack from the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) removeAssetPackWithIdentifier:(NSString *) assetPackIdentifier completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `assetPackIdentifier`: The asset pack’s identifier.
- `completionHandler`: A block that receives an error if one occurs.

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
- [- getStatusOfAssetPackWithIdentifier:completionHandler:](./getstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/removeassetpackwithidentifier:completionhandler:)*