# requestApplicationPermission(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Prompts the user to authorize the specified permission.

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
func requestApplicationPermission(_ applicationPermission: CKContainer.ApplicationPermissions) async throws -> CKContainer.ApplicationPermissionStatus
```

#### Discussion

To implement social features in your app, it’s possible to correlate a user record with the user’s actual name, but your app must get permission from the user to do so. Making a user record discoverable to the contacts of that user involves calling the [`requestApplicationPermission(_:completionHandler:)`](ckcontainer/requestapplicationpermission(_:completionhandler:).md) method and asking for the [`userDiscoverability`](ckcontainer/applicationpermissions/userdiscoverability.md) permission. When you call that method, CloudKit asks the user whether the user record can become discoverable. If the user grants the request, that user’s contacts can discover that user’s true identity when running the app. To discover the contacts of the current user, you use the `discoverAllContactUserInfos(completionHandler:)` method or one of several other methods to get the related user information.

The first time you request a permission on any of the user’s devices, the user receives a prompt to grant or deny the request. After the user grants or denies a permission, subsequent requests for the same permission (on the same or separate devices), don’t prompt the user again.

This method runs asynchronously, and the system calls your completion handler on an arbitary queue and provides the outcome.

## Parameters

- `applicationPermission`: The permission to request. This permission applies only to the current container. For a list of possible values, see  .
- `completionHandler`: The handler to execute with the outcome.

## See Also

- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/status(forapplicationpermission:completionhandler:).md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](ckcontainer/application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](ckcontainer/applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](ckcontainer/applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/requestapplicationpermission(_:completionhandler:))*