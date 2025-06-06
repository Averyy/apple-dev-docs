# status(forApplicationPermission:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Determines the authorization status of the specified permission.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func applicationPermissionStatus(for applicationPermission: CKContainer.ApplicationPermissions) async throws -> CKContainer.ApplicationPermissionStatus
```

#### Discussion

Use this method to determine the extra capabilities that the user grants to your app. If your app doesn’t have a specific permission, calling this method yields [`CKContainer.ApplicationPermissionStatus.initialState`](ckcontainer/applicationpermissionstatus/initialstate.md). In response, call the [`requestApplicationPermission(_:completionHandler:)`](ckcontainer/requestapplicationpermission(_:completionhandler:).md) method to prompt the user to provide their permission.

## Parameters

- `applicationPermission`: The permission to check. For a list of possible values, see  .
- `completionHandler`: The handler to execute with the outcome.

## See Also

- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/requestapplicationpermission(_:completionhandler:).md)
  Prompts the user to authorize the specified permission.
- [CKContainer.Application](ckcontainer/application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](ckcontainer/applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](ckcontainer/applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/status(forapplicationpermission:completionhandler:))*