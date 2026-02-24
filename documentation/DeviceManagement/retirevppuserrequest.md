# RetireVppUserRequest

**Framework**: Device Management  
**Kind**: dictionary

The request to retire a user.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RetireVppUserRequest
```

## Properties

- `clientUserIdStr` (string): The identifier supplied by the client when registering a user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.
- `sToken` (string) *(required)*: The authentication token. For more information, see [`Authentication`](managing-apps-and-books-through-web-services-legacy#Authentication.md).
- `userId` (int64): The unique identifier assigned by the VPP when registering the user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.

## See Also

- [object RetireVppUserResponse](retirevppuserresponse.md)
  The response from retiring a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retirevppuserrequest)*