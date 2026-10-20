# DeleteAutoSignInTokenRequest

**Framework**: Automatic Sign-In API  
**Kind**: dictionary  
**Role**: Object

The request body that contains the sign-in token to be deleted.

**Availability**:
- Automatic Sign-In API 1.0+

## Declaration

```
object DeleteAutoSignInTokenRequest
```

#### Overview

This is the request object for the [`Delete Sign-In Token`](./delete-this-token-for-all-associated-users.md) endpoint.

## Properties

- `autoSignInTokenValue` (string): The token [`value`](../VideoSubscriberAccount/vsautosignintoken/value.md) that needs to be deleted.

## See Also

### Token deletion
- [Delete Sign-In Token](./delete-this-token-for-all-associated-users.md)
  Deletes a specific sign-in token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticsigninapi/deleteautosignintokenrequest)*