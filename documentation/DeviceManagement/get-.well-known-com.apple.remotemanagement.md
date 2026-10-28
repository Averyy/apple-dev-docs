# Discover Authentication Servers

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of available authentication servers.

## Discussion

Each server entry corresponds to a server that supports a different version of the protocol. The client selects the server with the most recent version that matches its own most recent supported version.

## Topics

### Supporting Objects
- [object WellKnown](./wellknown.md)
  A list of available servers used for authentication.

## Endpoint

`GET https://yourmdmhost.example.com/.well-known/com.apple.remotemanagement`

## Parameters

### Query Parameters

- `model-family` (string): **Allowed Values**: `Mac`, `iPhone`, `iPad`, `AppleTV`, `Watch`, `RealityDevice`
- `user-identifier` (string)

## Responses

- `200` OK (`WellKnown`, `application/json`): A list of servers the client device can use for authentication.

## See Also

### Objects
- [object EnrollmentSSODocument](./enrollmentssodocument.md)
  Enrollment SSO streamlines the MDM enrollment process, reduces sign-ins, and improves security.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-.well-known-com.apple.remotemanagement)*