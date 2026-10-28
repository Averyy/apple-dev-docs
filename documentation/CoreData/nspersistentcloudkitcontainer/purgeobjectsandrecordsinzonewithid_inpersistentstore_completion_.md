# purgeObjectsAndRecordsInZoneWithID:inPersistentStore:completion:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Deletes all CloudKit records in the specified record zone, along with their corresponding managed objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (void) purgeObjectsAndRecordsInZoneWithID:(CKRecordZoneID *) zoneID inPersistentStore:(NSPersistentStore *) persistentStore completion:(void (^)(CKRecordZoneID *purgedZoneID, NSError *purgeError)) completion;
```

## Discussion

The `completion` callback returns no value and takes the following parameters:

- The ID of the purged record zone, or `nil` if the purge fails.
- An error object that contains information about a problem, or `nil` if Core Data successfully purges the record zone.

If `persistentStore` is `nil`, the method invokes the completion handler once for each of the persistent container’s stores that manages a CloudKit database.

## Parameters

- `zoneID`: The ID of the record zone to purge.
- `persistentStore`: The persistent store that manages the CloudKit database containing the record zone. Use `nil` to attempt the purge in each of the container’s persistent stores that manages a CloudKit database.
- `completion`: The handler to invoke after Core Data purges the CloudKit records and managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/purgeobjectsandrecordsinzonewithid:inpersistentstore:completion:)*