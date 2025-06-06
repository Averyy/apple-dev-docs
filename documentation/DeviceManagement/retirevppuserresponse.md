# RetireVppUserResponse

**Framework**: Devicemanagement  
**Kind**: dictionary

The response from retiring a user.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RetireVppUserResponse
```

#### Discussion

> **Note**:  If the user passes the `userId` value for an already-retired user, this request returns an error that indicates the user has already been retired.

## See Also

- [object RetireVppUserRequest](retirevppuserrequest.md)
  The request to retire a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/retirevppuserresponse)*