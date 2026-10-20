# allowReadOnly

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The option that gives participants read-only permission to the shared data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var allowReadOnly: UICloudSharingController.PermissionOptions { get }
```

```c
UICloudSharingPermissionAllowReadOnly
```

#### Discussion

To give the user the option to prevent other people from editing the shared data, include the [`allowReadOnly`](./allowreadonly.md) option when setting the [`availablePermissions`](../availablepermissions.md) property on the [`UICloudSharingController`](../../uicloudsharingcontroller.md) instance.

## See Also

### Constants
- [static var allowPublic: UICloudSharingController.PermissionOptions](./allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowPrivate: UICloudSharingController.PermissionOptions](./allowprivate.md)
  The option that restricts access to people who have been invited.
- [static var allowReadWrite: UICloudSharingController.PermissionOptions](./allowreadwrite.md)
  The option that gives participants read/write permission to the shared data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowreadonly)*