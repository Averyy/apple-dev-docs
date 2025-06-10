# UICloudSharingController.PermissionOptions

**Framework**: UIKit  
**Kind**: struct

A set of options that determine the permission options available to the user when viewing the Cloud sharing controller screens.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct PermissionOptions
```

#### Overview

These options are used when setting the [`availablePermissions`](uicloudsharingcontroller/availablepermissions.md) property on the [`UICloudSharingController`](uicloudsharingcontroller.md) instance. This property determines which permission options are presented to the user in the controller’s user interface.

## Topics

### Constants
- [static var allowPublic: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowPrivate: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowprivate.md)
  The option that restricts access to people who have been invited.
- [static var allowReadOnly: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowreadonly.md)
  The option that gives participants read-only permission to the shared data.
- [static var allowReadWrite: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions/allowreadwrite.md)
  The option that gives participants read/write permission to the shared data.
### Initializers
- [init(rawValue: UInt)](uicloudsharingcontroller/permissionoptions/init(rawvalue:).md)
  Creates a new permission option set with the given raw integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var availablePermissions: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/availablepermissions.md)
  A combination of permission and access options made available to the user when viewing screens presented by the CloudKit sharing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions)*