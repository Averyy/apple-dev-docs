# Request an authorization

**Framework**: Account & Organizational Data Sharing  
**Kind**: httpRequest

Request a user authorization to Account & Organizational Data Sharing apps and web services.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

## Endpoint

`GET https://appleid.apple.com/auth/oauth2/v2/authorize`

## Parameters

- `client_id` (string) *(required)*: The identifier (App ID or Services ID) for your app. To prevent exposing sensitive data to the end user, don’t include your Team ID in the identifier.
- `nonce` (string): A unique, single-use string that your app provides to associate a client session with the user’s identity token. This value also prevents replay attacks, and correlates the initial authentication request to the identity token provided in the authorization response.
- `redirect_uri` (string) *(required)*: The destination URI associated with your app that the authorization redirects. The URI must use the HTTPS protocol, include a domain name, can’t be an IP address or `localhost`, and must not contain a fragment identifer (`#`).
- `response_mode` (string)
- `response_type` (string) *(required)*: The type of response requested. Use the value `code`.
- `scope` (string) *(required)*: The amount of personal information your app or web service requests from Apple’s servers. Valid values are `edu.users.read` and `edu.classes.read`. You can request one, both, or none. Use space separation and percent-encoding for multiple scopes; for example, `"scope=edu.users.read%20edu.classes.read"`.
- `state` (string): An arbitrary string that your app provides to represent the current state of the authorization request. This value mitigates cross-site request forgery attacks by comparing against the state value contained in the authorization response.

## See Also

- [Token revocation](revoke-tokens.md)
  Invalidate the tokens and associated user authorizations for someone when they are no longer associated with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/request-an-authorization)*