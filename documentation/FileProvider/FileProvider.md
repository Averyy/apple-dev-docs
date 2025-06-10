# File Provider

**Framework**: File Provider  
**Kind**: module

An extension other apps use to access files and folders managed by your app and synced with a remote storage.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

#### Overview

If your app focuses on providing and syncing user documents from remote storage, you can implement a File Provider extension to give users access to those documents when they’re using other apps. If you just need to share local documents, see [`Share files locally`](https://developer.apple.com/documentation/fileprovider#Share-files-locally) below.

![A diagram that depicts the interaction between an app and your server facilitated by a File Provider extension. The app communicates with the document browser, which requests data to the File Provider extension. The File Provider extension syncs updates with the remote server.](https://docs-assets.developer.apple.com/published/c49c1b9fc90a37cd06b9a7b6f73912d9/media-4032695%402x.png)

The framework has two different starting points for building your File Provider extension.

The replicated extension takes responsibility for monitoring and managing the local copies of your documents. The file provider focuses on syncing data between the local copy and the remote storage—uploading any local changes and downloading any remote changes. For more information, see [`Replicated File Provider extension`](replicated-file-provider-extension.md).

The nonreplicated extension manages a local copy of the extension’s content, including creating and managing placeholders for remote files. It also syncs the content with your remote storage. For more information, see [`Nonreplicated File Provider extension`](nonreplicated-file-provider-extension.md).

##### Share Files Locally

You don’t need a File Provider extension to allow access to documents that your app stores locally.

In iOS, to give other apps access to the files in your `Documents` directory, set the following keys in your app’s Info tab or its `Info.plist` file. For document browser-based apps, set the [`UISupportsDocumentBrowser`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW37) key. For all other apps, set both the [`UIFileSharingEnabled`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW20) and [`LSSupportsOpeningDocumentsInPlace`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSSupportsOpeningDocumentsInPlace) keys.

After you set these keys, other apps can open and edit the contents of your `Documents` directory in place. Your files also appear in both the Files app and the document browser. For more information, see the [`UIDocumentBrowserViewController`](https://developer.apple.com/documentation/UIKit/UIDocumentBrowserViewController) class.

## Topics

### Essentials
- [File Provider updates](../Updates/FileProvider.md)
  Learn about important changes to File Provider.
### Extension types
- [Replicated File Provider extension](replicated-file-provider-extension.md)
  Build a File Provider extension that syncs the local copies of your files with your remote storage.
- [Nonreplicated File Provider extension](nonreplicated-file-provider-extension.md)
  Build a File Provider extension that hosts and manages the user’s local files.
### Extension management
- [class NSFileProviderManager](nsfileprovidermanager.md)
  A manager object that you use to communicate with the file provider from either your app or your File Provider extension.
### Provided items
- [typealias NSFileProviderItem](nsfileprovideritem-swift.typealias.md)
  An item the File Provider extension manages.
- [protocol NSFileProviderItemProtocol](nsfileprovideritemprotocol.md)
  A protocol that defines the properties of an item managed by the File Provider extension.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [struct NSFileProviderItemCapabilities](nsfileprovideritemcapabilities.md)
  An item’s capabilities, which define the actions that the user can perform in the document browser.
- [struct NSFileProviderTypeAndCreator](nsfileprovidertypeandcreator.md)
  A structure that contains the file type and file creator codes for an item.
### Cloud search
- [protocol NSFileProviderSearching](nsfileprovidersearching.md)
  A protocol you implement to support searching in your file provider.
### Domains
- [class NSFileProviderDomain](nsfileproviderdomain.md)
  A File Provider extension’s domain.
### Errors
- [struct NSFileProviderError](nsfileprovidererror.md)
  A structure that contains information about File Provider extension errors.
- [NSFileProviderError.Code](nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [let NSFileProviderErrorDomain: String](nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorItemKey: String](nsfileprovidererroritemkey.md)
  The key for accessing information about sync-related errors.
- [let NSFileProviderErrorNonExistentItemIdentifierKey: String](nsfileprovidererrornonexistentitemidentifierkey.md)
  The key for accessing the specified item’s identifier when the item doesn’t exist.
- [let NSFileProviderErrorCollidingItemKey: String](nsfileprovidererrorcollidingitemkey.md)
  The key for accessing the existing item from a filename collision error’s user info dictionary.
### Data export
- [Exporting file provider metrics data](exporting-file-provider-metrics-data.md)
  Download and analyze usage, consistency, and error data.
### Global variables and macros
- [Global variables and macros](global-variables-and-macros.md)
### Structures
- [struct NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason.md)
  Constants that describe why an external volume might not be eligible for storing a domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProvider)*