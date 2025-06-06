# SSLConnectionRef

**Framework**: Security  
**Kind**: typealias

A pointer to an opaque I/O connection object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SSLConnectionRef = UnsafeRawPointer
```

#### Discussion

The I/O connection object refers to data that identifies a connection. The connection data is opaque to Secure Transport; you can set it to any value that your application can use in the callback functions [`SSLReadFunc`](sslreadfunc.md) and [`SSLWriteFunc`](sslwritefunc.md) to uniquely identify the connection, such as a socket or endpoint. Use the [`SSLSetConnection(_:_:)`](sslsetconnection(_:_:).md) function to assign a value to the connection object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslconnectionref)*