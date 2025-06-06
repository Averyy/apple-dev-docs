# Revoke tokens

**Framework**: Account & Organizational Data Sharing  
**Kind**: httpRequest

Invalidate the tokens and associated user authorizations for someone when they are no longer associated with your app.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

#### Overview

To revoke authorization for a user, you must obtain a valid refresh token or access token. If you don’t have either token for the user, you can generate tokens when validating an authorization code. For more information about user tokens and creating client secrets, see [`Generate and validate tokens`](generate-and-validate-tokens.md).

To invalidate a user’s refresh token, invoke the revoke endpoint with the following `HTTP POST` method:

```sh
curl -v POST "https://appleid.apple.com/auth/oauth2/v2/revoke" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'token=REFRESH_TOKEN' \
-d 'token_type_hint=refresh_token'
```

Additionally, to invalidate a user’s access token, use the following `HTTP POST` method:

```sh
curl -v POST "https://appleid.apple.com/auth/oauth2/v2/revoke" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'token=ACCESS_TOKEN' \
-d 'token_type_hint=access_token'
```

For either token revocation request, the revoke endpoint returns a `200` response code without a response body after the server invalidates the `token` value, or if the token was previously invalidated. If the server encounters an error, it returns an [`ErrorResponse`](errorresponse.md) that identifies the problem.

## Request Body

The list of input parameters required for the server to invalidate the token.

## See Also

- [Request an authorization](request-an-authorization.md)
  Request a user authorization to Account & Organizational Data Sharing apps and web services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/revoke-tokens)*