# standard

**Framework**: CloudKit  
**Kind**: property

An object set to the most permissive sharing options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var standard: CKAllowedSharingOptions { get }
```

#### Discussion

The `standardOptions` has [`allowedParticipantPermissionOptions`](ckallowedsharingoptions/allowedparticipantpermissionoptions.md) set to [`any`](cksharingparticipantpermissionoption/any.md) and [`allowedParticipantAccessOptions`](ckallowedsharingoptions/allowedparticipantaccessoptions.md) set to [`any`](cksharingparticipantaccessoption/any.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions/standard)*