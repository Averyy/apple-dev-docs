# CKAsset

**Framework**: CloudKit  
**Kind**: class

An external file that belongs to a record.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKAsset
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)

#### Overview

Use assets to incorporate external files into your app’s records, such as photos, videos, and binary files. Alternatively, use assets when a field’s value is more than a few kilobytes in size. To associate an instance of [`CKAsset`](ckasset.md) with a record, assign it to one of its fields.

> **Note**:  CloudKit stores only an asset’s data. If you require its filename, or any other file-system metadata, use one or more separate fields on the record to store it.

 CloudKit stores only an asset’s data. If you require its filename, or any other file-system metadata, use one or more separate fields on the record to store it.

CloudKit stores an asset’s data separately from a record that references it, but maintains an association with that record. When you save a record that has an asset, CloudKit saves both the record and the asset to the server. Similarly, when you fetch the record, the server returns the record and the asset.

When you fetch a record that contains an asset, CloudKit stores the asset’s data in a staging area accessible to your app. Use the asset’s [`fileURL`](ckasset/fileurl.md) property to access its staged location. The system regularly deletes files in the staging area to reclaim disk space. To avoid this behavior, move the data into your app’s container as soon as you fetch it.

If you don’t require the asset when retrieving records, use the operation’s `desiredKeys` property to exclude the field. For more information, see [`CKFetchRecordsOperation`](ckfetchrecordsoperation.md), [`CKQueryOperation`](ckqueryoperation.md), and [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md).

If you no longer require an asset that’s on the server, you don’t delete it. Instead, orphan the asset by setting any fields that contain the asset to `nil` and then saving the record. CloudKit periodically deletes orphaned assets from the server.

## Topics

### Creating an Asset
- [init(fileURL: URL)](ckasset/init(fileurl:).md)
  Creates an asset that references a file.
### Getting the URL of the Asset
- [var fileURL: URL?](ckasset/fileurl.md)
  The URL for accessing the asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CKRecordValueProtocol](ckrecordvalueprotocol.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)
  Create a schema to store your app’s objects as records in iCloud using CloudKit.
- [Managing iCloud Containers with CloudKit Database App](managing-icloud-containers-with-cloudkit-database-app.md)
  Inspect and modify the schema and data for your app’s iCloud container.
- [class CKRecordZone](ckrecordzone.md)
  A database partition that contains related records.
- [class CKRecord](ckrecord.md)
  A collection of key-value pairs that store your app’s data.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [Integrating a Text-Based Schema into Your Workflow](integrating-a-text-based-schema-into-your-workflow.md)
  Define and update your schema with the CloudKit Schema Language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckasset)*