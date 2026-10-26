# UICloudSharingController.PermissionOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UICloudSharingPermissionOptions : NSUInteger;
```

#### Overview

These options are used when setting the [`availablePermissions`](./availablepermissions.md) property on the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance. This property determines which permission options are presented to the user in the controller’s user interface.

## Topics

### Constants
- [static var allowPublic: UICloudSharingController.PermissionOptions](./permissionoptions/allowpublic.md)
  The option that grants access to anyone who has the share link.
- [static var allowPrivate: UICloudSharingController.PermissionOptions](./permissionoptions/allowprivate.md)
  The option that restricts access to people who have been invited.
- [static var allowReadOnly: UICloudSharingController.PermissionOptions](./permissionoptions/allowreadonly.md)
  The option that gives participants read-only permission to the shared data.
- [static var allowReadWrite: UICloudSharingController.PermissionOptions](./permissionoptions/allowreadwrite.md)
  The option that gives participants read/write permission to the shared data.
- [UICloudSharingPermissionStandard](../uicloudsharingpermissionoptions/uicloudsharingpermissionstandard.md)
  The option that makes all user options available.
### Initializers
- [init(rawValue: UInt)](./permissionoptions/init%28rawvalue%29.md)
  Creates a new permission option set with the given raw integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring the permissions
- [var availablePermissions: UICloudSharingController.PermissionOptions](./availablepermissions.md)
  A combination of permission and access options made available to the user when viewing screens presented by the CloudKit sharing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions)*