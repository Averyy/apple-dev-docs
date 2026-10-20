# CKAllowedSharingOptions

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CKAllowedSharingOptions : NSObject
```

#### Overview

Register an instance of this class with an [`NSItemProvider`](../Foundation/nsitemprovider.md) or when preparing a [`CKShareTransferRepresentation.ExportedShare`](./cksharetransferrepresentation/exportedshare.md) before your app invokes the share sheet. The share sheet uses the registered `CKAllowedSharingOptions` object to let the user choose between the allowed options when sharing.

## Topics

### Creating sharing options
- [init(allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption, allowedParticipantAccessOptions: CKSharingParticipantAccessOption)](./ckallowedsharingoptions/init%28allowedparticipantpermissionoptions,allowedparticipantaccessoptions%29.md)
  Creates and initializes an allowed sharing options object.
### Using the standard options
- [class var standard: CKAllowedSharingOptions](./ckallowedsharingoptions/standard.md)
  An object set to the most permissive sharing options.
### Configuring the options
- [var allowedParticipantAccessOptions: CKSharingParticipantAccessOption](./ckallowedsharingoptions/allowedparticipantaccessoptions.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [var allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption](./ckallowedsharingoptions/allowedparticipantpermissionoptions.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [struct CKSharingParticipantAccessOption](./cksharingparticipantaccessoption.md)
  An object that controls participant access options.
- [struct CKSharingParticipantPermissionOption](./cksharingparticipantpermissionoption.md)
  An object that controls participant permission options.
### Initializers
- [init?(coder: NSCoder)](./ckallowedsharingoptions/init%28coder%29.md)
### Instance Properties
- [var allowsAccessRequests: Bool](./ckallowedsharingoptions/allowsaccessrequests.md)
  Default value is NO. If set, the system sharing UI allows the user to configure whether participants can request access to the share.
- [var allowsParticipantsToInviteOthers: Bool](./ckallowedsharingoptions/allowsparticipantstoinviteothers.md)
  Default value is NO. If set, the system sharing UI allows the user to choose whether added participants can invite others to the share. CloudKit returns shares with [`CKShare.ParticipantRole.administrator`](./ckshare/participantrole/administrator.md) participants as read-only to devices running OS versions prior to this role being introduced. CloudKit returns administrator participants on such read-only shares as [`CKShare.ParticipantRole.privateUser`](./ckshare/participantrole/privateuser.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Collaboration
- [Sharing CloudKit Data with Other iCloud Users](./sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](./ckshare.md)
  A specialized record type that manages a collection of shared records.
- [struct CKShareTransferRepresentation](./cksharetransferrepresentation.md)
  A transfer representation the system uses to share an item.
- [class CKSystemSharingUIObserver](./cksystemsharinguiobserver.md)
  An object the system uses to monitor changes in sharing.
- [class UICloudSharingController](../UIKit/uicloudsharingcontroller.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/information-property-list/cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions)*