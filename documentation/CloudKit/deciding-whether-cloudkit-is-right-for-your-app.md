# Deciding whether CloudKit is right for your app

**Framework**: CloudKit

Explore the various options you have for using iCloud to store and sync your app’s data.

#### Overview

Use iCloud to store your app’s data and make that data available on the web and on each device a person owns. iCloud provides a number of options for storing app data, where each option provides a different set of features and a varying amount of control over that data. Some options are easier to implement than others, so it’s important that you carefully consider each one and its suitability for your app before choosing CloudKit.

##### Store Documents Images and Other File Types in Icloud

If your app creates files such as documents and images, and you want those files to sync across a person’s devices, use iCloud Documents. You decide which files to sync by storing them in your app’s ubiquity container, and iCloud manages the persistence and synchronization of those files for you. For more information, see [`url(forUbiquityContainerIdentifier:)`](https://developer.apple.com/documentation/Foundation/FileManager/url(forUbiquityContainerIdentifier:)) and [`Configuring iCloud services`](https://developer.apple.com/documentation/Xcode/configuring-icloud-services).

In addition, the device’s owner can use iCloud Backup to store a snapshot of their device, including files that your app creates. That person can then restore an existing or new device from that snapshot. Even though your app isn’t explicitly participating in the system backup process, any files your app creates contribute to the backup’s overall size, and large backups may lead to longer restore times. If your app has files that the system doesn’t need to back up, such as temporary or cached files, use the available APIs to indicate to the system that it can ignore them. For more information, see [`Optimizing Your App’s Data for iCloud Backup`](https://developer.apple.com/documentation/Foundation/optimizing-your-app-s-data-for-icloud-backup).

##### Sync Preferences and Other Key Value Pairs Using Icloud

If your app maintains a set of feature flags or other lightweight configuration, or enables someone to customize the app’s look and feel, you may want to synchronize that state across a person’s devices to create a rich and consistent experience. Using iCloud key-value storage, your app can store a maximum of 1,024 string keys, with associated data, and iCloud automatically keeps those key-value pairs in sync. Key-value storage supports only numeric types, as well as [`Bool`](https://developer.apple.com/documentation/Swift/Bool), [`String`](https://developer.apple.com/documentation/Swift/String), [`Date`](https://developer.apple.com/documentation/Foundation/Date), [`Data`](https://developer.apple.com/documentation/Foundation/Data), [`Array`](https://developer.apple.com/documentation/Swift/Array), and [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary). For more information, see [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/Foundation/NSUbiquitousKeyValueStore).

##### Store Model Objects in Cloudkit

If your app manages a complex graph of model objects, which may include relationships between those objects, use one of the options in the following table:

| [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer) | If you don’t require granular control over how and when your data syncs, or your app already uses [`NSPersistentContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer) to persist data to disk, prefer this approach. [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer) provides a fully managed schema, maintains a local replica of your data, and supports the public, private, and shared databases. For more information, see [`Setting Up Core Data with CloudKit`](https://developer.apple.com/documentation/CoreData/setting-up-core-data-with-cloudkit). |
| --- | --- |
| [`CKSyncEngine`](cksyncengine-5sie5.md) | With a sync engine, you retain control of your data but the engine automatically schedules sync operations to fetch and send changes to that data. Your app participates in those operations by handling sync events and providing changed records when the engine requests them. Use [`CKSyncEngine`](cksyncengine-5sie5.md) with private and shared databases. |
| [`CKDatabase`](ckdatabase.md), [`CKOperation`](ckoperation.md), and related types | CloudKit’s base types provide full control over the data you store, and the design and management of your container’s schema. This approach, however, is the most intricate and requires you to manually fetch and send records, resolve any conflicts, schedule operations, handle iCloud account changes, process change notifications, persist server change tokens, and so on. For more information, see [`Enabling CloudKit in Your App`](enabling-cloudkit-in-your-app.md). |

## See Also

- [Enabling CloudKit in Your App](enabling-cloudkit-in-your-app.md)
  Configure your app to store data in iCloud using CloudKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app)*