# CKShare

**Framework**: CloudKit  
**Kind**: class

A specialized record type that manages a collection of shared records.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKShare
```

#### Overview

A share is a specialized record type that facilitates the sharing of one or more records with many participants. You store shareable records in a custom record zone in the user’s private database. As you create records in that zone, they become eligible for record zone sharing. If you want to share a specific hierarchy of related records, rather than the entire record zone, set each record’s [`parent`](ckrecord/parent.md) property to define the relationship with its parent. CloudKit infers the shared hierarchy using only the [`parent`](ckrecord/parent.md) property, and ignores any custom reference fields.

You create a share with either the ID of the record zone to share, or the root record, which defines the point in a record hierarchy where you want to start sharing. CloudKit shares all the records in the record zone, or every record in the hierarchy below the root. If you set the root record’s [`parent`](ckrecord/parent.md) property, CloudKit ignores it. A record can take part in only a single share. This applies to every record in the shared record zone or hierarchy. If a record is participating in another share, any attempt to save the share fails, and CloudKit returns an [`alreadyShared`](ckerror/alreadyshared.md) error.

Use [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md) to save the share to the server. The initial set of records the share includes must exist on the server or be part of the same save operation to succeed. CloudKit then updates the share’s [`url`](ckshare/url.md) property. Use [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) to present options to the user for sharing the URL. Otherwise, distribute the URL to any participants you add to the share. You can allow anyone with the URL to take part in the share by setting [`publicPermission`](ckshare/publicpermission.md) to a value more permissive than [`CKShare.ParticipantPermission.none`](ckshare/participantpermission/none.md).

> ❗ **Important**:  You must add the [`CKSharingSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CKSharingSupported) key to your app’s `Info.plist` file with a value of `true`. This allows the system to launch your app when a user taps or clicks the URL.

After CloudKit saves the share, a participant can fetch its corresponding metadata, which includes a reference to the share, information about the user’s participation, and, for shared hierarchies, the root record’s record ID. Create an instance of [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md) using the share’s URL and add it to the container’s queue to execute it. The operation returns an instance of [`CKShare.Metadata`](ckshare/metadata.md) for each URL you provide. This is only applicable if you manually process share acceptance. If a user receives the share URL and taps or clicks it, CloudKit automatically processes their participation.

To determine the configuration of a fetched share, inspect the [`recordName`](ckrecord/id/recordname.md) property of its [`recordID`](ckrecord/recordid.md). If the value is [`CKRecordNameZoneWideShare`](ckrecordnamezonewideshare.md), the share is managing a shared record zone; otherwise, it’s managing a shared record hierarchy.

```swift
let isZoneWide = (metadata.share.recordID.recordName == CKRecordNameZoneWideShare)
```

