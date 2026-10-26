# BADownload

**Framework**: Background Assets  
**Kind**: class  
**Role**: Class

An object that represents an in-progress or concluded asset download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class BADownload
```

```objc
@interface BADownload : NSObject
```

#### Overview

> **Note**:  You don’t create instances of this object directly. Instead, use an object that inherits from [`BADownload`](./badownload.md), such as [`BAURLDownload`](./baurldownload.md).

## Topics

### Getting the identity
- [var identifier: String](./badownload/identifier.md)
  The app-specific string that uniquely identifies the downloadable asset.
- [var uniqueIdentifier: String](./badownload/uniqueidentifier.md)
  The system-provided string that uniquely identifies the download object.
### Determining the priority
- [var isEssential: Bool](./badownload/isessential.md)
- [var priority: BADownload.Priority](./badownload/priority-swift.property.md)
  The download’s execution priority.
- [BADownload.Priority](./badownload/priority-swift.struct.md)
  A type that determines the execution priority of a scheduled asset download.
### Getting the current state
- [var state: BADownload.State](./badownload/state-swift.property.md)
  The current state of the download.
- [BADownload.State](./badownload/state-swift.enum.md)
  Constants that indicate the state of a download.
### Downloading nonessential assets
- [func removingEssential() -> Self](./badownload/removingessential%28%29.md)
### Initializers
- [init?(coder: NSCoder)](./badownload/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [BAURLDownload](./baurldownload.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Unmanaged asset downloads
- [Configuring an unmanaged Background Assets project](./configuring-an-unmanaged-background-assets-project.md)
  Manage and download individual assets yourself by configuring your app and extension targets.
- [Downloading essential assets in the background](./downloading-essential-assets-in-the-background.md)
  Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.
- [BAManifestURL](../BundleResources/information-property-list/bamanifesturl.md)
  The location URL of the app’s manifest file that contains the names and sizes of assets.
- [BAInitialDownloadRestrictions](../BundleResources/information-property-list/bainitialdownloadrestrictions.md)
  The restrictions that apply to the set of assets that download immediately after app installation.
- [BAEssentialMaxInstallSize](../BundleResources/information-property-list/baessentialmaxinstallsize.md)
  The combined, maximum size of the essential assets that the system downloads before it launches your app in bytes.
- [BAMaxInstallSize](../BundleResources/information-property-list/bamaxinstallsize.md)
  The combined, maximum size, in bytes, of the non-essential assets that download immediately after app installation.
- [class BADownloadManager](./badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtension](./badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [protocol BADownloaderExtensionConfiguration](./badownloaderextensionconfiguration.md)
- [class BAURLDownload](./baurldownload.md)
  An object that represents a remote asset to download.
- [BADownloaderExtension](./badownloaderextension-zuvm.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownload)*