# BAManagedDownloaderExtension

**Framework**: Background Assets  
**Kind**: protocol  
**Role**: Protocol

An application extension that uses the system implementation to schedule asset-pack downloads automatically.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@protocol BAManagedDownloaderExtension <BADownloaderExtension>
```

## Overview

The protocol provides default implementations for all of the inherited [`BADownloaderExtension`](./badownloaderextension-zuvm.md) requirements.

> ⚠️ **Warning**: Don’t implement any of the inherited [`BADownloaderExtension`](./badownloaderextension-zuvm.md) requirements aside from, optionally, [`backgroundDownload:didReceiveChallenge:completionHandler:`](./badownloaderextension-zuvm/backgrounddownload_didreceivechallenge_completionhandler_.md).

## Creating an Objective-C Downloader Extension

Xcode’s Background Download extension template generates Swift code when you select either the “Apple-Hosted, Managed” option or the “Self-Hosted, Managed” option, but you can easily switch to Objective-C instead if you prefer. To do so, follow these steps:

1. Remove `BackgroundDownloadHandler.swift`.
2. Create `DownloaderExtension.h` with the following contents:

   ### Apple Hosting

   ```objc
   #import <StoreKit/StoreKit.h>

   @interface DownloaderExtension : NSObject <SKDownloaderExtension>

   @end
   ```

   ### Self Hosting

   ```objc
   #import <BackgroundAssets/BackgroundAssets.h>

   @interface DownloaderExtension : NSObject <BAManagedDownloaderExtension>

   @end
   ```
3. Create `DownloaderExtension.m` with the following contents:

   ```objc
   #import "DownloaderExtension.h"

   @implementation DownloaderExtension

   - (BOOL)shouldDownloadAssetPack:(BAAssetPack *)assetPack {
       // Use this method to filter out asset packs that the system would otherwise download automatically. You can also remove this method entirely if you just want to rely on the default download behavior.
       return true;
   }

   @end
   ```
4. Add `DownloaderExtension.m` to your extension’s target.
5. Add the following snippet inside your extension’s `Info.plist`’s `EXAppExtensionAttributes` dictionary:

   ```plist
   <key>EXPrincipalClass</key>
   <string>DownloaderExtension</string>
   ```
6. Check that the downloader extension’s target explicitly links the Background Assets framework under Frameworks and Libraries in the target editor’s General tab. If it doesn’t, then click to add an item to the list. Select “BackgroundAssets.framework” under Apple SDKs, then click Add.

## Topics

### Downloading asset packs
- [- shouldDownloadAssetPack:](./bamanageddownloaderextension/shoulddownloadassetpack_.md)
  Determines whether to download an asset pack.

## Relationships

### Inherits From
- [BADownloaderExtension](./badownloaderextension-zuvm.md)

## See Also

### Managed asset packs
- [BAAssetPack](./baassetpack.md)
  An archive of assets that the system downloads together.
- [BAAssetPackStatus](./baassetpackstatus.md)
  The status of an asset pack.
- [BAAssetPackManager](./baassetpackmanager.md)
  A class that manages asset packs.
- [BAAssetPackManifest](./baassetpackmanifest.md)
  A manifest of asset packs that are available to download.
- [BAManagedAssetPackDownloadDelegate](./bamanagedassetpackdownloaddelegate.md)
  An object that handles status updates when downloading an asset pack.
- [BAAppGroupID](../BundleResources/information-property-list/baappgroupid.md)
  The app group identifier that you share between your app and the extension that uses asset packs.
- [BAHasManagedAssetPacks](../BundleResources/information-property-list/bahasmanagedassetpacks.md)
  A Boolean value that indicates whether you let the system automatically manage your asset packs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bamanageddownloaderextension)*