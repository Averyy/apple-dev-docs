# CFStream Property SSL Settings Constants

**Framework**: Core Foundation

Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.

#### Overview

This enumeration defines the constants for keys in a `CFDictionary` object that is the value of the kCFStreamPropertySSLSettings key.

## Topics

### Constants
- [let kCFStreamSSLLevel: CFString](../CFNetwork/kCFStreamSSLLevel.md)
  Security property key whose value specifies the stream’s security level.
- [let kCFStreamSSLAllowsExpiredCertificates: CFString](../CFNetwork/kCFStreamSSLAllowsExpiredCertificates.md)
  Security property key whose value indicates whether expired certificates are allowed.
- [let kCFStreamSSLAllowsExpiredRoots: CFString](../CFNetwork/kCFStreamSSLAllowsExpiredRoots.md)
  Security property whose value indicates whether expired root certificates are allowed.
- [let kCFStreamSSLAllowsAnyRoot: CFString](../CFNetwork/kCFStreamSSLAllowsAnyRoot.md)
  Security property key whose value indicates whether root certificates should be allowed.
- [let kCFStreamSSLValidatesCertificateChain: CFString](../CFNetwork/kCFStreamSSLValidatesCertificateChain.md)
  Security property key whose value indicates whether the certificate chain should be validated.
- [let kCFStreamSSLPeerName: CFString](../CFNetwork/kCFStreamSSLPeerName.md)
  Security property key whose value overrides the name used for certificate verification.
- [let kCFStreamSSLCertificates: CFString](../CFNetwork/kCFStreamSSLCertificates.md)
  Security property key whose value is a CFArray of SecCertificateRefs except for the first element in the array, which is a SecIdentityRef.
- [let kCFStreamSSLIsServer: CFString](../CFNetwork/kCFStreamSSLIsServer.md)
  Security property key whose value indicates whether the connection is to act as a server in the SSL process.

## See Also

- [enum CFStreamStatus](cfstreamstatus.md)
  Constants that describe the status of a stream.
- [enum CFStreamErrorDomain](cfstreamerrordomain.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md)
  Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../CFNetwork/1518266-secure-sockets-socks-errors.md)
  Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [struct CFStreamEventType](cfstreameventtype.md)
  Defines constants for stream-related events.
- [Stream Properties](stream-properties.md)
  Stream property names that can be set or copied.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md)
  Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md)
  String constants that specify the service type of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstream-property-ssl-settings-constants)*