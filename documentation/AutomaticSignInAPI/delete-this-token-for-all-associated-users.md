# Delete Sign-In Token

**Framework**: Automatic Sign-In API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes a specific sign-in token.

**Availability**:
- Automatic Sign-In API 1.0+

## Mentions

- [Signing people in to their media accounts automatically](../VideoSubscriberAccount/signing-people-in-to-media-apps-automatically.md)

#### Overview

Use this endpoint to delete a specific [`value`](../VideoSubscriberAccount/vsuseraccountmanager/autosignintoken-swift.struct/value.md).

## Endpoint

`POST https://api.storekit-sandbox.itunes.apple.com/account/v1/autoSignIn/delete`

## Request Body

**Content-Type**: `application/json`  
**Type**: `DeleteAutoSignInTokenRequest`

The request body that contains the sign-in token to be deleted.

## Responses

- `204` No Content: The request succeeded.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `404` Not Found: Token not found.

## See Also

### Token deletion
- [object DeleteAutoSignInTokenRequest](./deleteautosignintokenrequest.md)
  The request body that contains the sign-in token to be deleted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticsigninapi/delete-this-token-for-all-associated-users)*