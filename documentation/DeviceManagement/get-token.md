# Get Token

**Framework**: Device Management  
**Kind**: httpRequest

Check-in protocol get-token data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

A server that supports this request needs to include a `com.apple.mdm.token` value in the `ServerCapabilities` key of the MDM profile payload to enroll the device.

This request allows devices to fetch security-related tokens from the server and to retrieve different types of tokens for the different services that need them. Each service has a unique identifier, and can pass a specific set of parameters for the server to use when generating the token. If the server doesn’t recognize the service type, it needs to return a `400` HTTP response status.

> **Note**:  The `GetBootstrapToken` request is a separate request specifically for the bootstrap token.

 The `GetBootstrapToken` request is a separate request specifically for the bootstrap token.

##### Support Access Management for Managed Apple Ids

For the service `type com.apple.maid`, the Apple Identity Service requests this token when a Managed Apple ID is signing in. It’s used to verify that the Managed Apple ID belongs to the same organization as the MDM server that enrolled the device. The token is a JSON Web Token (JWT) per RFC7519 with the following claims:

- `iss`: A String, per RFC7519 Section 4.1.1, that the server sets to the system-generated server identifier (`server_uuid`) that [`AccountDetail`](accountdetail.md) returns.
- `iat`: A NumericDate, per RFC7519 Section 4.1.6, that the server sets to the timestamp for when it generated the token. The system uses this value to limit the time period that the token is valid.
- `jti`: A String, per RFC7519 Section 4.1.7, that the server sets to a unique identifier (a random UUID) for the JWT. The system uses this value to ensure that a token is only used once.
- `service_type`: A String that the server sets to the value of the `TokenServiceType` key included in the `CheckIn` request, which needs to be `com.apple.maid`.

Sign the JWT using the server’s private key that corresponds to the IETF RFC 3280 compliant public key certificate that’s registered with Apple Business or School Manager.

##### Support Apple Watch Pairing

For the service type `com.apple.watch.pairing`, the MDM server requests this token to enroll a watch, with the request coming from the phone that’s paired to the watch. The format of the token is implementation-defined, but the phone and watch MDM servers need to use the same format. The purpose of this token is to confirm the pairing relationship of the watch to the phone, and that the phone is already enrolled in an MDM server that belongs to the same organization as the watch MDM server. Ensure that the token is cryptographically protected against tampering, spoofing, and replay attacks.

## Topics

### Request and Response
- [object GetTokenRequest](gettokenrequest.md)
  Check-in protocol get-token request data.
- [object GetTokenResponse](gettokenresponse.md)
  Check-in protocol get-token response data.

## Request Body

Check-in protocol get-token request.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [UserAuthenticate](userauthenticate.md)
  Authenticates a user with a two-step authentication protocol.
- [Check Out](check-out.md)
  Responds to the removal of the MDM enrollment profile from a device.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token.
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sets the bootstrap token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-token)*