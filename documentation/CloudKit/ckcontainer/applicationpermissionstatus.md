# CKContainer.ApplicationPermissionStatus

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the status of a permission.

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
enum ApplicationPermissionStatus
```

```c
enum CKApplicationPermissionStatus : NSInteger;
```

## Topics

### Permission Statuses
- [CKContainer.ApplicationPermissionStatus.initialState](./applicationpermissionstatus/initialstate.md)
  The app is yet to request the permission.
- [CKContainer.ApplicationPermissionStatus.couldNotComplete](./applicationpermissionstatus/couldnotcomplete.md)
  An error that occurs while processing the permission request.
- [CKContainer.ApplicationPermissionStatus.denied](./applicationpermissionstatus/denied.md)
  The user denies the permission.
- [CKContainer.ApplicationPermissionStatus.granted](./applicationpermissionstatus/granted.md)
  The user grants the permission.
### Initializers
- [init?(rawValue: Int)](./applicationpermissionstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [CKContainer.ApplicationPermissionBlock](./applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissionstatus)*