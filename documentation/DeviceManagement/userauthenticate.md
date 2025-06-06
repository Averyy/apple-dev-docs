# UserAuthenticate

**Framework**: Device Management  
**Kind**: httpRequest

Authenticates a user with a two-step authentication protocol.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

A [`UserAuthenticate`](userauthenticate.md) handshake usually consists of two transactions between client and server. Upon receiving the first request from the client, the server should respond with a 200 status code and a dictionary containing a `DigestChallenge` key (string).

A zero-length `DigestChallenge` provided by the server indicates that the server does not require any `AuthToken` to be generated for this user. Otherwise, the client generates a digest from the user’s short name, the user’s clear-text password and the `DigestChallenge` value provided by the server. The resulting digest is sent in a second [`UserAuthenticate`](userauthenticate.md) request to the server, which validates the response and returns a dictionary that contains an `AuthToken` value that is sent subsequent commands on the user channel (to both the `ServerURL` and `CheckInURL`).

If the server rejects the `DigestResponse` value because of an invalid password, it must return a `200` response and an empty `AuthToken` value. If the server does not want to mange this user, it returns a `410` status code to the initial `UserAuthenticate` request. The client will not make any additional requests to the server on behalf of this user for the duration of this login session.

The next time the user logs in, the client sends a new request and the server can optionally return `410` again. The `AuthToken` remains valid until the next time the client sends a [`UserAuthenticate`](userauthenticate.md) request. The client initiates a handshake each time a mobile or network user logs in.

## Topics

### Request
- [object UserAuthenticateRequest](userauthenticaterequest.md)
  The User Authenticate Request details.

## Request Body

The request object for two-step user authentication.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [Check Out](check-out.md)
  Responds to the removal of the MDM enrollment profile from a device.
- [Get Token](get-token.md)
  Check-in protocol get-token data.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token.
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sets the bootstrap token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userauthenticate)*