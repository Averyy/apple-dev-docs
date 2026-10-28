# File Provider

**Framework**: File Provider  
**Kind**: module  
**Role**: Framework

An extension other apps use to access files and folders managed by your app and synced with a remote storage.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Overview

If your app focuses on providing and syncing user documents from remote storage, you can implement a File Provider extension to give users access to those documents when they’re using other apps. If you just need to share local documents, see [Share files locally](./FileProvider.md#Share-files-locally) below.

![A diagram that depicts the interaction between an app and your server facilitated by a File Provider extension. The app communicates with the document browser, which requests data to the File Provider extension. The File Provider extension syncs updates with the remote server.](https://developer.apple.com/tutorials/images/com.apple.fileprovider/media-4032695@2x.png)

The framework has two different starting points for building your File Provider extension.

- **[`NSFileProviderReplicatedExtension`](./nsfileproviderreplicatedextension.md)**: The system manages the content accessed through the File Provider extension. Available in macOS 11+ and iOS 16+.
- **[`NSFileProviderExtension`](./nsfileproviderextension.md)**: The extension hosts and manages the files accessed through the File Provider extension. Available in iOS 11+.

The replicated extension takes responsibility for monitoring and managing the local copies of your documents. The file provider focuses on syncing data between the local copy and the remote storage—uploading any local changes and downloading any remote changes. For more information, see [Replicated File Provider extension](./replicated-file-provider-extension.md).

The nonreplicated extension manages a local copy of the extension’s content, including creating and managing placeholders for remote files. It also syncs the content with your remote storage. For more information, see [Nonreplicated File Provider extension](./nonreplicated-file-provider-extension.md).

### Share files locally

You don’t need a File Provider extension to allow access to documents that your app stores locally.

In iOS, to give other apps access to the files in your `Documents` directory, set the following keys in your app’s Info tab or its `Info.plist` file. For document browser-based apps, set the [UISupportsDocumentBrowser](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW37) key. For all other apps, set both the [UIFileSharingEnabled](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW20) and [LSSupportsOpeningDocumentsInPlace](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSSupportsOpeningDocumentsInPlace) keys.

After you set these keys, other apps can open and edit the contents of your `Documents` directory in place. Your files also appear in both the Files app and the document browser. For more information, see the [`UIDocumentBrowserViewController`](../UIKit/uidocumentbrowserviewcontroller.md) class.

## Topics

### Essentials
- [File Provider updates](../Updates/fileprovider.md)
  Learn about important changes to File Provider.
### Extension types
- [Replicated File Provider extension](./replicated-file-provider-extension.md)
  Build a File Provider extension that syncs the local copies of your files with your remote storage.
- [Nonreplicated File Provider extension](./nonreplicated-file-provider-extension.md)
  Build a File Provider extension that hosts and manages the user’s local files.
### Extension management
- [class NSFileProviderManager](./nsfileprovidermanager.md)
  A manager object that you use to communicate with the file provider from either your app or your File Provider extension.
### Provided items
- [typealias NSFileProviderItem](./nsfileprovideritem-swift.typealias.md)
  An item the File Provider extension manages.
- [protocol NSFileProviderItemProtocol](./nsfileprovideritemprotocol.md)
  A protocol that defines the properties of an item managed by the File Provider extension.
- [struct NSFileProviderItemIdentifier](./nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [struct NSFileProviderItemCapabilities](./nsfileprovideritemcapabilities.md)
  An item’s capabilities, which define the actions that the user can perform in the document browser.
- [struct NSFileProviderTypeAndCreator](./nsfileprovidertypeandcreator.md)
  A structure that contains the file type and file creator codes for an item.
### Cloud search
- [protocol NSFileProviderSearching](./nsfileprovidersearching.md)
  A protocol you implement to support searching in your file provider.
### Domains
- [class NSFileProviderDomain](./nsfileproviderdomain.md)
  A File Provider extension’s domain.
### Errors
- [struct NSFileProviderError](./nsfileprovidererror.md)
  A structure that contains information about File Provider extension errors.
- [NSFileProviderError.Code](./nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [let NSFileProviderErrorDomain: String](./nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorItemKey: String](./nsfileprovidererroritemkey.md)
  The key for accessing information about sync-related errors.
- [let NSFileProviderErrorNonExistentItemIdentifierKey: String](./nsfileprovidererrornonexistentitemidentifierkey.md)
  The key for accessing the specified item’s identifier when the item doesn’t exist.
- [let NSFileProviderErrorCollidingItemKey: String](./nsfileprovidererrorcollidingitemkey.md)
  The key for accessing the existing item from a filename collision error’s user info dictionary.
### Data export
- [Exporting file provider metrics data](./exporting-file-provider-metrics-data.md)
  Download and analyze usage, consistency, and error data.
### Structures
- [struct NSFileProviderUserInfoKey](./nsfileprovideruserinfokey.md)
- [struct NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason.md)
  Constants that describe why an external volume might not be eligible for storing a domain.
### Enumerations
- [enum NSFileProviderNamespacePolicy](./nsfileprovidernamespacepolicy.md)
### Global variables and macros
- [Global variables and macros](./global-variables-and-macros.md)
### Variables
- [NSFileProviderUserInfoExperimentIDKey](./nsfileprovideruserinfokey/experimentid.md)
  System interpreted user info key When setting a value to that user info on a domain, the system will ingest this value. If user has given their consent for telemetry, this value will be used to decorate telemetry messages sent by the FileProvider subsystem. The telemetry messages can be then later on retrieved by developers along with the other metrics through the CloudKit console as detailed here: https://developer.apple.com/documentation/fileprovider/exporting-file-provider-metrics-data?language=objc This will help developers triaging data they receive from testing population compared to regular users The value must either be a NSNumber between [0 - 31]. If it’s not in that range, or if it is not a NSNumber, any call to addDomain with that invalid UserInfo dictionary will fail with a EINVAL POSIX NSError. To update this value, the provider must call addDomain with an updated userInfo dictionary
### Macros
- [FILEPROVIDER_API_AVAILABILITY_FEEDBACK](./fileprovider_api_availability_feedback.md)
- [FILEPROVIDER_API_AVAILABILITY_SEARCH](./fileprovider_api_availability_search.md)
- [FILEPROVIDER_API_AVAILABILITY_SYNC_CONTROLS](./fileprovider_api_availability_sync_controls.md)
- [FILE_PROVIDER_AVAILABILITY_NAMESPACE_POLICY](./file_provider_availability_namespace_policy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProvider)*