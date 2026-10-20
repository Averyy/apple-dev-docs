# CKContainer.Application

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

A collection of types for app permissions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
enum Application
```

## Topics

### Container Application Types
- [CKContainer.Application.Permissions](./application/permissions.md)
  A type that represents the permissions that a user grants.
- [CKContainer.Application.PermissionBlock](./application/permissionblock.md)
  A type that represents a handler that processes the outcome of a permission’s request.
- [CKContainer.Application.PermissionStatus](./application/permissionstatus.md)
  A type that represents the status of a permission.

## See Also

### Requesting and Determining App Permissions
- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./requestapplicationpermission%28_,completionhandler%29.md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./status%28forapplicationpermission,completionhandler%29.md)
  Determines the authorization status of the specified permission.
- [CKContainer.ApplicationPermissions](./applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](./applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](./applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/application)*