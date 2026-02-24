# EditVppUserRequest

**Framework**: Device Management  
**Kind**: dictionary

The request to edit a user.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EditVppUserRequest
```

## Properties

- `clientUserIdStr` (string): The identifier supplied by the client when registering a user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.
- `email` (string): The user’s email address. The `email` field is updated only if the value is provided in the request.
- `itsIdHash` (string): The hash of the user’s iTunes Store ID.
- `managedAppleIDStr` (string): The Apple Account associated with the user. This ID’s organization must match that of the provided sToken. See [`Associating an Apple Account with a Volume Purchase Program (VPP) User`](associating-an-apple-id-with-a-volume-purchase-program-vpp-user.md) for more information.
- `sToken` (string) *(required)*: The authentication token. For more information, see [`Authentication`](managing-apps-and-books-through-web-services-legacy#Authentication.md).
- `userId` (int64): The unique identifier assigned by the VPP when registering the user. Either `clientUserIdStr` or `userId` is required. If both `clientUserIdStr` and `userId` are supplied, `userId` takes precedence.

## See Also

- [object EditVppUserResponse](editvppuserresponse.md)
  The response from editing a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/editvppuserrequest)*