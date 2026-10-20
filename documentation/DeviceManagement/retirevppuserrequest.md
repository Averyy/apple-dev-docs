# RetireVppUserRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request to retire a user.

**Availability**:
- VPP License Management 1.0+

## Declaration

```
object RetireVppUserRequest
```

## Properties

- `clientUserIdStr` (string): The identifier supplied by the client when registering a user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.
- `sToken` (string) *(required)*: The authentication token. For more information, see [Authenticate with the web service](./managing-apps-and-books-through-web-services-legacy.md#Authenticate-with-the-web-service).
- `userId` (int64): The unique identifier assigned by the VPP when registering the user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.

## See Also

### Request and Response
- [object RetireVppUserResponse](./retirevppuserresponse.md)
  The response from retiring a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retirevppuserrequest)*