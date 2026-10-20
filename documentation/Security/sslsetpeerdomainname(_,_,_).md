# SSLSetPeerDomainName(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies the fully qualified domain name of the peer.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetPeerDomainName(_ context: SSLContext, _ peerName: UnsafePointer<CChar>?, _ peerNameLen: Int) -> OSStatus
```

```c
OSStatus SSLSetPeerDomainName(SSLContextRef context, const char *peerName, size_t peerNameLen);
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](./using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

You can use this function to verify the common name field in the peer’s certificate. If you call this function and the common name in the certificate does not match the value you specify in the `peerName` parameter, then handshake fails and returns `errSSLXCertChainInvalid`. Use of this function is optional.

This function can be called only when no session is active.

## Parameters

- `context`: An SSL session context reference.
- `peerName`: The fully qualified domain name of the peer—for example, `store.apple.com`. The name is in the form of a C string, except that `NULL` termination is optional.
- `peerNameLen`: The number of bytes passed in the `peerName` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetpeerdomainname(_:_:_:))*