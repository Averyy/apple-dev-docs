# UserListResponse.UsersItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains information about an active account on a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.13+

## Declaration

```swift
object UserListResponse.UsersItem
```

## Properties

- `DataQuota` (integer) *(required)*: If present, the user’s data quota in bytes. This isn’t present if the account doesn’t enforce a quota. Available: iOS 9.3+ | iPadOS 9.3+
- `DataUsed` (integer) *(required)*: The amount of data, in bytes, that the user has used. Available: iOS 9.3+ | iPadOS 9.3+
- `FullName` (string) *(required)*: The user’s full name. Available: macOS 10.13+
- `HasDataToSync` (boolean) *(required)*: If `true`, the user has data to sync to the cloud. Available: iOS 9.3+ | iPadOS 9.3+
- `HasSecureToken` (boolean) *(required)*: If `true`, the user currently has a secure token set. Available: macOS 11+
- `IsLoggedIn` (boolean) *(required)*: If `true`, the user is currently logged in on the device.
- `MobileAccount` (boolean) *(required)*: If `true`, the account is a mobile account. Available: macOS 10.13+
- `UID` (integer) *(required)*: The user’s unique identifier. Available: macOS 10.13+
- `UserGUID` (string) *(required)*: The user’s `GeneratedUID`. Available: macOS 10.13+
- `UserName` (string) *(required)*: The user name for the account. In macOS, this is the short name of the user account.

## See Also

- [object UserListResponse.ErrorChainItem](userlistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userlistresponse/usersitem)*