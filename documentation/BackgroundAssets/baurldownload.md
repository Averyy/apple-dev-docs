# BAURLDownload

**Framework**: Background Assets  
**Kind**: class  
**Role**: Class

An object that represents a remote asset to download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class BAURLDownload
```

```objc
@interface BAURLDownload : BADownload
```

## Topics

### Creating a download
- [init(identifier: String, request: URLRequest, essential: Bool, fileSize: Int, applicationGroupIdentifier: String, priority: BADownload.Priority)](./baurldownload/init%28identifier,request,essential,filesize,applicationgroupidentifier,priority%29.md)
- [convenience init(identifier: String, request: URLRequest, fileSize: Int, applicationGroupIdentifier: String)](./baurldownload/init%28identifier,request,filesize,applicationgroupidentifier%29.md)
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String)](./baurldownload/init%28identifier,request,applicationgroupidentifier%29.md)
  Creates a download that uses the specified identifier and App Group.
- [convenience init(identifier: String, request: URLRequest, applicationGroupIdentifier: String, priority: BADownload.Priority)](./baurldownload/init%28identifier,request,applicationgroupidentifier,priority%29.md)
  Creates a prioritized download that uses the specified identifier and App Group.

## Relationships

### Inherits From
- [BADownload](./badownload.md)
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
- [class BADownload](./badownload.md)
  An object that represents an in-progress or concluded asset download.
- [BADownloaderExtension](./badownloaderextension-zuvm.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baurldownload)*