# CKContainer.ApplicationPermissionStatus

**Framework**: CloudKit  
**Kind**: enum

Constants that represent the status of a permission.

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
enum ApplicationPermissionStatus
```

## Topics

### Permission Statuses
- [CKContainer.ApplicationPermissionStatus.initialState](ckcontainer/applicationpermissionstatus/initialstate.md)
  The app is yet to request the permission.
- [CKContainer.ApplicationPermissionStatus.couldNotComplete](ckcontainer/applicationpermissionstatus/couldnotcomplete.md)
  An error that occurs while processing the permission request.
- [CKContainer.ApplicationPermissionStatus.denied](ckcontainer/applicationpermissionstatus/denied.md)
  The user denies the permission.
- [CKContainer.ApplicationPermissionStatus.granted](ckcontainer/applicationpermissionstatus/granted.md)
  The user grants the permission.
### Initializers
- [init?(rawValue: Int)](ckcontainer/applicationpermissionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestApplicationPermission(CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/requestapplicationpermission(_:completionhandler:).md)
  Prompts the user to authorize the specified permission.
- [func status(forApplicationPermission: CKContainer.ApplicationPermissions, completionHandler: (CKContainer.ApplicationPermissionStatus, (any Error)?) -> Void)](ckcontainer/status(forapplicationpermission:completionhandler:).md)
  Determines the authorization status of the specified permission.
- [CKContainer.Application](ckcontainer/application.md)
  A collection of types for app permissions.
- [CKContainer.ApplicationPermissions](ckcontainer/applicationpermissions.md)
  Constants that represent the permissions that a user grants.
- [CKContainer.ApplicationPermissionBlock](ckcontainer/applicationpermissionblock.md)
  A closure that processes the outcome of a permissions request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissionstatus)*