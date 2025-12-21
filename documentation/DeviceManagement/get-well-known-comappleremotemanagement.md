# Discover Authentication Servers

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of available authentication servers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Each server entry corresponds to a server that supports a different version of the protocol. The client selects the server with the most recent version that matches its own most recent supported version.

## Topics

### Supporting Objects
- [object WellKnown](wellknown.md)
  A list of available servers used for authentication.

## See Also

- [object EnrollmentSSODocument](enrollmentssodocument.md)
  Enrollment SSO streamlines the MDM enrollment process, reduces sign-ins, and improves security.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-.well-known-com.apple.remotemanagement)*