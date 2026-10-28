# UICloudSharingPermissionStandard

**Framework**: UIKit  
**Kind**: case  
**Role**: Enumeration Case

The option that makes all user options available.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```c
UICloudSharingPermissionStandard
```

## Discussion

To tell the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance to display all user options, set its [`availablePermissions`](../uicloudsharingcontroller/availablepermissions.md) property to [`UICloudSharingPermissionStandard`](./uicloudsharingpermissionstandard.md).

The other [`UICloudSharingController.PermissionOptions`](../uicloudsharingcontroller/permissionoptions.md) options override this option, so there’s no need to combine the other options with [`UICloudSharingPermissionStandard`](./uicloudsharingpermissionstandard.md).

## See Also

### Constants
- [static var allowPublic: UICloudSharingController.PermissionOptions](../uicloudsharingcontroller/permissionoptions/allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowPrivate: UICloudSharingController.PermissionOptions](../uicloudsharingcontroller/permissionoptions/allowprivate.md)
  The option that restricts access to people who have been invited.
- [static var allowReadOnly: UICloudSharingController.PermissionOptions](../uicloudsharingcontroller/permissionoptions/allowreadonly.md)
  The option that gives participants read-only permission to the shared data.
- [static var allowReadWrite: UICloudSharingController.PermissionOptions](../uicloudsharingcontroller/permissionoptions/allowreadwrite.md)
  The option that gives participants read/write permission to the shared data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionstandard)*