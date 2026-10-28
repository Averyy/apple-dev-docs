# stop()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Halts a currently running attempt to publish or resolve a service.

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
func stop()
```

```objc
- (void) stop;
```

## Discussion

The delegate will receive [`netServiceDidStop(_:)`](../netservicedelegate/netservicedidstop%28_%29.md) after the service stops.

It is safe to remove all strong references to the service immediately after calling [`stop()`](./stop%28%29.md).

## See Also

### Using Network Services
- [func publish()](./publish%28%29.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](./publish%28options%29.md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve()](./resolve%28%29.md)
  Starts a resolve process for the service.
- [func resolve(withTimeout: TimeInterval)](./resolve%28withtimeout%29.md)
  Starts a resolve process of a finite duration for the service.
- [var port: Int](./port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](./startmonitoring%28%29.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stopMonitoring()](./stopmonitoring%28%29.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/stop())*