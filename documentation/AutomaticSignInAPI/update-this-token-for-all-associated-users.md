# Update Sign-In Token

**Framework**: Automatic Sign-In API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Updates a specific sign-in token to a new value.

**Availability**:
- Automatic Sign-In API 1.0+

## Mentions

- [Signing people in to their media accounts automatically](../VideoSubscriberAccount/signing-people-in-to-media-apps-automatically.md)

## Overview

Use this endpoint to update a specific [`VSUserAccountManager.AutoSignInToken`](../VideoSubscriberAccount/vsuseraccountmanager/autosignintoken-swift.struct.md) to a new [`value`](../VideoSubscriberAccount/vsautosignintoken/value.md).

## Endpoint

`POST https://api.storekit-sandbox.itunes.apple.com/account/v1/autoSignIn/update`

## Request Body

**Content-Type**: `application/json`  
**Type**: `UpdateAutoSignInTokenRequest`

The request body that contains the old sign-in token and the new sign-in token.

## Responses

- `204` No Content: The request succeeded.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `404` Not Found: Token not found.

## See Also

### Token updates
- [object UpdateAutoSignInTokenRequest](./updateautosignintokenrequest.md)
  The request body that contains the old sign-in token and the new sign-in token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticsigninapi/update-this-token-for-all-associated-users)*