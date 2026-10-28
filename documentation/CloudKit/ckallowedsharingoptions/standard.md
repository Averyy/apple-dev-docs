# standard

**Framework**: CloudKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, strong, readonly) CKAllowedSharingOptions * standardOptions;
```

## Discussion

The `standardOptions` has [`allowedParticipantPermissionOptions`](./allowedparticipantpermissionoptions.md) set to [`any`](../cksharingparticipantpermissionoption/any.md) and [`allowedParticipantAccessOptions`](./allowedparticipantaccessoptions.md) set to [`any`](../cksharingparticipantaccessoption/any.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions/standard)*