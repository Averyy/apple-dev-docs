# CKAllowedSharingOptions

**Framework**: CloudKit  
**Kind**: class

An object that controls participant access and permission options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class CKAllowedSharingOptions
```

#### Overview

Register an instance of this class with an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) or when preparing a [`CKShareTransferRepresentation.ExportedShare`](cksharetransferrepresentation/exportedshare.md) before your app invokes the share sheet. The share sheet uses the registered `CKAllowedSharingOptions` object to let the user choose between the allowed options when sharing.

## Topics

### Creating sharing options
- [init(allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption, allowedParticipantAccessOptions: CKSharingParticipantAccessOption)](ckallowedsharingoptions/init(allowedparticipantpermissionoptions:allowedparticipantaccessoptions:).md)
  Creates and initializes an allowed sharing options object.
### Using the standard options
- [class var standard: CKAllowedSharingOptions](ckallowedsharingoptions/standard.md)
  An object set to the most permissive sharing options.
### Configuring the options
- [var allowedParticipantAccessOptions: CKSharingParticipantAccessOption](ckallowedsharingoptions/allowedparticipantaccessoptions.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [var allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption](ckallowedsharingoptions/allowedparticipantpermissionoptions.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [struct CKSharingParticipantAccessOption](cksharingparticipantaccessoption.md)
  An object that controls participant access options.
- [struct CKSharingParticipantPermissionOption](cksharingparticipantpermissionoption.md)
  An object that controls participant permission options.
### Instance Properties
- [var allowsAccessRequests: Bool](ckallowedsharingoptions/allowsaccessrequests.md)
  Default value is `NO`. If set, the system sharing UI will allow the user to configure whether access requests are enabled on the share.
- [var allowsParticipantsToInviteOthers: Bool](ckallowedsharingoptions/allowsparticipantstoinviteothers.md)
  Default value is `NO`. If set, the system sharing UI will allow the user to choose whether added participants can invite others to the share. Shares with [`CKShare.ParticipantRole.administrator`](ckshare/participantrole/administrator.md) participants will be returned as read-only to devices running OS versions prior to this role being introduced. Administrator participants on these read-only shares will be returned as [`CKShare.ParticipantRole.privateUser`](ckshare/participantrole/privateuser.md).

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

- [Sharing CloudKit Data with Other iCloud Users](sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](ckshare.md)
  A specialized record type that manages a collection of shared records.
- [struct CKShareTransferRepresentation](cksharetransferrepresentation.md)
  A transfer representation the system uses to share an item.
- [class CKSystemSharingUIObserver](cksystemsharinguiobserver.md)
  An object the system uses to monitor changes in sharing.
- [class UICloudSharingController](../UIKit/UICloudSharingController.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/Information-Property-List/CKSharingSupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions)*