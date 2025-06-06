# allowReadWrite

**Framework**: UIKit  
**Kind**: property

The option that gives participants read/write permission to the shared data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var allowReadWrite: UICloudSharingController.PermissionOptions { get }
```

#### Discussion

To give the user the option to allow other people to edit the shared data, include the [`allowReadWrite`](uicloudsharingcontroller/permissionoptions/allowreadwrite.md) option when setting the [`availablePermissions`](uicloudsharingcontroller/availablepermissions.md) property on the [`UICloudSharingController`](uicloudsharingcontroller.md) instance.

## See Also

- [static var allowPublic: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowPrivate: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowprivate.md)
  The option that restricts access to people who have been invited.
- [static var allowReadOnly: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowreadonly.md)
  The option that gives participants read-only permission to the shared data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowreadwrite)*