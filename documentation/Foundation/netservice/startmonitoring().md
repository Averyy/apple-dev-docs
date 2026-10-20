# startMonitoring()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Starts the monitoring of TXT-record updates for the receiver.

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
func startMonitoring()
```

```objc
- (void) startMonitoring;
```

#### Discussion

The delegate must implement [`netService(_:didUpdateTXTRecord:)`](../netservicedelegate/netservice%28_,didupdatetxtrecord%29.md), which is called when the TXT record for the receiver is updated.

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
- [func stop()](./stop%28%29.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](./stopmonitoring%28%29.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/startmonitoring())*