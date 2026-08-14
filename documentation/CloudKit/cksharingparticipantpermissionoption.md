# CKSharingParticipantPermissionOption

**Framework**: CloudKit  
**Kind**: struct

An object that controls participant permission options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct CKSharingParticipantPermissionOption
```

## Topics

### Creating an access option
- [init(rawValue: UInt)](cksharingparticipantpermissionoption/init(rawvalue:).md)
  Creates and initializes a participant permission option object.
### Configuring the options
- [static var any: CKSharingParticipantPermissionOption](cksharingparticipantpermissionoption/any.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [static var readOnly: CKSharingParticipantPermissionOption](cksharingparticipantpermissionoption/readonly.md)
  The permission option the system uses to control whether a user can grant read-only access.
- [static var readWrite: CKSharingParticipantPermissionOption](cksharingparticipantpermissionoption/readwrite.md)
  The permission option the system uses to control whether a user can grant write access.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var allowedParticipantAccessOptions: CKSharingParticipantAccessOption](ckallowedsharingoptions/allowedparticipantaccessoptions.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [var allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption](ckallowedsharingoptions/allowedparticipantpermissionoptions.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [struct CKSharingParticipantAccessOption](cksharingparticipantaccessoption.md)
  An object that controls participant access options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharingparticipantpermissionoption)*