# Token revocation

**Framework**: SigninwithAppleRESTAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Invalidate the tokens and associated user authorizations for a user when they are no longer associated with your app.

**Availability**:
- Sign in with Apple REST API 1.0+

#### Discussion

In order to revoke authorization for a user, you must obtain a valid refresh token or access token. If you don’t have either token for the user, you can generate tokens when validating an authorization code. For more information about user tokens and creating client secrets, see [`Token validation`](./generate-and-validate-tokens.md).

To invalidate a user’s refresh token, invoke the revoke endpoint with the following HTTP POST method.

```console
curl -v POST "https://appleid.apple.com/auth/revoke" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'token=REFRESH_TOKEN' \
-d 'token_type_hint=refresh_token'
```

Additionally, to invalidate a user’s access token, use the following HTTP POST method.

```console
curl -v POST "https://appleid.apple.com/auth/revoke" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'token=ACCESS_TOKEN' \
-d 'token_type_hint=access_token'
```

For either token revocation request, the `revoke` endpoint returns a `200` response code without a response body after the server invalidates the `token` value, or if the `token` value was previously invalidated. If the response contains an error, please see [`ErrorResponse`](./errorresponse.md) for the specific error code provided in the response body.

## Endpoint

`POST https://appleid.apple.com/auth/revoke`

## Request Body

**Content-Type**: `application/x-www-form-urlencoded`  
**Type**: `form-data`

The list of input parameters required for the server to invalidate the token.

- `client_id` (string) *(required)*: The identifier (App ID or Services ID) for your app. The identifier must match the value provided during the authorization request for the user’s information. Additionally, the identifier must not include your Team ID, to help mitigate the possibility of exposing sensitive data to the end user.
- `client_secret` (string) *(required)*: A secret JSON Web Token (JWT) that uses the Sign in with Apple private key associated with your developer account. For more information about creating client secrets, see  [Creating a client secret](../AccountOrganizationalDataSharing/creating-a-client-secret.md).
- `token` (string) *(required)*: The user refresh token or access token intended to be revoked. The user session associated with the token provided is revoked if the request is successful.
- `token_type_hint` (string): A hint about the type of the token submitted for revocation. Use `refresh_token` or `access_token`.

## Responses

- `200` OK (`application/json`): The request was successful; the provided token has been revoked successfully or was previously invalid.
- `400` Bad Request (`ErrorResponse`, `application/json`): The server was unable to process the request. See the error code description for more information about the underlying error.

## See Also

### Generating and revoking tokens
- [Creating a client secret](../AccountOrganizationalDataSharing/creating-a-client-secret.md)
  Generate a signed token to identify your client application.
- [Fetch Apple’s public key to verify token signatures](./fetch-apples-public-key-for-verifying-token-signature.md)
  Fetch Apple’s public key to verify ID token and server notification signatures.
- [Token validation](./generate-and-validate-tokens.md)
  Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/revoke-tokens)*