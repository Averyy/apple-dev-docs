# CKContainer.ApplicationPermissions

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

Constants that represent the permissions that a user grants.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct ApplicationPermissions
```

```c
enum CKApplicationPermissions : NSUInteger;
```

## Topics

### Creating Permissions
- [init(rawValue: UInt)](./applicationpermissions/init%28rawvalue%29.md)
  Creates a premission with the specified raw value.
### Accessing Permissions
- [static var userDiscoverability: CKContainer.ApplicationPermissions](./applicationpermissions/userdiscoverability.md)
  The user is discoverable using their email address.

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

### Requesting and Determining App Permissions
- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./requestapplicationpermission%28_,completionhandler%29.md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./status%28forapplicationpermission,completionhandler%29.md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](./application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissionBlock](./applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](./applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissions)*