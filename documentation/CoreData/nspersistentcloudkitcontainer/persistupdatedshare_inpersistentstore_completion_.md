# persistUpdatedShare:inPersistentStore:completion:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Saves the share record and schedules it for export to iCloud.

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
- (void) persistUpdatedShare:(CKShare *) share inPersistentStore:(NSPersistentStore *) persistentStore completion:(void (^)(CKShare *persistedShare, NSError *persistedShareError)) completion;
```

#### Discussion

The `completion` callback returns no value and takes the following parameters:

- The saved share record, or `nil` if the save fails.
- An error object that contains information about a problem, or `nil` if the share record saves successfully.

Core Data saves the share to the persistent store before this method returns, but doesn’t invoke the completion handler until after the export finishes.

> ❗ **Important**:  Whenever you modify a share record, save the changes using this method to keep the record and the local store’s metadata in sync.

## Parameters

- `share`: The share record to save.
- `persistentStore`: The persistent store that provides the database scope and the CloudKit container’s identifier. For more information, see [`NSPersistentCloudKitContainerOptions`](../nspersistentcloudkitcontaineroptions.md).
- `completion`: The handler to invoke after the export finishes.

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
- [- fetchSharesMatchingObjectIDs:error:](./fetchsharesmatchingobjectids_error_.md)
  Returns a dictionary that contains the share records that CloudKit associates with specified managed object IDs.
- [- shareManagedObjects:toShare:completion:](./sharemanagedobjects_toshare_completion_.md)
  Associates the specified managed objects with a new or existing share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/persistupdatedshare:inpersistentstore:completion:)*