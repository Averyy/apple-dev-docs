# EditVppUserRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request to edit a user.

**Availability**:
- VPP License Management 1.0+

## Declaration

```
object EditVppUserRequest
```

## Properties

- `clientUserIdStr` (string): The identifier supplied by the client when registering a user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.
- `email` (string): The user’s email address. The `email` field updates only if the value is provided in the request.
- `itsIdHash` (string): The hash of the user’s iTunes Store ID.
- `managedAppleIDStr` (string): The Apple Account associated with the user. This ID’s organization must match that of the provided `sToken`.
- `sToken` (string) *(required)*: The authentication token. For more information, see [Authenticate with the web service](./managing-apps-and-books-through-web-services-legacy.md#Authenticate-with-the-web-service).
- `userId` (int64): The unique identifier assigned by the VPP when registering the user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.

## See Also

### Request and Response
- [object EditVppUserResponse](./editvppuserresponse.md)
  The response from editing a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/editvppuserrequest)*