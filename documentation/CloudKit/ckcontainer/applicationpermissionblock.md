# CKContainer.ApplicationPermissionBlock

**Framework**: CloudKit  
**Kind**: typealias

A closure that processes the outcome of a permissions request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
typealias ApplicationPermissionBlock = (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void
```

#### Discussion

When you request or determine the status of a permission, use this closure to process the result. The closure has no return value and takes the following parameters:

- The permission’s status. For a list of possible values, see [`CKContainer.ApplicationPermissionStatus`](ckcontainer/applicationpermissionstatus.md).
- An error if the system can’t fulfill the request, or `nil` if it successfully determines the status.

## See Also

- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/requestapplicationpermission(_:completionhandler:).md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/status(forapplicationpermission:completionhandler:).md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](ckcontainer/application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionStatus](ckcontainer/applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissionblock)*