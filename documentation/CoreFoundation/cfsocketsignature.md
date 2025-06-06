# CFSocketSignature

**Framework**: Core Foundation  
**Kind**: struct

A structure that fully specifies the communication protocol and connection address of a CFSocket object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFSocketSignature
```

## Topics

### Initializers
- [init()](cfsocketsignature/init.md)
- [init(protocolFamily: Int32, socketType: Int32, protocol: Int32, address: Unmanaged<CFData>!)](cfsocketsignature/init(protocolfamily:sockettype:protocol:address:).md)
### Instance Properties
- [var address: Unmanaged<CFData>!](cfsocketsignature/address.md)
  A CFData object holding the contents of a `struct sockaddr` appropriate for the given protocol family (`struct sockaddr_in` or `struct sockaddr_in6`, for example), identifying the address of the socket.
- [var `protocol`: Int32](cfsocketsignature/protocol.md)
  The protocol type of the socket.
- [var protocolFamily: Int32](cfsocketsignature/protocolfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](cfsocketsignature/sockettype.md)
  The socket type of the socket.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct CFSocketContext](cfsocketcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a CFSocket object’s behavior.
- [typealias CFSocketNativeHandle](cfsocketnativehandle.md)
  Type for the platform-specific native socket handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketsignature)*