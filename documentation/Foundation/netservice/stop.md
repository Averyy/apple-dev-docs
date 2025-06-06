# stop()

**Framework**: Foundation  
**Kind**: method

Halts a currently running attempt to publish or resolve a service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

#### Discussion

The delegate will receive [`netServiceDidStop(_:)`](netservicedelegate/netservicedidstop(_:).md) after the service stops.

It is safe to remove all strong references to the service immediately after calling [`stop()`](netservice/stop().md).

## See Also

- [func publish()](netservice/publish.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](netservice/publish(options:).md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve()](netservice/resolve.md)
  Starts a resolve process for the service.
- [func resolve(withTimeout: TimeInterval)](netservice/resolve(withtimeout:).md)
  Starts a resolve process of a finite duration for the service.
- [var port: Int](netservice/port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](netservice/startmonitoring.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stopMonitoring()](netservice/stopmonitoring.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/stop())*