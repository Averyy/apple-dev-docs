# CFStream Socket Security Level Constants

**Framework**: Core Foundation

Constants for setting the security level of a socket stream.

#### Overview

This enumeration defines the preferred constants for setting the security protocol for a socket stream pair when calling [`CFReadStreamSetProperty(_:_:_:)`](cfreadstreamsetproperty(_:_:_:).md) or [`CFWriteStreamSetProperty(_:_:_:)`](cfwritestreamsetproperty(_:_:_:).md).

## Topics

### Constants
- [let kCFStreamSocketSecurityLevelNone: CFString](kcfstreamsocketsecuritylevelnone.md)
  Specifies that no security level be set.
- [let kCFStreamSocketSecurityLevelSSLv2: CFString](kcfstreamsocketsecuritylevelsslv2.md)
  Specifies that SSL version 2 be set as the security protocol for a socket stream.
- [let kCFStreamSocketSecurityLevelSSLv3: CFString](kcfstreamsocketsecuritylevelsslv3.md)
  Specifies that SSL version 3 be set as the security protocol for a socket stream pair.
- [let kCFStreamSocketSecurityLevelTLSv1: CFString](kcfstreamsocketsecurityleveltlsv1.md)
  Specifies that TLS version 1 be set as the security protocol for a socket stream.
- [let kCFStreamSocketSecurityLevelNegotiatedSSL: CFString](kcfstreamsocketsecuritylevelnegotiatedssl.md)
  Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.

## See Also

- [func CFReadStreamSetProperty(CFReadStream!, CFStreamPropertyKey!, CFTypeRef!) -> Bool](cfreadstreamsetproperty(_:_:_:).md)
  Sets the value of a property for a stream.
- [func CFWriteStreamSetProperty(CFWriteStream!, CFStreamPropertyKey!, CFTypeRef!) -> Bool](cfwritestreamsetproperty(_:_:_:).md)
  Sets the value of a property for a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstream-socket-security-level-constants)*