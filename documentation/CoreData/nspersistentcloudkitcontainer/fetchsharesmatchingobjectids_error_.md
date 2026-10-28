# fetchSharesMatchingObjectIDs:error:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary that contains the share records that CloudKit associates with specified managed object IDs.

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
- (NSDictionary<NSManagedObjectID *,CKShare *> *) fetchSharesMatchingObjectIDs:(NSArray<NSManagedObjectID *> *) objectIDs error:(NSError **) error;
```

## Return Value

A dictionary that uses `objectIDs` as its keys, and the associated share records as its values.

## Discussion

If a specified managed object doesn’t belong to a shared record zone, or if Core Data has yet to save the object to iCloud and, therefore, its record zone is unknown, the returned dictionary doesn’t include it.

Use a fetched share record to manage its participants and their permissions, or assign data directly to it. A share record is a subclass of [`CKRecord`](../../CloudKit/ckrecord.md), which means you can store any data you choose in the underlying record to meet your specific needs. For more information, see [`CKShare`](../../CloudKit/ckshare.md).

If you modify a share record, you must save it using the [`persistUpdatedShare:inPersistentStore:completion:`](./persistupdatedshare_inpersistentstore_completion_.md) method.

> **Note**:  This method fetches known share records only. It doesn’t attempt to discover additional record zones or share records in any of the persistent container’s CloudKit databases.

## Parameters

- `objectIDs`: An array of managed object IDs.
- `error`: On return, an error object that contains information about a problem, or `nil` if the method successfully fetches the share records.

## See Also

### Sharing Objects
- [Accepting Share Invitations in a SwiftUI App](../accepting-share-invitations-in-a-swiftui-app.md)
  Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.
- [- acceptShareInvitationsFromMetadata:intoPersistentStore:completion:](./acceptshareinvitationsfrommetadata_intopersistentstore_completion_.md)
  Accepts one or more invitations to participate in sharing using the specified metadata.
- [- fetchParticipantsMatchingLookupInfos:intoPersistentStore:completion:](./fetchparticipantsmatchinglookupinfos_intopersistentstore_completion_.md)
  Fetches all participants that match the specified critieria.
- [- fetchSharesInPersistentStore:error:](./fetchsharesinpersistentstore_error_.md)
  Returns an array that contains all share records in the specified persistent store.
- [- persistUpdatedShare:inPersistentStore:completion:](./persistupdatedshare_inpersistentstore_completion_.md)
  Saves the share record and schedules it for export to iCloud.
- [- shareManagedObjects:toShare:completion:](./sharemanagedobjects_toshare_completion_.md)
  Associates the specified managed objects with a new or existing share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/fetchsharesmatchingobjectids:error:)*