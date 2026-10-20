# status(forApplicationPermission:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Determines the authorization status of the specified permission.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.0+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
func status(forApplicationPermission applicationPermission: CKContainer.ApplicationPermissions, completionHandler: @escaping @Sendable (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)
```

```swift
func applicationPermissionStatus(for applicationPermission: CKContainer.ApplicationPermissions) async throws -> CKContainer.ApplicationPermissionStatus
```

```objc
- (void) statusForApplicationPermission:(CKApplicationPermissions) applicationPermission completionHandler:(CKApplicationPermissionBlock) completionHandler;
```

#### Discussion

Use this method to determine the extra capabilities that the user grants to your app. If your app doesn’t have a specific permission, calling this method yields [`CKContainer.ApplicationPermissionStatus.initialState`](./applicationpermissionstatus/initialstate.md). In response, call the [`requestApplicationPermission(_:completionHandler:)`](./requestapplicationpermission%28_,completionhandler%29.md) method to prompt the user to provide their permission.

## Parameters

- `applicationPermission`: The permission to check. For a list of possible values, see [`CKContainer.ApplicationPermissions`](./applicationpermissions.md).
- `completionHandler`: The handler to execute with the outcome.

## See Also

### Requesting and Determining App Permissions
- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](./requestapplicationpermission%28_,completionhandler%29.md)
  Prompts the user to authorize the specified permission.
- [CKContainer.Application](./application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](./applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](./applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.
- [CKContainer.ApplicationPermissionStatus](./applicationpermissionstatus.md)
  Constants that represent the status of a permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/status(forapplicationpermission:completionhandler:))*