# CKContainer.Application

**Framework**: CloudKit  
**Kind**: enum

A collection of types for app permissions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
enum Application
```

## Topics

### Container Application Types
- [CKContainer.Application.Permissions](ckcontainer/application/permissions.md)
  A type that represents the permissions that a user grants.
- [CKContainer.Application.PermissionBlock](ckcontainer/application/permissionblock.md)
  A type that represents a handler that processes the outcome of a permission’s request.
- [CKContainer.Application.PermissionStatus](ckcontainer/application/permissionstatus.md)
  A type that represents the status of a permission.

## See Also

- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/requestapplicationpermission(_:completionhandler:).md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/status(forapplicationpermission:completionhandler:).md)
  Determines the authorization status of the specified permission.
- [CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](ckcontainer/applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](ckcontainer/applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/application)*