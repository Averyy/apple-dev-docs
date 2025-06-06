# iCloud

**Framework**: Foundation

Manage files and key-value data that automatically synchronize among a user’s iCloud devices.

## Topics

### iCloud Storage
- [class FileManager](filemanager.md)
  A convenient interface to the contents of the file system, and the primary means of interacting with it.
- [protocol FileManagerDelegate](filemanagerdelegate.md)
  The interface a file manager’s delegate uses to intervene during operations or if an error occurs.
### App Preferences
- [class NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md)
  An iCloud-based container of key-value pairs you use to share data among instances of your app running on a user’s connected devices.
### File Search
- [class NSMetadataQuery](nsmetadataquery.md)
  A query that you perform against Spotlight metadata.
- [protocol NSMetadataQueryDelegate](nsmetadataquerydelegate.md)
  An interface that enables the delegate of a metadata query to provide substitute results or attributes.
- [class NSMetadataItem](nsmetadataitem.md)
  The metadata associated with a file.
### Entitlements
- [com.apple.developer.icloud-container-development-container-identifiers](../BundleResources/Entitlements/com.apple.developer.icloud-container-development-container-identifiers.md)
  The container identifiers for the iCloud development environment.
- [com.apple.developer.icloud-container-environment](../BundleResources/Entitlements/com.apple.developer.icloud-container-environment.md)
  The development or production environment to use for the iCloud containers.
- [iCloud Container Identifiers Entitlement](../BundleResources/Entitlements/com.apple.developer.icloud-container-identifiers.md)
  The container identifiers for the iCloud production environment.
- [iCloud Services Entitlement](../BundleResources/Entitlements/com.apple.developer.icloud-services.md)
  The iCloud services used by the app.
- [iCloud Key-Value Store Entitlement](../BundleResources/Entitlements/com.apple.developer.ubiquity-kvstore-identifier.md)
  The container identifier to use for iCloud key-value storage.
### Errors
- [iCloud Error Codes](icloud-error-codes.md)
  Error codes to expect when an iCloud-related error occurs.

## See Also

- [File System](file-system.md)
  Create, read, write, and examine files and folders in the file system.
- [Archives and Serialization](archives-and-serialization.md)
  Convert objects and values to and from property list, JSON, and other flat binary representations.
- [Preferences](preferences.md)
  Persistently store domain-scoped pieces of information for configuring your app.
- [Spotlight](spotlight.md)
  Search for files and other items on the local device, and index your app’s content for searching.
- [Optimizing Your App’s Data for iCloud Backup](optimizing-your-app-s-data-for-icloud-backup.md)
  Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/icloud)*