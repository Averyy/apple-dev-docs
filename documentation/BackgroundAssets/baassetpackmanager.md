# BAAssetPackManager

**Framework**: Background Assets  
**Kind**: class  
**Role**: Class

A class that manages asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface BAAssetPackManager : NSObject
```

## Mentions

- [Reducing download and storage demands with localized asset packs](./reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Overview

The first time that your code refers to the shared manager, Background Assets considers that your application is opting into automatic system management of your asset packs.

> ❗ **Important**: When using the asset-pack manager, make sure that you also adopt the corresponding managed extension protocol. For applications that use Apple hosting, the corresponding protocol is `SKDownloaderExtension` from StoreKit. For other applications, the corresponding protocol is [`BAManagedDownloaderExtension`](./bamanageddownloaderextension.md). Not adopting the right protocol is a programmer error.

## Topics

### Getting the shared manager
- [sharedManager](./baassetpackmanager/sharedmanager.md)
  The shared asset-pack manager.
### Tracking downloads
- [delegate](./baassetpackmanager/delegate.md)
  An object that receives notifications about events that occur as an asset pack is downloaded.
- [BAManagedAssetPackDownloadDelegate](./bamanagedassetpackdownloaddelegate.md)
  An object that handles status updates when downloading an asset pack.
### Accessing asset packs
- [- getManifestWithCompletionHandler:](./baassetpackmanager/getmanifestwithcompletionhandler_.md)
  Gets the manifest of asset packs that are available to download.
- [BAAssetPackManifest](./baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [- getAllAssetPacksWithCompletionHandler:](./baassetpackmanager/getallassetpackswithcompletionhandler_.md)
  Gets the asset packs that are available to download.
- [- getAssetPackWithIdentifier:completionHandler:](./baassetpackmanager/getassetpackwithidentifier_completionhandler_.md)
  Gets the asset pack with the given identifier.
### Accessing asset contents
- [- contentsAtPath:searchingInAssetPackWithIdentifier:options:error:](./baassetpackmanager/contentsatpath_searchinginassetpackwithidentifier_options_error_.md)
  Returns the contents of an asset file at the specified relative path.
- [- contentsAtPath:asLocalizedForLanguage:options:error:](./baassetpackmanager/contentsatpath_aslocalizedforlanguage_options_error_.md)
  Returns the contents of a localized asset file at the specified relative path.
- [- fileDescriptorForPath:searchingInAssetPackWithIdentifier:error:](./baassetpackmanager/filedescriptorforpath_searchinginassetpackwithidentifier_error_.md)
  Opens and returns a file descriptor for the asset file at the specified relative path.
- [- fileDescriptorForPath:asLocalizedForLanguage:error:](./baassetpackmanager/filedescriptorforpath_aslocalizedforlanguage_error_.md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [- URLForPath:error:](./baassetpackmanager/urlforpath_error_.md)
  Returns a URL for the specified relative path.
- [- URLForPath:asLocalizedForLanguage:error:](./baassetpackmanager/urlforpath_aslocalizedforlanguage_error_.md)
  Returns a URL for the specified relative path.
### Managing asset packs
- [- checkForUpdatesWithCompletionHandler:](./baassetpackmanager/checkforupdateswithcompletionhandler_.md)
  Gets the latest asset-pack information from the server, updates outdated asset packs, and removes obsolete asset packs.
- [- ensureLocalAvailabilityOfAssetPack:completionHandler:](./baassetpackmanager/ensurelocalavailabilityofassetpack_completionhandler_.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.
- [- ensureLocalAvailabilityOfAssetPacks:completionHandler:](./baassetpackmanager/ensurelocalavailabilityofassetpacks_completionhandler_.md)
  Ensures that the specified asset packs are available locally.
- [- ensureLocalAvailabilityOfAssetPack:requireLatestVersion:completionHandler:](./baassetpackmanager/ensurelocalavailabilityofassetpack_requirelatestversion_completionhandler_.md)
  Ensures that the specified asset pack is available locally, performing a download if necessary.
- [- ensureLocalAvailabilityOfAssetPacks:requireLatestVersions:completionHandler:](./baassetpackmanager/ensurelocalavailabilityofassetpacks_requirelatestversions_completionhandler_.md)
  Ensures that the specified asset packs are available locally, performing a batch download if necessary.
- [- assetPackIsAvailableLocallyWithIdentifier:](./baassetpackmanager/assetpackisavailablelocallywithidentifier_.md)
  Checks whether the asset pack with the specified identifier is available locally.
- [- getStatusRelativeToAssetPack:completionHandler:](./baassetpackmanager/getstatusrelativetoassetpack_completionhandler_.md)
  Gets the current status relative to a particular asset pack.
- [- getLocalStatusOfAssetPackWithIdentifier:completionHandler:](./baassetpackmanager/getlocalstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s local status.
- [- removeAssetPackWithIdentifier:completionHandler:](./baassetpackmanager/removeassetpackwithidentifier_completionhandler_.md)
  Removes the specified asset pack from the device.
- [- getStatusOfAssetPackWithIdentifier:completionHandler:](./baassetpackmanager/getstatusofassetpackwithidentifier_completionhandler_.md)
  Gets an asset pack’s status.
### Inspecting language support
- [- getLocallyAvailableLanguagesWithCompletionHandler:](./baassetpackmanager/getlocallyavailablelanguageswithcompletionhandler_.md)
  Gets the languages used by asset packs that are localized and are available locally.
- [resolvedLanguage](./baassetpackmanager/resolvedlanguage.md)
  The language asset packs that are localized for which the system automatically makes available locally, represented as a BCP-47 identifier.
- [- reconcilePreferredLanguagesWithCompletionHandler:](./baassetpackmanager/reconcilepreferredlanguageswithcompletionhandler_.md)
  Reconciles the set of locally available asset packs with the current preferred languages.
### Instance Methods
- [- getLocalSizeOfAssetPackWithIdentifier:calculationMethod:completionHandler:](./baassetpackmanager/getlocalsizeofassetpackwithidentifier_calculationmethod_completionhandler_.md)
  Calculates a locally available asset pack’s installation size.
- [- localVersionOfAssetPackWithIdentifier:error:](./baassetpackmanager/localversionofassetpackwithidentifier_error_.md)
  Returns a locally available asset pack’s version number.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Managed asset packs
- [BAAssetPack](./baassetpack.md)
  An archive of assets that the system downloads together.
- [BAAssetPackStatus](./baassetpackstatus.md)
  The status of an asset pack.
- [BAAssetPackManifest](./baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [BAManagedDownloaderExtension](./bamanageddownloaderextension.md)
  An application extension that uses the system implementation to schedule asset-pack downloads automatically.
- [BAManagedAssetPackDownloadDelegate](./bamanagedassetpackdownloaddelegate.md)
  An object that handles status updates when downloading an asset pack.
- [BAAppGroupID](../BundleResources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager)*