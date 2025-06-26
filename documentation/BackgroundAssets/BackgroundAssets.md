# Background Assets

**Framework**: Background Assets  
**Kind**: module

Schedule background downloads of large assets during or after app installation, when the app updates, and periodically while the app remains on-device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

#### Overview

With the Background Assets framework, you can improve the experience of your app or game by reducing or eliminating the time people have to wait while your app downloads any required assets at first launch. For example, a game might use the Background Assets framework to download additional content immediately after installation, such as level packs, 3D character models, and textures.

![A graphic containing the framework’s logo and several circular progress indicators that show the download status of additional content such as audio, images, and achievements. Each progress indicator displays an icon that represents that specific content type such as a music note for audio.](https://docs-assets.developer.apple.com/published/7192e3aef1127088ff61bfbac7978294/media-4132858%402x.png)

> **Note**:  For compatible iPad and iPhone apps, Background Assets is available in visionOS 1.0 and later. For apps built for visionOS, Background Assets is available in visionOS 2.4 and later.

Add a Background Assets extension to your app’s target, and let the system notify that extension about an app installation or subsequent update. Then use the download manager to schedule background downloads of required content from your servers or content delivery network (CDN), and have those downloads finish even when the app isn’t running. Check for updated content when the system periodically launches the extension (dependent on app usage) and, when content is available, schedule it for immediate download. The framework leverages [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) and common types like [`URLRequest`](https://developer.apple.com/documentation/Foundation/URLRequest). For more information see, 2022 WWDC session 110403: [`Meet Background Assets`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/110403/)

> ❗ **Important**:  Use the framework only to download additional assets for your app; don’t use it for any other purposes. For example, don’t collect or transmit data to identify a user or device or to perform advertising or advertising measurement.

#### The Background Assets Extension Life Cycle

The system launches the extension during the first install and subsequent updates, before a person launches the app, and periodically in the background when the app isn’t running. The sequence of events are:

- A person installs or updates your app on the device.
- The system prevents the app from launching and begins downloading your manifest file using the URL you provide.
- During the manifest download, the system reports progress to the App Store.
- When the download completes, the system launches your app extension, sending it a content request with the location of the manifest file on disk.
- The extension uses the manifest file, which contains the asset URLs and file sizes, to return a set of download requests to the system.
- The system pauses, or terminates, the extension and begins the downloads.
- When the downloads complete, the system notifies the extension and allows the app to launch.

The flow for periodic content requests is identical to the app install and updates, except the system determines when periodic events occur, depending on a person’s usage and their system settings. For example, the system factors in whether a person enables the Low Power Mode and Background App Refresh settings.

## Topics

### Essentials
- [Configuring your Background Assets project](configuring-background-assets.md)
  Edit your app and extension targets in your Xcode project to use Background Assets.
- [BAManifestURL](../BundleResources/Information-Property-List/BAManifestURL.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAInitialDownloadRestrictions](../BundleResources/Information-Property-List/BAInitialDownloadRestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAEssentialMaxInstallSize](../BundleResources/Information-Property-List/BAEssentialMaxInstallSize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
- [BAMaxInstallSize](../BundleResources/Information-Property-List/BAMaxInstallSize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
### Apple-Hosted Background Assets
- [Downloading asset packs hosted by Apple](downloading-asset-packs-hosted-by-apple.md)
  Create asset packs, upload them to App Store Connect, and download them in your app.
- [Testing your asset packs locally](testing-asset-packs-locally.md)
  Test your asset packs using a local mock server.
### Asset download management
- [class BADownloadManager](badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtension](badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [protocol BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)
- [Downloading essential assets in the background](downloading-essential-assets-in-the-background.md)
  Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.
### Asset downloads
- [class BAURLDownload](baurldownload.md)
  An object that represents a remote asset to download.
- [class BADownload](badownload.md)
  An object that represents an in-progress or concluded asset download.
- [BADownload.Priority](badownload/priority-swift.struct.md)
  A type that determines the execution priority of a scheduled asset download.
### Errors
- [let BAErrorDomain: String](baerrordomain.md)
- [enum BAErrorCode](baerrorcode.md)
### Classes
- [actor AssetPackManager](assetpackmanager.md)
  An actor that manages asset packs.
### Protocols
- [protocol ManagedDownloaderExtension](manageddownloaderextension.md)
  A protocol to which a managed downloader extension must conform.
- [protocol ManagedDownloaderExtensionConfiguration](manageddownloaderextensionconfiguration.md)
### Structures
- [struct AssetPack](assetpack.md)
  An archive of assets that the system downloads together.
- [struct AssetPackManifest](assetpackmanifest.md)
  A representation of a manifest that lists asset packs that are available to download.
- [struct BAAssetPackStatus](baassetpackstatus.md)
  The status of an asset pack.
### Enumerations
- [enum ManagedBackgroundAssetsError](managedbackgroundassetserror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/BackgroundAssets)*