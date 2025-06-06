# CKSharingParticipantAccessOption

**Framework**: CloudKit  
**Kind**: struct

An object that controls participant access options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct CKSharingParticipantAccessOption
```

## Topics

### Creating an access option
- [init(rawValue: UInt)](cksharingparticipantaccessoption/init(rawvalue:).md)
  Creates and initializes a participant access option object.
### Configuring the options
- [static var any: CKSharingParticipantAccessOption](cksharingparticipantaccessoption/any.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [static var anyoneWithLink: CKSharingParticipantAccessOption](cksharingparticipantaccessoption/anyonewithlink.md)
  The permission option the system uses to control whether a user can share publicly.
- [static var specifiedRecipientsOnly: CKSharingParticipantAccessOption](cksharingparticipantaccessoption/specifiedrecipientsonly.md)
  The permission option the system uses to control whether a user can share privately.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var allowedParticipantAccessOptions: CKSharingParticipantAccessOption](ckallowedsharingoptions/allowedparticipantaccessoptions.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [var allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption](ckallowedsharingoptions/allowedparticipantpermissionoptions.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [struct CKSharingParticipantPermissionOption](cksharingparticipantpermissionoption.md)
  An object that controls participant permission options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharingparticipantaccessoption)*