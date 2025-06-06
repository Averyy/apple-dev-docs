# CFStream SOCKS Proxy Key Constants

**Framework**: Core Foundation

Constants for SOCKS Proxy `CFDictionary` keys.

#### Overview

When setting the stream’s SOCKS Proxy property, the property’s value is a `CFDictionary` object containing at minimum the kCFStreamPropertySOCKSProxyHost and kCFStreamPropertySOCKSProxyPort keys. The dictionary may also contain the other keys described in this section.

## Topics

### Constants
- [let kCFStreamPropertySOCKSProxyHost: CFString](kcfstreampropertysocksproxyhost.md)
  Constant for the SOCKS proxy host key.
- [let kCFStreamPropertySOCKSProxyPort: CFString](kcfstreampropertysocksproxyport.md)
  Constant for the SOCKS proxy host port key.
- [let kCFStreamPropertySOCKSVersion: CFString](kcfstreampropertysocksversion.md)
  Constant for the SOCKS version key.
- [let kCFStreamSocketSOCKSVersion4: CFString](kcfstreamsocketsocksversion4.md)
  Constant used in the `kCFStreamSockerSOCKSVersion` key to specify SOCKS4 as the SOCKS version for the stream.
- [let kCFStreamSocketSOCKSVersion5: CFString](kcfstreamsocketsocksversion5.md)
  Constant used in the `kCFStreamSOCKSVersion` key to specify SOCKS5 as the SOCKS version for the stream.
- [let kCFStreamPropertySOCKSUser: CFString](kcfstreampropertysocksuser.md)
  Constant for the key required to set a user name.
- [let kCFStreamPropertySOCKSPassword: CFString](kcfstreampropertysockspassword.md)
  Constant for the key required to set a user’s password.

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
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md)
  Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
- [Stream Service Types](stream-service-types.md)
  String constants that specify the service type of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstream-socks-proxy-key-constants)*