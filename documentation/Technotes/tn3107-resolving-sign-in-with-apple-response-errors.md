# TN3107: Resolving Sign in with Apple response errors

**Framework**: Technotes

Diagnose errors received by the Sign in with Apple client, or its server infrastructure, by identifying the underlying causes of common error codes and explore their potential solutions.

#### Overview

This document aids in debugging response errors relating to Sign in with Apple. This information supplements the Sign in with Apple documentation — including [`Sign in with Apple REST API`](https://developer.apple.comhttps://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api), [`Sign in with Apple JS SDK`](https://developer.apple.comhttps://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js), as well as the [`Authentication Services`](https://developer.apple.comhttps://developer.apple.com/documentation/authenticationservices) framework — so start with the documentation first to ensure the client is using the APIs properly.

#### Authorization Response Errors

Errors can occur during Sign in with Apple authorization requests — such as when the client asks permission for the user’s information after a successful Apple ID authentication. For example, the provided [`client ID`](https://developer.apple.comhttps://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/incorporating_sign_in_with_apple_into_other_platforms) is invalid or unauthorized, the [`client ID`](https://developer.apple.comhttps://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_js/incorporating_sign_in_with_apple_into_other_platforms) are incorrect, or the [`redirect URI`](https://developer.apple.comhttps://developer.apple.com/documentation/sign_in_with_apple/configuring_your_environment_for_sign_in_with_apple) is invalid or misconfigured for the web service. When errors occur, the authorizing server sends a standard OAuth error response with an error code.

The following example shows a sample error response in JSON format received from the `/auth/authorize` endpoint:

```None
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error": "invalid_request"
}
```

To help troubleshoot why an authorization error occurred, review the following error code descriptions:

| Error Code | Description | Solution |
| --- | --- | --- |
| `invalid_request` | The authorization request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed. | Check that all parameters are correct, the provided `client_id` exists and is identical to the value registered to your developer account (case-sensitive), etc. |
| `invalid_client` | The authorization request is invalid because the primary app or web service with the provided `client_id` could not be found. | Check that all parameters are correct, the provided `client_id` exists and is identical to the value registered to your developer account (case-sensitive), etc. |
| `unauthorized_client` | The client is not authorized to request an authorization code using this method: The `redirect_uri` of the service either is incorrect or not provided. | Make sure the provided `redirect_uri` is valid, publicly accessible, and is identical to the value registered for the service. |
| `invalid_scope` | The requested `scope` is invalid. | Make sure the request is correct, and that the provided `scope` is supported, etc. |

For more information about OAuth error responses, see [`RFC 6749`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6749#section-4.1.2.1).

#### Token Response Errors

Errors can occur during Sign in with Apple token requests — such as token generation when [`Transferring your apps and users to another team`](https://developer.apple.com/documentation/signinwithapple/transferring-your-apps-and-users-to-another-team) and [`exchanging transfer identifiers`](https://developer.apple.comhttps://developer.apple.com/documentation/signinwithapple/bringing-new-apps-and-users-into-your-team) during user migration, or [`Token validation`](https://developer.apple.com/documentation/signinwithapplerestapi/generate-and-validate-tokens) for a user’s credentials. For example, the provided token is invalid or expired, the client secret — a JSON Web Token (JWT) — is invalid or expired, or the request parameters are incorrect, malformed, or not percent-encoded. When errors occur, the token validation server sends a standard OAuth error response with an error code.

The following example shows a sample error response in JSON format received from the `/auth/token` endpoint:

```None
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error": "invalid_client"
}
```

To help troubleshoot why a token generation or validation error occurred, review the following error code descriptions:

| Error Code | Description | Solution |
| --- | --- | --- |
| `invalid_request` | The token request is missing a required parameter, includes an invalid header or parameter value, includes a parameter more than once, or is otherwise malformed. | Check that the content type is valid, all parameters are correct, the form data is percent-encoded, etc. See [`Possible reasons for invalid request errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-request-errors.md) below for details. |
| `invalid_client` | The token request is invalid because the `client_secret` is invalid or expired, is improperly signed, or is otherwise malformed. | Check that all parameters are correct, the form data is percent-encoded, the JWT header and claim values are correct and the signature is valid, etc. See [`Possible reasons for invalid client errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-client-errors.md) below for details. |
| `invalid_grant` | The client is not authorized for the provided `code` or `refresh_token`, or the `code` or `refresh_token` is invalid, previously consumed, or expired. | Check that all parameters are correct, the provided token is valid, etc. See [`Possible reasons for invalid grant errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-grant-errors.md) below for details. |

For more information about JWTs and their errors, see [`RFC 7519`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519) and [`RFC 7523`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7523#section-3).

#### Revoke Response Errors

Errors can occur during Sign in with Apple revoke requests — such as token revocation after a user account deletion. For example, the provided token does not match the token type hint, the client secret — a JSON Web Token (JWT) — is invalid or expired, or the request parameters are incorrect, malformed, or not percent-encoded. When errors occur, the token revocation server sends a standard OAuth error response with an error code.

The following example shows a sample error response in JSON format received from the `/auth/revoke` endpoint:

```None
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error": "invalid_client"
}
```

To help troubleshoot why a token generation or validation error occurred, review the following error code descriptions:

| Error Code | Description | Solution |
| --- | --- | --- |
| `invalid_request` | The token request is missing a required parameter, includes an invalid header or parameter value, includes a parameter more than once, or is otherwise malformed. | Check that the content type is valid, all parameters are correct, the form data is percent-encoded, etc. See [`Possible reasons for invalid request errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-request-errors.md) below for details. |
| `invalid_client` | The token request is invalid because the `client_secret` is invalid or expired, is improperly signed, or is otherwise malformed. | Check that all parameters are correct, the form data is percent-encoded, the JWT header and claim values are correct and the signature is valid, etc. See [`Possible reasons for invalid client errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-client-errors.md) below for details. |
| `invalid_grant` | The client is not authorized for the provided `code` or `refresh_token`, or the `code` or `refresh_token` is invalid, previously consumed, or expired. | Check that all parameters are correct, the provided token is valid, etc. See [`Possible reasons for invalid grant errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-grant-errors.md) below for details. |

For more information about JWTs and their errors, see [`RFC 7519`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7519) and [`RFC 7523`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7523#section-3).

#### User Migration Info Response Errors

Errors can occur during Sign in with Apple user migration info requests — such as access token generation, [`Transferring your apps and users to another team`](https://developer.apple.com/documentation/signinwithapple/transferring-your-apps-and-users-to-another-team), and [`exchanging transfer identifiers`](https://developer.apple.comhttps://developer.apple.com/documentation/signinwithapple/bringing-new-apps-and-users-into-your-team) for team-scoped user credentials. For example, the provided access token is invalid or expired, the [`Token validation`](https://developer.apple.com/documentation/signinwithapplerestapi/generate-and-validate-tokens) is invalid or expired, the request parameters are incorrect, or the user has [`revoked access`](https://developer.apple.comhttps://support.apple.com/en-us/HT210426) to the client. When errors occur, the user migration info server sends a standard OAuth error response with an error code.

The following example shows a sample error response in JSON format received from the `/auth/usermigrationinfo` endpoint:

```None
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error": "invalid_request"
}
```

To help troubleshoot why a user migration token generation or validation error occurred, review the following error code descriptions:

| Error Code | Description | Solution |
| --- | --- | --- |
| `invalid_request` | The user migration info request is missing a required parameter, includes an invalid header or parameter value, includes a parameter more than once, or is otherwise malformed. | Check that the content type is valid, all parameters are correct, the form data is percent-encoded, etc. See [`Possible reasons for invalid request errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-request-errors.md) below for details. |
| `invalid_client` | The user migration info request is invalid because the `client_secret` is invalid or expired, is improperly signed, or is otherwise malformed. | Check that all parameters are correct, the form data is percent-encoded, the JWT header and claim values are correct and the signature is valid, etc. See [`Possible reasons for invalid client errors`](tn3107-resolving-sign-in-with-apple-response-errors#Possible-reasons-for-invalid-client-errors.md) below for details. |

For more information about OAuth error responses, see [`RFC 6749`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6749#section-4.1.2.1).

#### Possible Reasons for Invalid Request Errors

An `invalid_request` error can occur during a Sign in with Apple request for several reasons, but most commonly for the following scenarios:

- The request has an invalid content type.
- The request is missing a required parameter.
- The request contains an unsupported parameter.
- The request includes multiple user credentials — a mismatched access token, `client_id`, and `client_secret` subject (`sub`) values, or duplicate parameters.
- The user has revoked authorization for the client.

#### Possible Reasons for Invalid Client Errors

An `invalid_client` error can occur during a Sign in with Apple request for several reasons, but most commonly while providing [`Token validation`](https://developer.apple.com/documentation/signinwithapplerestapi/generate-and-validate-tokens) for server validation:

- The request has form data that is not percent-encoded.
- The `client_secret` is missing required headers or payload claims.
- The `client_secret` has a `sub` claim that is not identical to the value registered to your developer account.
- The `client_secret` has expired.
- The `client_secret` signature is invalid or in an unsupported byte format.

To validate the `client_secret` and its signature, see [`JWT.io`](https://developer.apple.comhttps://jwt.io) and [`RFC 7515`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7515#page-45). If you use a third-party library to create, verify, and sign the JWT, make sure the library meets the following criteria for Sign in with Apple:

- Supports `E256` digital signatures
- Supports the required headers and payload claims
- Does not decode using `ASN.1 DER` byte format

#### Possible Reasons for Invalid Grant Errors

An `invalid_grant` error can occur during a Sign in with Apple request for several reasons, but most commonly for the following scenarios while performing [`Token validation`](https://developer.apple.com/documentation/signinwithapplerestapi/generate-and-validate-tokens).

**For authorization code token validation requests:**

- The `client_id` does not match the client for which the `code` was issued.
- The `code` has expired or has been previously consumed by the validation server.

**For refresh token validation requests:**

- The `client_id` does not match the client for which the `refresh_token` was issued.
- The `refresh_token` is invalid or has expired.

#### Revision History

- **2024-01-16** Updated content to include more underlying causes of response errors, and added token revoke endpoint.
- **2022-05-24** Made minor editorial changes.
- **2022-02-15** First published.

## See Also

- [TN3159: Migrating Sign in with Apple users for an app transfer](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer.md)
  Migrate existing Sign in with Apple user identifiers and private email relay addresses by exchanging transfer identifiers from one developer team to another with the user migration info endpoint.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3107-resolving-sign-in-with-apple-response-errors)*