# SSLGetPeerDomainName(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the peer domain name specified previously.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLGetPeerDomainName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<CChar>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

If you previously called the [`SSLSetPeerDomainName(_:_:_:)`](sslsetpeerdomainname(_:_:_:).md) function to specify a fully qualified domain name for the peer certificate, you can use the [`SSLGetPeerDomainName(_:_:_:)`](sslgetpeerdomainname(_:_:_:).md) function to retrieve the domain name.

## Parameters

- `context`: An SSL session context reference.
- `peerName`: On return, points to the peer domain name.
- `peerNameLen`: A pointer to the length of the peer domain name. Before calling this function, retrieve the peer domain name length by calling the function  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetpeerdomainname(_:_:_:))*