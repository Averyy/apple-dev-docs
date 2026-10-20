# listenForConnections

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var listenForConnections: NetService.Options { get }
```

```c
NSNetServiceListenForConnections
```

#### Discussion

Specifies that a TCP listener should be started for both IPv4 and IPv6 on the port specified by this service. If the listening port can’t be opened, the service calls its delegate’s [`netService(_:didNotPublish:)`](../../netservicedelegate/netservice%28_,didnotpublish%29.md) method to report the error.

The listener supports only TCP connections. If the service’s type does not end with `_tcp`, publication fails with [`NetService.ErrorCode.badArgumentError`](../errorcode-swift.enum/badargumenterror.md).

Whenever a client connects to the listening socket, the service calls its delegate’s [`netService(_:didAcceptConnectionWith:outputStream:)`](../../netservicedelegate/netservice%28_,didacceptconnectionwith,outputstream%29.md) method with a pair of `NSStream` objects.

## See Also

### Constants
- [static var noAutoRename: NetService.Options](./noautorename.md)
  Specifies that the network service should not rename itself in the event of a name collision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/options/listenforconnections)*