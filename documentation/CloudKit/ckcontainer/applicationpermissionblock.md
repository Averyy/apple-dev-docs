# CKContainer.ApplicationPermissionBlock

**Framework**: CloudKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that processes the outcome of a permissions request.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.10+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
typealias ApplicationPermissionBlock = (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void
```

```c
typedef void (^)(enum CKApplicationPermissionStatus, NSError *) CKApplicationPermissionBlock;
```

#### Discussion

When you request or determine the status of a permission, use this closure to process the result. The closure has no return value and takes the following parameters:

- The permission’s status. For a list of possible values, see [`CKContainer.ApplicationPermissionStatus`](./applicationpermissionstatus.md).
- An error if the system can’t fulfill the request, or `nil` if it successfully determines the status.

## See Also

### Requesting and Determining App Permissions
- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./requestapplicationpermission%28_,completionhandler%29.md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./status%28forapplicationpermission,completionhandler%29.md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](./application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](./applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionStatus](./applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissionblock)*