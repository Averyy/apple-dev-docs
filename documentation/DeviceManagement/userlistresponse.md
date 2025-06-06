# UserListResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to get a list of users with active accounts.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object UserListResponse
```

## Topics

### Commands
- [object UserListResponse.UsersItem](userlistresponse/usersitem.md)
  A dictionary that contains information about an active account on a device.
- [object UserListResponse.ErrorChainItem](userlistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## See Also

- [object UserListCommand](userlistcommand.md)
  The command to get a list of users with active accounts on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userlistresponse)*