CloudKit limits the number of participants in a share to 100, and each participant must have an active iCloud account. You don’t create participants. Instead, use [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) to manage a share’s participants and their permissions. Alternatively, create an instance of [`CKUserIdentity.LookupInfo`](ckuseridentity/lookupinfo-swift.class.md) for each user. Provide the user’s email address or phone number, and use [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) to fetch the corresponding participants. CloudKit queries iCloud for corresponding accounts as part of the operation. If it doesn’t find an account, the server updates the participant’s [`userIdentity`](ckshare/participant/useridentity.md) to reflect that by setting the [`hasiCloudAccount`](ckuseridentity/hasicloudaccount.md) property to [`false`](https://developer.apple.com/documentation/Swift/false). CloudKit associates the participant with their iCloud account when they accept the share if they launch the process by tapping or clicking the share URL.

Participants with write permissions can modify or delete any record that you include in the share. However, only the owner can delete a shared hierarchy’s root record. If a participant attempts to delete the share, CloudKit removes the participant. The share remains active for all other participants. If the owner deletes a share that manages a record hierarchy, CloudKit sets the root record’s [`share`](ckrecord/share.md) property to `nil`. CloudKit deletes the share if the owner of the shared heirarchy deletes its root record.

You can customize the title and image the system displays when initiating a share or accepting an invitation to participate. You can also provide a custom UTI to indicate the content of the shared records. Use the keys that [`CKShare.SystemFieldKey`](ckshare/systemfieldkey.md) defines, as the following example shows:

```swift
let share = CKShare(rootRecord: album)

// Configure the share so the system displays the album's 
// name and cover when the user initiates sharing or accepts 
// an invitation to participate.
share[CKShare.SystemFieldKey.title] = album["name"]
if let cover = album["cover"] as? UIImage, let data = cover.pngData() {
    share[CKShare.SystemFieldKey.thumbnailImageData] = data
}
// Include a custom UTI that describes the share's content.
share[CKShare.SystemFieldKey.shareType] = "com.example.app.album"
```

## Topics

### Creating a Share
- [init(coder: NSCoder)](ckshare/init(coder:).md)
  Creates a share from a serialized instance.
- [convenience init(rootRecord: CKRecord)](ckshare/init(rootrecord:).md)
  Creates a new share for the specified record.
- [init(rootRecord: CKRecord, shareID: CKRecord.ID)](ckshare/init(rootrecord:shareid:).md)
  Creates a new share for the specified record and record ID.
- [init(recordZoneID: CKRecordZone.ID)](ckshare/init(recordzoneid:).md)
  Creates a new share for the specified record zone.
### Accessing the Share’s Attributes
- [var owner: CKShare.Participant](ckshare/owner.md)
  The participant that represents the share’s owner.
- [var currentUserParticipant: CKShare.Participant?](ckshare/currentuserparticipant.md)
  The participant that represents the current user.
- [var participants: [CKShare.Participant]](ckshare/participants.md)
  An array that contains the share’s participants.
- [var url: URL?](ckshare/url.md)
  The URL for inviting participants to the share.
### Configuring the Share
- [var publicPermission: CKShare.ParticipantPermission](ckshare/publicpermission.md)
  The permission for anyone with access to the share’s URL.
- [func addParticipant(CKShare.Participant)](ckshare/addparticipant(_:).md)
  Adds a participant to the share.
- [func removeParticipant(CKShare.Participant)](ckshare/removeparticipant(_:).md)
  Removes a participant from the share.
- [CKShare.Participant](ckshare/participant.md)
  An object that describes a user’s participation in a share.
### Accessing Metadata
- [CKShare.Metadata](ckshare/metadata.md)
  An object that describes a shared record’s metadata.
### Subscripting
- [CKShare.SystemFieldKey](ckshare/systemfieldkey.md)
  Constants that represent the system fields of a share.
### Classes
- [CKShare.AccessRequester](ckshare/accessrequester.md)
- [CKShare.BlockedIdentity](ckshare/blockedidentity.md)
### Instance Properties
- [var allowsAccessRequests: Bool](ckshare/allowsaccessrequests.md)
  Indicates whether uninvited users can request access to this share.
- [var blockedIdentities: [CKShare.BlockedIdentity]](ckshare/blockedidentities.md)
  A list of users blocked from requesting access to this share.
- [var requesters: [CKShare.AccessRequester]](ckshare/requesters.md)
  A list of all uninvited users who have requested access to this share.
### Instance Methods
- [func blockRequesters([CKShare.AccessRequester])](ckshare/blockrequesters(_:).md)
  Blocks specified users from requesting access to this share.
- [func denyRequesters([CKShare.AccessRequester])](ckshare/denyrequesters(_:).md)
  Denies access requests from specified users.
- [func oneTimeURL(for: CKShare.Participant.ID) -> URL?](ckshare/onetimeurl(for:).md)
- [func unblockIdentities([CKShare.BlockedIdentity])](ckshare/unblockidentities(_:).md)
  Unblocks previously blocked users, allowing them to request access again.

## Relationships

### Inherits From
- [CKRecord](ckrecord.md)
### Conforms To
- [CKRecordKeyValueSetting](ckrecordkeyvaluesetting.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [Sharing CloudKit Data with Other iCloud Users](sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [struct CKShareTransferRepresentation](cksharetransferrepresentation.md)
  A transfer representation the system uses to share an item.
- [class CKAllowedSharingOptions](ckallowedsharingoptions.md)
  An object that controls participant access and permission options.
- [class CKSystemSharingUIObserver](cksystemsharinguiobserver.md)
  An object the system uses to monitor changes in sharing.
- [class UICloudSharingController](../UIKit/UICloudSharingController.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/Information-Property-List/CKSharingSupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare)*