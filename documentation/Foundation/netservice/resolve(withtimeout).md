# resolve(withTimeout:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Starts a resolve process of a finite duration for the service.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t or nw_listener_t in Network framework instead

## Declaration

```swift
func resolve(withTimeout timeout: TimeInterval)
```

```objc
- (void) resolveWithTimeout:(NSTimeInterval) timeout;
```

#### Discussion

During the resolve period, the service sends [`netServiceDidResolveAddress(_:)`](../netservicedelegate/netservicedidresolveaddress%28_%29.md) to the delegate for each address it discovers that matches the service parameters. Once the timeout is hit, the service sends [`netServiceDidStop(_:)`](../netservicedelegate/netservicedidstop%28_%29.md) to the delegate. If no addresses resolve during the timeout period, the service sends [`netService(_:didNotResolve:)`](../netservicedelegate/netservice%28_,didnotresolve%29.md) to the delegate.

## Parameters

- `timeout`: The maximum number of seconds to attempt a resolve. A value of 0.0 indicates no timeout and a resolve process of indefinite duration.

## See Also

### Related Documentation
- [var addresses: [Data]?](./addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
### Using Network Services
- [func publish()](./publish%28%29.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](./publish%28options%29.md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve()](./resolve%28%29.md)
  Starts a resolve process for the service.
- [var port: Int](./port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](./startmonitoring%28%29.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](./stop%28%29.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](./stopmonitoring%28%29.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/resolve(withtimeout:))*