# CKSharingParticipantPermissionOption

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum CKSharingParticipantPermissionOption : NSUInteger;
```

## Topics

### Creating an access option
- [init(rawValue: UInt)](./cksharingparticipantpermissionoption/init%28rawvalue%29.md)
  Creates and initializes a participant permission option object.
### Configuring the options
- [static var any: CKSharingParticipantPermissionOption](./cksharingparticipantpermissionoption/any.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [static var readOnly: CKSharingParticipantPermissionOption](./cksharingparticipantpermissionoption/readonly.md)
  The permission option the system uses to control whether a user can grant read-only access.
- [static var readWrite: CKSharingParticipantPermissionOption](./cksharingparticipantpermissionoption/readwrite.md)
  The permission option the system uses to control whether a user can grant write access.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Configuring the options
- [var allowedParticipantAccessOptions: CKSharingParticipantAccessOption](./ckallowedsharingoptions/allowedparticipantaccessoptions.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [var allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption](./ckallowedsharingoptions/allowedparticipantpermissionoptions.md)
  The permission option the system uses to control whether a user can grant read-only or write access.
- [struct CKSharingParticipantAccessOption](./cksharingparticipantaccessoption.md)
  An object that controls participant access options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharingparticipantpermissionoption)*