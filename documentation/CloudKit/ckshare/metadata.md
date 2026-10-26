# CKShare.Metadata

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes a shared record’s metadata.

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
class Metadata
```

```objc
@interface CKShareMetadata : NSObject
```

#### Overview

A share’s metadata is an intermediary object that provides access to the share, its owner, and, for a shared record hierarchy, its root record. Metadata also includes details about the current user’s participation in the share.

You don’t create metadata. CloudKit provides it to your app when the user taps or clicks a share’s [`url`](./url.md), such as in an email or a message. The method CloudKit calls varies by platform and app configuration, and includes the following:

- For a scene-based iOS app in a running or suspended state, CloudKit calls the [`windowScene(_:userDidAcceptCloudKitShareWith:)`](../../UIKit/uiwindowscenedelegate/windowscene%28_,userdidacceptcloudkitsharewith%29.md) method on your window scene delegate.
- For a scene-based iOS app that’s not running, the system launches your app in response to the tap or click, and calls the [`scene(_:willConnectTo:options:)`](../../UIKit/uiscenedelegate/scene%28_,willconnectto,options%29.md) method on your scene delegate. The `connectionOptions` parameter contains the metadata. Use its [`cloudKitShareMetadata`](../../UIKit/uiscene/connectionoptions/cloudkitsharemetadata.md) property to access it.
- For an iOS app that doesn’t use scenes, CloudKit calls your app delegate’s [`application(_:userDidAcceptCloudKitShareWith:)`](../../UIKit/uiapplicationdelegate/application%28_,userdidacceptcloudkitsharewith%29.md) method.
- For a macOS app, CloudKit calls your app delegate’s [`application(_:userDidAcceptCloudKitShareWith:)`](../../AppKit/nsapplicationdelegate/application%28_,userdidacceptcloudkitsharewith%29.md) method.
- For a watchOS app, CloudKit calls the [`userDidAcceptCloudKitShare(with:)`](../../WatchKit/wkextensiondelegate/userdidacceptcloudkitshare%28with%29.md) method on your watch extension delegate.

Respond by checking the [`participantStatus`](./metadata/participantstatus.md) of the provided metadata. If the status is `pending`, use [`CKAcceptSharesOperation`](../ckacceptsharesoperation.md) to accept participation in the share. You can also fetch metadata independent of this flow using [`CKFetchShareMetadataOperation`](../ckfetchsharemetadataoperation.md).

For a shared record hierarchy, the [`hierarchicalRootRecordID`](./metadata/hierarchicalrootrecordid.md) property contains the ID of the share’s root record. When using [`CKFetchShareMetadataOperation`](../ckfetchsharemetadataoperation.md) to fetch metadata, you can include the entire root record by setting the operation’s [`shouldFetchRootRecord`](../ckfetchsharemetadataoperation/shouldfetchrootrecord.md) property to [`true`](../../Swift/true.md). CloudKit then populates the [`rootRecord`](./metadata/rootrecord.md) property before it returns the metadata. You can further customize this behavior using the operation’s [`rootRecordDesiredKeys`](../ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md) property to specify which fields to return. This functionality isn’t applicable for a shared record zone because, unlike a shared record hierarchy, it doesn’t have a nominated root record.

The participant properties provide the current user’s acceptance status, permissions, and role. Use these values to determine what functionality to provide to the user. For example, only display editing controls for accepted participants with `readWrite` permissions.

## Topics

### Accessing the Share
- [var share: CKShare](./metadata/share.md)
  The share that owns the metadata.
- [var containerIdentifier: String](./metadata/containeridentifier.md)
  The ID of the share’s container.
- [var ownerIdentity: CKUserIdentity](./metadata/owneridentity.md)
  The identity of the share’s owner.
### Accessing the Root Record
- [var hierarchicalRootRecordID: CKRecord.ID?](./metadata/hierarchicalrootrecordid.md)
  The record ID of the shared hierarchy’s root record.
- [var rootRecord: CKRecord?](./metadata/rootrecord.md)
  The share’s root record.
- [var rootRecordID: CKRecord.ID](./metadata/rootrecordid.md)
  The record ID of the share’s root record.
### Accessing the Participant’s Capabilities
- [var participantRole: CKShare.ParticipantRole](./metadata/participantrole.md)
  The share’s participant role for the user who retrieves the metadata.
- [var participantPermission: CKShare.ParticipantPermission](./metadata/participantpermission.md)
  The share’s permissions for the user who retrieves the metadata.
- [var participantStatus: CKShare.ParticipantAcceptanceStatus](./metadata/participantstatus.md)
  The share’s participation status for the user who retrieves the metadata.
- [participantType](../cksharemetadata/participanttype.md)
  The share’s participation type for the user who retrieves the metadata.
### Initializers
- [init?(coder: NSCoder)](./metadata/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Share Requests
- [class CKFetchShareMetadataOperation](../ckfetchsharemetadataoperation.md)
  An operation that fetches metadata for one or more shares.
- [class CKAcceptSharesOperation](../ckacceptsharesoperation.md)
  An operation that confirms a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata)*