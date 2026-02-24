# UserListResponse.UsersItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains information about an active account on a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+

## Declaration

```swift
object UserListResponse.UsersItem
```

## Properties

- `DataQuota` (integer) *(required)*: If present, the user’s data quota in bytes. This isn’t present if the account doesn’t enforce a quota. This value is available in iOS 9.3 and later.
- `DataUsed` (integer) *(required)*: The amount of data, in bytes, that the user has used. This value is available in iOS 9.3 and later.
- `FullName` (string) *(required)*: The user’s full name. This value is available in macOS 10.13 and later.
- `HasDataToSync` (boolean) *(required)*: If `true`, the user has data to sync to the cloud. This value is available in iOS 9.3 and later.
- `HasSecureToken` (boolean) *(required)*: If `true`, the user currently has a secure token set. This value is available in macOS 11 and later.
- `IsLoggedIn` (boolean) *(required)*: If `true`, the user is currently logged in on the device. This value is available in iOS 9.3 and later, and macOS 10.13 and later.
- `MobileAccount` (boolean) *(required)*: If `true`, the account is a mobile account. This value is available in macOS 10.13 and later.
- `UID` (integer) *(required)*: The user’s unique identifier. This value is available in macOS 10.13 and later.
- `UserGUID` (string) *(required)*: The user’s `GeneratedUID`. This value is available in macOS 10.13 and later.
- `UserName` (string) *(required)*: The user name for the account. In macOS, this is the short name of the user account. This value is available in iOS 9.3 and later, and macOS 10.13 and later.

## See Also

- [object UserListResponse.ErrorChainItem](userlistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userlistresponse/usersitem)*