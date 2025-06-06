# kCFStreamPropertyShouldCloseNativeSocket

**Framework**: Core Foundation  
**Kind**: var

Should Close Native Socket property key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCFStreamPropertyShouldCloseNativeSocket: CFString
```

#### Discussion

If set to `kCFBooleanTrue`, the stream will close and release the underlying native socket when the stream is released. If set to `kCFBooleanFalse`, the stream will not close and release the underlying native socket when the stream is released. If a stream is created with a native socket, the default value of this property is `kCFBooleanFalse`. This property is only available for socket streams. It can be set by calling [`CFReadStreamSetProperty(_:_:_:)`](cfreadstreamsetproperty(_:_:_:).md) and [`CFWriteStreamSetProperty(_:_:_:)`](cfwritestreamsetproperty(_:_:_:).md), and it can be copied by [`CFReadStreamCopyProperty(_:_:)`](cfreadstreamcopyproperty(_:_:).md) and [`CFWriteStreamCopyProperty(_:_:)`](cfwritestreamcopyproperty(_:_:).md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfstreampropertyshouldclosenativesocket)*