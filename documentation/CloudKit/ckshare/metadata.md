# CKShare.Metadata

**Framework**: CloudKit  
**Kind**: class

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

#### Overview

A share’s metadata is an intermediary object that provides access to the share, its owner, and, for a shared record hierarchy, its root record. Metadata also includes details about the current user’s participation in the share.

You don’t create metadata. CloudKit provides it to your app when the user taps or clicks a share’s [`url`](ckshare/url.md), such as in an email or a message. The method CloudKit calls varies by platform and app configuration, and includes the following:

- For a scene-based iOS app in a running or suspended state, CloudKit calls the [`windowScene(_:userDidAcceptCloudKitShareWith:)`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate/windowScene(_:userDidAcceptCloudKitShareWith:)) method on your window scene delegate.
- For a scene-based iOS app that’s not running, the system launches your app in response to the tap or click, and calls the [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) method on your scene delegate. The `connectionOptions` parameter contains the metadata. Use its [`cloudKitShareMetadata`](https://developer.apple.com/documentation/UIKit/UIScene/ConnectionOptions/cloudKitShareMetadata) property to access it.
- For an iOS app that doesn’t use scenes, CloudKit calls your app delegate’s [`application(_:userDidAcceptCloudKitShareWith:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:userDidAcceptCloudKitShareWith:)) method.
- For a macOS app, CloudKit calls your app delegate’s [`application(_:userDidAcceptCloudKitShareWith:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/application(_:userDidAcceptCloudKitShareWith:)) method.
- For a watchOS app, CloudKit calls the [`userDidAcceptCloudKitShare(with:)`](https://developer.apple.com/documentation/WatchKit/WKExtensionDelegate/userDidAcceptCloudKitShare(with:)) method on your watch extension delegate.

Respond by checking the [`participantStatus`](ckshare/metadata/participantstatus.md) of the provided metadata. If the status is `pending`, use [`CKAcceptSharesOperation`](ckacceptsharesoperation.md) to accept participation in the share. You can also fetch metadata independent of this flow using [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md).

For a shared record hierarchy, the [`hierarchicalRootRecordID`](ckshare/metadata/hierarchicalrootrecordid.md) property contains the ID of the share’s root record. When using [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md) to fetch metadata, you can include the entire root record by setting the operation’s [`shouldFetchRootRecord`](ckfetchsharemetadataoperation/shouldfetchrootrecord.md) property to [`true`](https://developer.apple.com/documentation/Swift/true). CloudKit then populates the [`rootRecord`](ckshare/metadata/rootrecord.md) property before it returns the metadata. You can further customize this behavior using the operation’s [`rootRecordDesiredKeys`](ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md) property to specify which fields to return. This functionality isn’t applicable for a shared record zone because, unlike a shared record hierarchy, it doesn’t have a nominated root record.

The participant properties provide the current user’s acceptance status, permissions, and role. Use these values to determine what functionality to provide to the user. For example, only display editing controls for accepted participants with `readWrite` permissions.

## Topics

### Accessing the Share
- [var share: CKShare](ckshare/metadata/share.md)
  The share that owns the metadata.
- [var containerIdentifier: String](ckshare/metadata/containeridentifier.md)
  The ID of the share’s container.
- [var ownerIdentity: CKUserIdentity](ckshare/metadata/owneridentity.md)
  The identity of the share’s owner.
### Accessing the Root Record
- [var hierarchicalRootRecordID: CKRecord.ID?](ckshare/metadata/hierarchicalrootrecordid.md)
  The record ID of the shared hierarchy’s root record.
- [var rootRecord: CKRecord?](ckshare/metadata/rootrecord.md)
  The share’s root record.
- [var rootRecordID: CKRecord.ID](ckshare/metadata/rootrecordid.md)
  The record ID of the share’s root record.
### Accessing the Participant’s Capabilities
- [var participantRole: CKShare.ParticipantRole](ckshare/metadata/participantrole.md)
  The share’s participant role for the user who retrieves the metadata.
- [var participantPermission: CKShare.ParticipantPermission](ckshare/metadata/participantpermission.md)
  The share’s permissions for the user who retrieves the metadata.
- [var participantStatus: CKShare.ParticipantAcceptanceStatus](ckshare/metadata/participantstatus.md)
  The share’s participation status for the user who retrieves the metadata.
- [var participantType: CKShare.ParticipantType](ckshare/metadata/participanttype.md)
  The share’s participation type for the user who retrieves the metadata.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
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

## See Also

- [class CKFetchShareMetadataOperation](ckfetchsharemetadataoperation.md)
  An operation that fetches metadata for one or more shares.
- [class CKAcceptSharesOperation](ckacceptsharesoperation.md)
  An operation that confirms a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata)*