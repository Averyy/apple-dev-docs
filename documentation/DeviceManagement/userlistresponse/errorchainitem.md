# UserListResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object UserListResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object UserListResponse.UsersItem](userlistresponse/usersitem.md)
  A dictionary that contains information about an active account on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userlistresponse/errorchainitem)*