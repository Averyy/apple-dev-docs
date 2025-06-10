# Generate and validate tokens

**Framework**: Account & Organizational Data Sharing  
**Kind**: httpRequest

Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

#### Overview

The validation server returns a [`TokenResponse`](tokenresponse.md) object in the response body of a successful validation request. Use this endpoint to either authorize a user by validating the authorization code received by your app, or by validating an existing refresh token to verify a user session or obtain access tokens.

##### Validate the Authorization Grant Code

When you send an authorization request to the validation server, include the following form data parameters:

- `client_id`
- `client_secret`
- `code`
- `grant_type`
- `redirect_uri`

> **Note**: When authorizing a user with your app, include the `redirect_uri` parameter only if the application provided a `redirect_uri` in the initial authorization request.

For information on how to create the JWT that you use as the client secret, see [`Creating a client secret`](creating-a-client-secret.md).

The following is an example authorization validation request URL via `curl`:

```sh
curl -v POST "https://appleid.apple.com/auth/oauth2/v2/token" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'code=CODE' \
-d 'grant_type=authorization_code' \
-d 'redirect_uri=REDIRECT_URI'
```

After the server validates the authorization code, the endpoint returns the identity token, an access token, and a refresh token. The following is an example authorization validation response:

```js
{
	"access_token": "adg61...670r9",
	"token_type": "Bearer",
	"expires_in": 3600,
	"refresh_token": "rca7...lABoQ",
	"id_token": "eyJra...96sZg"
}
```

Use the refresh token to verify the user session from the server and obtain access tokens.

##### Validate an Existing Refresh Token

When performing a validation request, you must include the following form data parameters:

- `client_id`
- `client_secret`
- `grant_type`
- `refresh_token`

For information on how to create the JWT you use as the client secret, see [`Creating a client secret`](creating-a-client-secret.md).

The following is an example validation request URL using `curl`:

```sh
curl -v POST "https://appleid.apple.com/auth/oauth2/v2/token" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'grant_type=refresh_token' \
-d 'refresh_token=REFRESH_TOKEN'
```

After the server validates the refresh token, the endpoint returns the identity token and an access token. The following is an example refresh token validation response:

```js
{
  "access_token": "beg510...670r9",
  "token_type": "Bearer",
  "expires_in": 3600,
  "id_token": "eyJra...96sZg"
}
```

## Request Body

The list of input parameters required for the server to validate the authorization code or refresh token.

## See Also

- [Creating a client secret](creating-a-client-secret.md)
  Generate a signed token to identify your client application.
- [Fetch Apple's public key for verifying token signature](fetch-apple's-public-key-for-verifying-token-signature.md)
  Retrieve the public key associated with the cryptographic identity Apple uses to sign the token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/generate-and-validate-tokens)*