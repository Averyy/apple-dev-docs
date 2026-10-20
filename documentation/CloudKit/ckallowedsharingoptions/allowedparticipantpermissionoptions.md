# allowedParticipantPermissionOptions

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The permission option the system uses to control whether a user can grant read-only or write access.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var allowedParticipantPermissionOptions: CKSharingParticipantPermissionOption { get set }
```

```objc
@property (assign) CKSharingParticipantPermissionOption allowedParticipantPermissionOptions;
```

## See Also

### Configuring the options
- [var allowedParticipantAccessOptions: CKSharingParticipantAccessOption](./allowedparticipantaccessoptions.md)
  The permission option the system uses to control whether a user can share publicly or privately.
- [struct CKSharingParticipantAccessOption](../cksharingparticipantaccessoption.md)
  An object that controls participant access options.
- [struct CKSharingParticipantPermissionOption](../cksharingparticipantpermissionoption.md)
  An object that controls participant permission options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions/allowedparticipantpermissionoptions)*