# SSLSetConnection(_:_:)

**Framework**: Security  
**Kind**: func

Specifies an I/O connection for a specific session.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLSetConnection(_ context: SSLContext, _ connection: SSLConnectionRef?) -> OSStatus
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

You must establish a connection before creating a secure session. After calling the [`SSLCreateContext(_:_:_:)`](sslcreatecontext(_:_:_:).md) function to create an SSL session context, you call the [`SSLSetConnection(_:_:)`](sslsetconnection(_:_:).md) function to specify the connection to which the context applies. You specify a value in the `connection` parameter that your callback routines can use to identify the connection. This value might be a pointer to a socket (if you are using the Sockets API) or an endpoint (if you are using Open Transport). For example, you might create a socket, start a connection on it, create a context reference, cast the socket to an [`SSLConnectionRef`](sslconnectionref.md), and then pass both the context reference and connection reference to the [`SSLSetConnection(_:_:)`](sslsetconnection(_:_:).md) function.

Note that the Sockets API is the preferred networking interface for new development.

On the client side, it’s assumed that communication has been established with the desired server on this connection. On the server side, it’s assumed that a connection has been established in response to an incoming client request .

This function must be called prior to the [`SSLHandshake(_:)`](sslhandshake(_:).md) function; consequently, this function can be called only when no session is active.

## Parameters

- `context`: An SSL session context reference.
- `connection`: An SSL session connection reference. The connection data is opaque to Secure Transport; you can set it to any value that your application can use to uniquely identify the connection in the callback functions   and  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetconnection(_:_:))*