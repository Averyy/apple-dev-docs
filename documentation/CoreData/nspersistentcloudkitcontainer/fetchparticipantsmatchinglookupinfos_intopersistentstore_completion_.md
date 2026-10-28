# fetchParticipantsMatchingLookupInfos:intoPersistentStore:completion:

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Fetches all participants that match the specified critieria.

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
- (void) fetchParticipantsMatchingLookupInfos:(NSArray<CKUserIdentityLookupInfo *> *) lookupInfos intoPersistentStore:(NSPersistentStore *) persistentStore completion:(void (^)(NSArray<CKShareParticipant *> *fetchedParticipants, NSError *fetchError)) completion;
```

## Discussion

The `completion` handler returns no value and takes the following parameters:

- An array of fetched participants. For more information, see [`CKShare.Participant`](../../CloudKit/ckshare/participant.md).
- An error object that contains information about a problem, or `nil` if the method successfully fetches participants.

> **Note**:  To fetch participants, this method executes operations against [`CKContainer`](../../CloudKit/ckcontainer.md), and requires an active network connection.

## Parameters

- `lookupInfos`: An array of criteria that CloudKit uses to find participants. For more information, see [`CKUserIdentity.LookupInfo`](../../CloudKit/ckuseridentity/lookupinfo-swift.class.md).
- `persistentStore`: The persistent store that provides the CloudKit container’s identifier. For more information, see [`NSPersistentCloudKitContainerOptions`](../nspersistentcloudkitcontaineroptions.md).
- `completion`: The handler to invoke after the method fetches participants.

## See Also

### Sharing Objects
- [Accepting Share Invitations in a SwiftUI App](../accepting-share-invitations-in-a-swiftui-app.md)
  Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.
- [- acceptShareInvitationsFromMetadata:intoPersistentStore:completion:](./acceptshareinvitationsfrommetadata_intopersistentstore_completion_.md)
  Accepts one or more invitations to participate in sharing using the specified metadata.
- [- fetchSharesInPersistentStore:error:](./fetchsharesinpersistentstore_error_.md)
  Returns an array that contains all share records in the specified persistent store.
- [- fetchSharesMatchingObjectIDs:error:](./fetchsharesmatchingobjectids_error_.md)
  Returns a dictionary that contains the share records that CloudKit associates with specified managed object IDs.
- [- persistUpdatedShare:inPersistentStore:completion:](./persistupdatedshare_inpersistentstore_completion_.md)
  Saves the share record and schedules it for export to iCloud.
- [- shareManagedObjects:toShare:completion:](./sharemanagedobjects_toshare_completion_.md)
  Associates the specified managed objects with a new or existing share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/fetchparticipantsmatchinglookupinfos:intopersistentstore:completion:)*