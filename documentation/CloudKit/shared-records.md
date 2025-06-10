# Shared Records

**Framework**: CloudKit

Share one or more records with other iCloud users.

#### Overview

CloudKit users can share records in their private databases with other iCloud users, which enables collaboration between the people using your app. The user that initiates sharing, the owner, handles all aspects of the collaboration, from inviting people to participate to restricting what actions the participants can perform.

![A diagram that shows the owner of a private database using iCloud to share records with two participants. The owner’s private database stores the records, which CloudKit makes available to each participant in their shared database.](https://docs-assets.developer.apple.com/published/c20e124d54f7123e04eb675844c16793/media-3761001%402x.png)

CloudKit allows you to share both record zones and record hierarchies. If you want to share an unbounded collection of records that don’t have natural parent-child relationships, share their containing record zone. However, if you want to share only a specific set of related records, define an explicit record hierarchy and share that instead.

For more information, see [`Sharing CloudKit Data with Other iCloud Users`](sharing-cloudkit-data-with-other-icloud-users.md).

##### Share a Record Zone or Hierarchy

You store shareable records in a custom record zone in the user’s private database. As you create records in that zone, they become eligible for record zone sharing. If you then choose to share that record zone, CloudKit allows participants to access all the records it contains.

Alternatively, you can build a hierarchy by defining relationships between records as you create them. Set a record’s [`parent`](ckrecord/parent.md) property to designate it as a child of the referenced record. If your data model is hierarchical, this is good practice even if you don’t plan to share the records. Whereas sharing a record zone is catch-all, sharing a record hierarchy allows you to specify exactly which records to include.

To begin sharing, create an instance of [`CKShare`](ckshare.md) with either the ID of the record zone to share, or the root record, which defines the point in the record hierarchy where you want to start sharing. CloudKit shares all the records in the record zone, or every record in the hierarchy below the root. A record can take part in only a single share. This applies to every record in the shared record zone or hierarchy.

After you create the share, save it using [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md). The shared records must already exist in iCloud or be part of the same save operation.

##### Invite Participants

After saving the share, CloudKit assigns it a stable share URL. Use this URL to invite other users to participate. In iOS, [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) provides a consistent and familiar experience for managing a share’s participants and their permissions, and for distributing the share URL. Use [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) and [`NSSharingService`](https://developer.apple.com/documentation/AppKit/NSSharingService) in macOS (with the [`cloudSharing`](https://developer.apple.com/documentation/AppKit/NSSharingService/Name/cloudSharing) service name) to achieve similar functionality. Only invited participants can join a private share. Anyone with the share URL can join a public share. For more information, see [`publicPermission`](ckshare/publicpermission.md).

When an invited user taps or clicks the share URL, CloudKit verifies they have an active iCloud account, which must match their participant details. After successful verification, the system launches your app. CloudKit provides share metadata to your app’s scene delegate or app delegate. The method the system calls varies by platform and app configuration. For more information, see [`CKShare.Metadata`](ckshare/metadata.md).

> ❗ **Important**:  To enable the system to launch your app when the user taps or clicks the share URL, add the `CKSharingSupported` key to the app’s `Info.plist` file. For more information, see [`CKSharingSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CKSharingSupported).

##### Manage Share Participation

After receiving the share metadata from CloudKit, use [`CKAcceptSharesOperation`](ckacceptsharesoperation.md) to confirm the user’s participation. CloudKit then creates a record zone in the participant’s shared database that provides a view into the owner’s private database. The record zone contains only the records in the share; no other data is accessible. A participant with write permissions can change or delete records in this new record zone. Any changes they make are visible to all participants.

Create a database subscription in the user’s shared database the first time they launch your app. Then, when they confirm participation in a share, iCloud notifies your app, on all of the user’s devices, of any changes to the shared records. For more information, see [`CKDatabaseSubscription`](ckdatabasesubscription.md).

To stop sharing, the share’s owner must delete the share or, for shared hierarchies, the root record. If a participant wants to leave the share, delete the share record from their shared database. Use [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) or [`NSSharingService`](https://developer.apple.com/documentation/AppKit/NSSharingService) to allow a participant to stop participating. Or remove them from the share using the [`removeParticipant(_:)`](ckshare/removeparticipant(_:).md) method, and then save the updated share to iCloud.

##### Customize the Sharing Experience

You can use the framework’s share-related operations to implement behavior similar to that of [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) and [`NSSharingService`](https://developer.apple.com/documentation/AppKit/NSSharingService) to build a custom sharing experience by following these steps:

1. Use [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) to generate participants and add them to the share using [`addParticipant(_:)`](ckshare/addparticipant(_:).md). Your app presents a list of potential participants to the user. You can also allow the owner to add participants by entering a participant’s email address or phone number.
2. Save the share to iCloud.
3. Provide the share URL to the participants. You can send the URL in an email or a message, or your app might have secure, in-app chat between users to facilitate distribution of the URL.
4. For each participant, fetch the share’s metadata using [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md) and the share URL.
5. Use [`CKAcceptSharesOperation`](ckacceptsharesoperation.md) to confirm participation.
6. After you share records, use the properties and methods on [`CKShare`](ckshare.md) to manage the share’s participants.

For public shares, you can skip the first step. Accepting a public share’s metadata automatically adds the user as a participant.

## Topics

### Collaboration
- [Sharing CloudKit Data with Other iCloud Users](sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](ckshare.md)
  A specialized record type that manages a collection of shared records.
- [struct CKShareTransferRepresentation](cksharetransferrepresentation.md)
  A transfer representation the system uses to share an item.
- [class CKAllowedSharingOptions](ckallowedsharingoptions.md)
  An object that controls participant access and permission options.
- [class CKSystemSharingUIObserver](cksystemsharinguiobserver.md)
  An object the system uses to monitor changes in sharing.
- [@MainActor class UICloudSharingController](../UIKit/UICloudSharingController.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/Information-Property-List/CKSharingSupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.
### Share Requests
- [class CKFetchShareMetadataOperation](ckfetchsharemetadataoperation.md)
  An operation that fetches metadata for one or more shares.
- [CKShare.Metadata](ckshare/metadata.md)
  An object that describes a shared record’s metadata.
- [class CKAcceptSharesOperation](ckacceptsharesoperation.md)
  An operation that confirms a user’s participation in a share.
### Participants
- [class CKFetchShareParticipantsOperation](ckfetchshareparticipantsoperation.md)
  An operation that converts user identities into share participants.
- [CKShare.Participant](ckshare/participant.md)
  An object that describes a user’s participation in a share.
### Base Objects
- [class CKOperation](ckoperation.md)
  The abstract base class for all operations that execute in a database.

## See Also

- [Local Records](local-records.md)
  Manipulate records on-device and save changes to the server.
- [Remote Records](remote-records.md)
  Use subscriptions and change tokens to efficiently manage modifications to remote records.
- [class CKSyncEngine](cksyncengine-5sie5.md)
  An object that manages the synchronization of local and remote record data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/shared-records)*