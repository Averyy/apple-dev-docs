# Stream Properties

**Framework**: Core Foundation

Stream property names that can be set or copied.

#### Overview

Use [`CFReadStreamCopyProperty(_:_:)`](cfreadstreamcopyproperty(_:_:).md) or [`CFWriteStreamCopyProperty(_:_:)`](cfwritestreamcopyproperty(_:_:).md) to read the property values. Use [`CFReadStreamSetProperty(_:_:_:)`](cfreadstreamsetproperty(_:_:_:).md) or [`CFWriteStreamSetProperty(_:_:_:)`](cfwritestreamsetproperty(_:_:_:).md) to set the property values.

## Topics

### Constants
- [static let appendToFile: CFStreamPropertyKey!](cfstreampropertykey/appendtofile.md)
  Value is a `CFBoolean` value that indicates whether to append the written data to a file, if it already exists, rather than to replace its contents.
- [static let dataWritten: CFStreamPropertyKey!](cfstreampropertykey/datawritten.md)
  Value is a `CFData` object that contains all the bytes written to a writable memory stream. You cannot modify this value.
- [static let fileCurrentOffset: CFStreamPropertyKey!](cfstreampropertykey/filecurrentoffset.md)
  Value is a `CFNumber` object containing the current file offset.
- [static let socketNativeHandle: CFStreamPropertyKey!](cfstreampropertykey/socketnativehandle.md)
  Value is a `CFData` object that contains the native handle for a socket stream—of type [`CFSocketNativeHandle`](cfsocketnativehandle.md)—to which the socket stream is connected.
- [static let socketRemoteHostName: CFStreamPropertyKey!](cfstreampropertykey/socketremotehostname.md)
  Value is a `CFString` object containing the name of the host to which the socket stream is connected or `NULL` if unknown.
- [static let socketRemotePortNumber: CFStreamPropertyKey!](cfstreampropertykey/socketremoteportnumber.md)
  Value is a `CFNumber` object containing the remote port number to which the socket stream is connected or `NULL` if unknown.
- [let kCFStreamPropertyShouldCloseNativeSocket: CFString](kcfstreampropertyshouldclosenativesocket.md)
  Should Close Native Socket property key.
- [let kCFStreamPropertySocketSecurityLevel: CFString](kcfstreampropertysocketsecuritylevel.md)
  Socket Security Level property key.
- [let kCFStreamPropertySSLPeerCertificates: CFString](../CFNetwork/kCFStreamPropertySSLPeerCertificates.md)
  SSL Peer Certificates property key for copy operations, which return a `CFArray` object containing `SecCertificateRef` objects.
- [let kCFStreamPropertySSLPeerTrust: CFString](../CFNetwork/kCFStreamPropertySSLPeerTrust.md)
  SSL Peer Trust property key for copy operations, which return a `SecTrustRef` object containing the result of the SSL handshake.
- [let kCFStreamPropertySSLSettings: CFString](../CFNetwork/kCFStreamPropertySSLSettings.md)
  SSL Settings property key for set operations.
- [let kCFStreamPropertySSLContext: CFString](../CFNetwork/kCFStreamPropertySSLContext.md)
- [let kCFStreamPropertySOCKSProxy: CFString](kcfstreampropertysocksproxy.md)
  SOCKS proxy property key.
- [let kCFStreamPropertyProxyLocalBypass: CFString](../CFNetwork/kCFStreamPropertyProxyLocalBypass.md)
  Proxy Local Bypass property key.
- [let kCFStreamPropertySocketRemoteHost: CFString](../CFNetwork/kCFStreamPropertySocketRemoteHost.md)
  The key’s value is a `CFHostRef` for the remote host if it is known. If not, its value is `NULL`.
- [let kCFStreamPropertySocketRemoteNetService: CFString](../CFNetwork/kCFStreamPropertySocketRemoteNetService.md)
  The key’s value is a `CFNetServiceRef` for the remote network service if it is known. If not, its value is `NULL`.
- [let kCFStreamNetworkServiceType: CFString](../CFNetwork/kCFStreamNetworkServiceType.md)
  The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See [Stream Service Types](doc://com.apple.documentation/documentation/CoreFoundation/stream-service-types) for a list of possible values.
- [let kCFStreamPropertyConnectionIsCellular: CFString](../CFNetwork/kCFStreamPropertyConnectionIsCellular.md)
  A boolean value indicating whether the stream is connected over a cellular (WWAN) interface. This is a read-only property, and is `false` until the connection has been established.
- [let kCFStreamPropertyNoCellular: CFString](../CFNetwork/kCFStreamPropertyNoCellular.md)
  A Boolean value indicating that the connection should not be established over a cellular (WWAN) connection. This value can only be set *before* you open the stream.

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
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md)
  Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md)
  Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md)
  String constants that specify the service type of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/stream-properties)*