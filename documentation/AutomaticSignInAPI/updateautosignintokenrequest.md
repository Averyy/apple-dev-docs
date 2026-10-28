# UpdateAutoSignInTokenRequest

**Framework**: Automatic Sign-In API  
**Kind**: dictionary  
**Role**: Object

The request body that contains the old sign-in token and the new sign-in token.

**Availability**:
- Automatic Sign-In API 1.0+

## Declaration

```
object UpdateAutoSignInTokenRequest
```

## Overview

This is the request object for the [`Update Sign-In Token`](./update-this-token-for-all-associated-users.md) endpoint.

## Properties

- `existingAutoSignInTokenValue` (string): The sign-in token [`value`](../VideoSubscriberAccount/vsautosignintoken/value.md) that needs to be updated.
- `newAutoSignInTokenValue` (string): The new sign-in token [`value`](../VideoSubscriberAccount/vsautosignintoken/value.md).

## See Also

### Token updates
- [Update Sign-In Token](./update-this-token-for-all-associated-users.md)
  Updates a specific sign-in token to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticsigninapi/updateautosignintokenrequest)*