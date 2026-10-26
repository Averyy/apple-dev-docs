# Request an authorization to the Sign in with Apple server

**Framework**: SigninwithAppleRESTAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a Sign in with Apple authorization flow to apps and web services that can’t directly access Sign in with Apple JS.

**Availability**:
- Sign in with Apple REST API 1.0+

## Mentions

- [Receiving a User’s Identity Token](../SigninwithApple/receiving-a-users-identity-token.md)

#### Discussion

Use this endpoint to request authorization for your app to receive the user’s information with Sign in with Apple. If your app is contained within an app group, the user credentials are associated with the primary app and shared across the group. To learn more about app groups, visit [Configuring your environment for Sign in with Apple](../SigninwithApple/configuring-your-environment-for-sign-in-with-apple.md).

##### Get the user information and tokens

When the Sign in with Apple UI appears in the opened browser tab, the user can sign in and accept any terms and conditions for your app. After Apple processes the authorization request, the handling of the response depends on the value in `response_mode`:

- For the `query` value, the response parameters are added to the `redirect_uri` value as query parameters, and the browser is redirected to the resulting value.
- For the `fragment` value, the response parameters are added to the `redirect_uri` value as a fragment, and the browser is redirected.
- For the `form_post` value, an HTTP POST request containing the results of the authorization is sent to the `redirectURI`. The HTTP body contains the result parameters with `application/x-www-form-urlencoded` content type.

A successful response contains the following parameters:

- **`code`**: A single-use authorization grant code that’s valid for five minutes. To learn how to validate this code to obtain user tokens, see [`Token validation`](./generate-and-validate-tokens.md).
- **`id_token`**: A JSON web token (JWT) containing the user’s identity information. For more information, see [`id_token`](../SigninwithAppleJS/authorizationi/id_token.md).
- **`state`**: The state contained in the authorization request. Compare against the state value provided in the initial authorization request to help prevent cross-site request forgery attacks.
- **`user`**: A JSON string containing the data requested in the `scope` property. The returned data is in the following format: `{ "name": { "firstName": string, "lastName": string }, "email": string }`

> ❗ **Important**:  For privacy, Apple doesn’t receive the user’s full name shared with the system UI. Therefore, the raw data is passed directly to your app from the browser and is not included in the user’s identity token. To prevent cross-site scripting attacks, validate and sanitize the user-submitted first and last name values before storing on your app servers.

Apple only returns the user object the first time the user authorizes the app. Validate and persist this information from your app to your server. Subsequent authorization requests do not contain the `user` object, however, the user’s email is provided in the identity token for all requests. For more information, visit [Authenticating users with Sign in with Apple](../SigninwithApple/authenticating-users-with-sign-in-with-apple.md).

If an error occurs, the HTTP body contains the following parameters:

- **`error`**: The returned error code
- **`state`**: The state contained in the authorization request. Compare against the state value provided in the initial authorization request to help prevent cross-site request forgery attacks.

> **Note**:  The only error code that might be returned is `user_cancelled_authorize`. This error code is returned if the user clicks the cancel button during the web flow.

##### Implement the authorization flow

**Request**:

```
https://appleid.apple.com/auth/authorize?client_id=[CLIENT_ID]&redirect_uri=[REDIRECT_URL]&response_type=code id_token&state=[STATE]&scope=[SCOPES]&response_mode=form_post
```

**Response**:

```json
{
     "authorization": {
       "code": "[CODE]",
       "id_token": "[ID_TOKEN]",
       "state": "[STATE]"
     },
     "user": {
       "email": "[EMAIL]",
       "name": {
         "firstName": "[FIRST_NAME]",
         "lastName": "[LAST_NAME]"
       }
     }
}
```

##### Return control to the app

At the end of the authorization flow, Apple performs a `form_post` to the `redirect_uri` value you provided in the request. At this point, the authorization flow is complete, and it’s your server’s responsibility to securely persist the data and return control to the app.

Platforms that support custom URL schemes — iOS 12.0 and earlier and Android — must handle the data resulting from the authorization flow by storing it on their app server in the logic of their `redirect_uri` endpoint. You then redirect the custom URL scheme to give control back to the app.

> ❗ **Important**:  To help prevent cross-site request forgery attacks, ensure the `state` values contained in the request and response are identical before handling the redirect in your app.

## Endpoint

`GET https://appleid.apple.com/auth/authorize`

## Parameters

### Query Parameters

- `client_id` (string) *(required)*: The identifier (App ID or Services ID) for your app. The identifier must not include your Team ID, to help prevent the possibility of exposing sensitive data to the end user.
- `nonce` (string): A unique, single-use string that your app provides to associate a client session with the user’s identity token. This value is also used to prevent replay attacks, and allows you to correlate the initial authentication request with the identity token provided in the authorization response.
- `redirect_uri` (string) *(required)*: The destination URI associated to your app, to which the authorization redirects. The URI must use the HTTPS protocool, include a domain name, can’t be an IP address or localhost, and must not contain a fragment identifer (#). For more information, see [Configuring your environment for Sign in with Apple](../SigninwithApple/configuring-your-environment-for-sign-in-with-apple.md).
- `response_mode` (string): The type of response mode expected. Valid values are `query`, `fragment`, and `form_post`. If you requested any scopes, the value must be `form_post`.
- `response_type` (string) *(required)*: The type of response requested. Valid values are `code` and `id_token`. You can request only `code`, or both `code` and `id_token`. Requesting only `id_token` is unsupported. When requesting `id_token`, `response_mode` must be either `fragment` or `form_post`.
- `scope` (string): The amount of user information requested from Apple. Valid values are `name` and `email`. You can request one, both, or none. Use space separation and percent-encoding for multiple scopes; for example, `"scope=name%20email"`.
- `state` (string): An arbitrary string that your app provides, representing the current state of the authorization request. This value is also used to mitigate cross-site request forgery attacks, by comparing against the state value contained in the authorization response.

## Responses

- `200` OK (`application/json`): Request succeeded.
- `404` Not Found (`application/json`): Resource not found.

## See Also

### Authentication and verification of users
- [Authenticating users with Sign in with Apple](../SigninwithApple/authenticating-users-with-sign-in-with-apple.md)
  Securely authenticate users and create accounts for them in your app.
- [Receiving a User’s Identity Token](../SigninwithApple/receiving-a-users-identity-token.md)
  Retrieve the user’s information from Apple Account servers
- [Verifying a user](../SigninwithApple/verifying-a-user.md)
  Check the validity and integrity of a user’s identity token.
- [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md)
  Manage user-initiated modifications to maintain privacy with server-to-server notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/request-an-authorization-to-the-sign-in-with-apple-server.)*