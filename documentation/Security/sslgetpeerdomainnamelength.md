# SSLGetPeerDomainNameLength(_:_:)

**Framework**: Security  
**Kind**: func

Determines the length of a previously set peer domain name.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetPeerDomainNameLength(_ context: SSLContext, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

If you previously called the [`SSLSetPeerDomainName(_:_:_:)`](sslsetpeerdomainname(_:_:_:).md) function to specify a fully qualified domain name for the peer certificate, you can use the [`SSLGetPeerDomainName(_:_:_:)`](sslgetpeerdomainname(_:_:_:).md) function to retrieve the peer domain name. Before doing so, you must call the [`SSLGetPeerDomainNameLength(_:_:)`](sslgetpeerdomainnamelength(_:_:).md) function to retrieve the buffer size needed for the domain name.

## Parameters

- `context`: An SSL session context reference.
- `peerNameLen`: On return, points to the length of the peer domain name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetpeerdomainnamelength(_:_:))*