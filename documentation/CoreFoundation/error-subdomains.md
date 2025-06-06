# Error Subdomains

**Framework**: Core Foundation

Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.

#### Overview

Error codes in the `kCFStreamErrorDomainSOCKS` domain can come from multiple parts of the protocol stack, many of which define their own error values as part of outside specifications such as the HTTP specification.

To avoid confusion from conflicting error numbers, error codes in the `kCFStreamErrorDomainSOCKS` domain contain two parts: a subdomain, which tells which part of the protocol stack generated the error, and the error code itself.

Calling [`CFSocketStreamSOCKSGetErrorSubdomain(_:)`](https://developer.apple.com/documentation/CFNetwork/CFSocketStreamSOCKSGetErrorSubdomain(_:)) returns an identifier that tells which layer of the protocol stack produced the error. This list of constants contains the possible values that this function will return.

Calling [`CFSocketStreamSOCKSGetError(_:)`](https://developer.apple.com/documentation/CFNetwork/CFSocketStreamSOCKSGetError(_:)) returns the actual error code that the subdomain describes.

## Topics

### Constants
- [var kCFStreamErrorSOCKSSubDomainNone: Int { get }](../CFNetwork/kCFStreamErrorSOCKSSubDomainNone.md)
  A general SOCKS error.
- [var kCFStreamErrorSOCKSSubDomainVersionCode: Int { get }](../CFNetwork/kCFStreamErrorSOCKSSubDomainVersionCode.md)
  The version of SOCKS that the server wants to use.
- [var kCFStreamErrorSOCKS4SubDomainResponse: Int { get }](../CFNetwork/kCFStreamErrorSOCKS4SubDomainResponse.md)
  The SOCKS4 status code returned by the server.
- [var kCFStreamErrorSOCKS5SubDomainUserPass: Int { get }](../CFNetwork/kCFStreamErrorSOCKS5SubDomainUserPass.md)
  The status code that the server returned during authentication.
- [var kCFStreamErrorSOCKS5SubDomainMethod: Int { get }](../CFNetwork/kCFStreamErrorSOCKS5SubDomainMethod.md)
  The server’s desired negotiation method.
- [var kCFStreamErrorSOCKS5SubDomainResponse: Int { get }](../CFNetwork/kCFStreamErrorSOCKS5SubDomainResponse.md)
  The response code that the server returned in reply to the connection request.

## See Also

- [enum CFStreamStatus](cfstreamstatus.md)
  Constants that describe the status of a stream.
- [enum CFStreamErrorDomain](cfstreamerrordomain.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Secure Sockets (SOCKS) Errors](../CFNetwork/1518266-secure-sockets-socks-errors.md)
  Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [struct CFStreamEventType](cfstreameventtype.md)
  Defines constants for stream-related events.
- [Stream Properties](stream-properties.md)
  Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md)
  Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md)
  Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md)
  String constants that specify the service type of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/error-subdomains)*