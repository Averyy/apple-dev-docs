# kCFStreamErrorSOCKS4IdConflict

**Framework**: CFNetwork  
**Kind**: var

Request rejected by the server because the client program and the `identd` daemon reported different user IDs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var kCFStreamErrorSOCKS4IdConflict: Int { get }
```

#### Discussion

This error is specific to SOCKS4. This error code is only valid for errors in the `kCFStreamErrorSOCKS4SubDomainResponse` subdomain.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfstreamerrorsocks4idconflict)*