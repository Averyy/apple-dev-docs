# allowPrivate

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The option that restricts access to people who have been invited.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var allowPrivate: UICloudSharingController.PermissionOptions { get }
```

```c
UICloudSharingPermissionAllowPrivate
```

#### Discussion

To give the user the option to limit access to people who have been invited, include the [`allowPrivate`](./allowprivate.md) option when setting the [`availablePermissions`](../availablepermissions.md) property on the [`UICloudSharingController`](../../uicloudsharingcontroller.md) instance.

> **Note**:  When inviting someone, the user must provide that person’s email address or phone number. This is how the person is identified when accepting the invitation.

## See Also

### Constants
- [static var allowPublic: UICloudSharingController.PermissionOptions](./allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowReadOnly: UICloudSharingController.PermissionOptions](./allowreadonly.md)
  The option that gives participants read-only permission to the shared data.
- [static var allowReadWrite: UICloudSharingController.PermissionOptions](./allowreadwrite.md)
  The option that gives participants read/write permission to the shared data.
- [UICloudSharingPermissionStandard](../../uicloudsharingpermissionoptions/uicloudsharingpermissionstandard.md)
  The option that makes all user options available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowprivate)*