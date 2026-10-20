# CKContainer.ApplicationPermissionStatus.granted

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The user grants the permission.

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
case granted
```

```c
CKApplicationPermissionStatusGranted
```

## See Also

### Permission Statuses
- [CKContainer.ApplicationPermissionStatus.initialState](./initialstate.md)
  The app is yet to request the permission.
- [CKContainer.ApplicationPermissionStatus.couldNotComplete](./couldnotcomplete.md)
  An error that occurs while processing the permission request.
- [CKContainer.ApplicationPermissionStatus.denied](./denied.md)
  The user denies the permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/applicationpermissionstatus/granted)*