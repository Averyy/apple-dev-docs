# Get Token

**Framework**: Device Management  
**Kind**: httpRequest

Gets a token from the server.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 1.1+

#### Discussion

A server that supports this request needs to include a `com.apple.mdm.token` value in the `ServerCapabilities` key of the MDM profile payload to enroll the device.

This request allows devices to fetch security-related tokens from the server and to retrieve different types of tokens for the various services that need them. Each service has a unique identifier, and can pass a specific set of parameters for the server to use when generating the token. If the server doesn’t recognize the service type, it needs to return a `400` HTTP response status.

> **Note**:  The `GetBootstrapToken` request is a separate request specifically for the bootstrap token.

##### Support Access Management for Managed Apple Accounts

For the service type `com.apple.maid`, the Apple Identity Service requests this token when a Managed Apple Account is signing in, and then uses it to verify that the Managed Apple Account belongs to the same organization as the MDM server that enrolled the device. The token is a JSON Web Token (JWT) per RFC 7519 with the following claims:

- `iss`: A `String`, per RFC 7519 section 4.1.1, that the server sets to the system-generated server identifier (`server_uuid`) that [`AccountDetail`](accountdetail.md) returns.
- `iat`: A `NumericDate`, per RFC 7519 section 4.1.6, that the server sets to the timestamp of the token generation. The Apple Identity Service uses this value to limit the time that the token is valid.
- `jti`: A `String`, per RFC 7519 section 4.1.7, that the server sets to a unique identifier (a random UUID) for the JWT. The Apple Identity Service uses this value to ensure that it only uses the token once.
- `service_type`: A `String` that the server sets to the value of the `TokenServiceType` key in the `CheckIn` request, which needs to be `com.apple.maid`.

Sign the JWT using the server’s private key that corresponds to the RFC 3280 public key certificate that’s registered with Apple Business Manager or Apple School Manager.

##### Support Apple Watch Pairing

For the service type `com.apple.watch.pairing`, the MDM server requests this token to enroll an Apple Watch, with the request coming from the phone that’s paired to the watch. The format of the token is implementation-defined, but the phone and watch MDM servers need to use the same format. The purpose of this token is to confirm the pairing relationship of the watch to the phone, and to ensure that the phone is already enrolled in an MDM server that belongs to the same organization as the watch MDM server. Ensure that the token is cryptographically protected against tampering, spoofing, and replay attacks.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, visionOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |

## Topics

### Requests and responses
- [object GetTokenRequest](gettokenrequest.md)
  The get token request details.
- [object GetTokenResponse](gettokenresponse.md)
  The get token response details.

## Request Body

The request object the system sends for the `GetToken` request.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [User Authenticate](user-authenticate.md)
  Authenticates a user with a two-step authentication protocol.
- [Check Out](check-out.md)
  Responds to the removal of the MDM enrollment profile from a device.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token from the server.
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sends the bootstrap token to the server.
- [Return To Service](return-to-service.md)
  Gets the return-to-service configuration from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-token)*