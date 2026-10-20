# SSLGetPeerDomainName(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the peer domain name specified previously.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetPeerDomainName(_ context: SSLContext, _ peerName: UnsafeMutablePointer<CChar>, _ peerNameLen: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus SSLGetPeerDomainName(SSLContextRef context, char *peerName, size_t *peerNameLen);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

If you previously called the [`SSLSetPeerDomainName(_:_:_:)`](./sslsetpeerdomainname%28_,_,_%29.md) function to specify a fully qualified domain name for the peer certificate, you can use the [`SSLGetPeerDomainName(_:_:_:)`](./sslgetpeerdomainname%28_,_,_%29.md) function to retrieve the domain name.

## Parameters

- `context`: An SSL session context reference.
- `peerName`: On return, points to the peer domain name.
- `peerNameLen`: A pointer to the length of the peer domain name. Before calling this function, retrieve the peer domain name length by calling the function [`SSLGetPeerDomainNameLength(_:_:)`](./sslgetpeerdomainnamelength%28_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetpeerdomainname(_:_:_:))*