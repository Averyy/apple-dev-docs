# allowPrivate

**Framework**: Uikit  
**Kind**: property

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

#### Discussion

To give the user the option to limit access to people who have been invited, include the [`allowPrivate`](uicloudsharingcontroller/permissionoptions/allowprivate.md) option when setting the [`availablePermissions`](uicloudsharingcontroller/availablepermissions.md) property on the [`UICloudSharingController`](uicloudsharingcontroller.md) instance.

> **Note**:  When inviting someone, the user must provide that person’s email address or phone number. This is how the person is identified when accepting the invitation.

## See Also

- [static var allowPublic: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowReadOnly: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowreadonly.md)
  The option that gives participants read-only permission to the shared data.
- [static var allowReadWrite: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowreadwrite.md)
  The option that gives participants read/write permission to the shared data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowprivate)*