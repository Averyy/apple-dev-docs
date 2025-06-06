# CKContainer.ApplicationPermissions

**Framework**: CloudKit  
**Kind**: struct

Constants that represent the permissions that a user grants.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct ApplicationPermissions
```

## Topics

### Creating Permissions
- [init(rawValue: UInt)](ckcontainer/applicationpermissions/init(rawvalue:).md)
  Creates a premission with the specified raw value.
### Accessing Permissions
- [static var userDiscoverability: CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions/userdiscoverability.md)
  The user is discoverable using their email address.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/requestapplicationpermission(_:completionhandler:).md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/status(forapplicationpermission:completionhandler:).md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](ckcontainer/application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissionBlock](ckcontainer/applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](ckcontainer/applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissions)*