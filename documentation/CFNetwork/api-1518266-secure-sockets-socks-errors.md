# Secure Sockets (SOCKS) Errors

**Framework**: CFNetwork

Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.

#### Overview

Error codes in the `kCFStreamErrorDomainSOCKS` domain can come from multiple parts of the protocol stack, many of which define their own error values as part of outside specifications such as the HTTP specification.

To avoid confusion from conflicting error numbers, error codes in the `kCFStreamErrorDomainSOCKS` domain contain two parts: a subdomain, which tells which part of the protocol stack generated the error, and the error code itself.

Calling [`CFSocketStreamSOCKSGetErrorSubdomain(_:)`](cfsocketstreamsocksgeterrorsubdomain(_:).md) returns an identifier that tells which layer of the protocol stack produced the error.

Calling [`CFSocketStreamSOCKSGetError(_:)`](cfsocketstreamsocksgeterror(_:).md) returns the actual error code that the subdomain describes. This list of constants contains the possible values that this function will return. They must be interpreted within the context of the relevant error subdomain.

## Topics

### Constants
- [var kCFStreamErrorSOCKS4IdConflict: Int](kcfstreamerrorsocks4idconflict.md)
  Request rejected by the server because the client program and the `identd` daemon reported different user IDs.
- [var kCFStreamErrorSOCKS4IdentdFailed: Int](kcfstreamerrorsocks4identdfailed.md)
  Request rejected by the server because it couldn’t connect to the `identd` daemon on the client.
- [var kCFStreamErrorSOCKS4RequestFailed: Int](kcfstreamerrorsocks4requestfailed.md)
  Request rejected by the server or request failed.
- [var kCFStreamErrorSOCKS4SubDomainResponse: Int](kcfstreamerrorsocks4subdomainresponse.md)
  The SOCKS4 status code returned by the server.
- [var kCFStreamErrorSOCKS5SubDomainMethod: Int](kcfstreamerrorsocks5subdomainmethod.md)
  The server’s desired negotiation method.
- [var kCFStreamErrorSOCKS5SubDomainResponse: Int](kcfstreamerrorsocks5subdomainresponse.md)
  The response code that the server returned in reply to the connection request.
- [var kCFStreamErrorSOCKS5SubDomainUserPass: Int](kcfstreamerrorsocks5subdomainuserpass.md)
  The status code that the server returned during authentication.
- [var kCFStreamErrorSOCKSSubDomainNone: Int](kcfstreamerrorsockssubdomainnone.md)
  A general SOCKS error.
- [var kCFStreamErrorSOCKSSubDomainVersionCode: Int](kcfstreamerrorsockssubdomainversioncode.md)
  The version of SOCKS that the server wants to use.
- [var kSOCKS5NoAcceptableMethod: Int](ksocks5noacceptablemethod.md)
  The client and server couldn’t find a mutually agreeable authentication method.
- [var kCFStreamErrorSOCKS5BadResponseAddr: Int](kcfstreamerrorsocks5badresponseaddr.md)
  The address returned is not of a known type. This error code is only valid for errors in the `kCFStreamErrorSOCKSSubDomainNone` subdomain.
- [var kCFStreamErrorSOCKS5BadState: Int](kcfstreamerrorsocks5badstate.md)
  The stream is not in a state that allows the requested operation. This error code is only valid for errors in the `kCFStreamErrorSOCKSSubDomainNone` subdomain..
- [var kCFStreamErrorSOCKSUnknownClientVersion: Int](kcfstreamerrorsocksunknownclientversion.md)
  The SOCKS server rejected access because it does not support connections with the requested SOCKS version. SOCKS client version. You can query the `kCFSOCKSVersionKey` key to find out what version the server requested. This error code is only valid for errors in the `kCFStreamErrorSOCKSSubDomainNone` subdomain.

## See Also

- [func CFReadStreamCreateForHTTPRequest(CFAllocator?, CFHTTPMessage) -> Unmanaged<CFReadStream>](cfreadstreamcreateforhttprequest(_:_:).md)
  Creates a read stream for a CFHTTP request message.
- [func CFReadStreamCreateForStreamedHTTPRequest(CFAllocator?, CFHTTPMessage, CFReadStream) -> Unmanaged<CFReadStream>](cfreadstreamcreateforstreamedhttprequest(_:_:_:).md)
  Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory.
- [let kCFStreamPropertyHTTPAttemptPersistentConnection: CFString](kcfstreampropertyhttpattemptpersistentconnection.md)
- [let kCFStreamPropertyHTTPFinalRequest: CFString](kcfstreampropertyhttpfinalrequest.md)
  HTTP Final Request property. A value of type CFHTTPMessage containing the final message transmitted by the stream after all modifications (including authentication, connection policy, redirects, and so on) have been made. This property cannot be set.
- [let kCFStreamPropertyHTTPFinalURL: CFString](kcfstreampropertyhttpfinalurl.md)
  HTTP Final URL property. A value of type CFURL containing the final HTTP URL. This value differs from the URL in the original HTTP request if an autoredirection occurred. This property cannot be set.
- [let kCFStreamPropertyHTTPProxy: CFString](kcfstreampropertyhttpproxy.md)
- [let kCFStreamPropertyHTTPProxyHost: CFString](kcfstreampropertyhttpproxyhost.md)
- [let kCFStreamPropertyHTTPProxyPort: CFString](kcfstreampropertyhttpproxyport.md)
- [let kCFStreamPropertyHTTPRequestBytesWrittenCount: CFString](kcfstreampropertyhttprequestbyteswrittencount.md)
- [let kCFStreamPropertyHTTPResponseHeader: CFString](kcfstreampropertyhttpresponseheader.md)
  HTTP Response Header property. When copied by [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)), the header of an HTTP response message is returned.
- [let kCFStreamPropertyHTTPSProxyHost: CFString](kcfstreampropertyhttpsproxyhost.md)
- [let kCFStreamPropertyHTTPSProxyPort: CFString](kcfstreampropertyhttpsproxyport.md)
- [let kCFStreamPropertyHTTPShouldAutoredirect: CFString](kcfstreampropertyhttpshouldautoredirect.md)
  HTTP Should Auto Redirect property. Set this property to `kCFBooleanTrue` to enable autoredirection; set this property to `kCFBooleanFalse` to disable autoredirection.
- [func CFWriteStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFWriteStream>](cfwritestreamcreatewithftpurl(_:_:).md)
  Creates an FTP write stream.
- [func CFReadStreamCreateWithFTPURL(CFAllocator?, CFURL) -> Unmanaged<CFReadStream>](cfreadstreamcreatewithftpurl(_:_:).md)
  Creates an FTP read stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/1518266-secure-sockets-socks-errors)*