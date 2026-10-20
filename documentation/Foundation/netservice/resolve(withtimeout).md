# resolve(withTimeout:)

**Framework**: Foundation  
**Kind**: method

Starts a resolve process of a finite duration for the service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func resolve(withTimeout timeout: TimeInterval)
```

#### Discussion

During the resolve period, the service sends [`netServiceDidResolveAddress(_:)`](netservicedelegate/netservicedidresolveaddress(_:).md) to the delegate for each address it discovers that matches the service parameters. Once the timeout is hit, the service sends [`netServiceDidStop(_:)`](netservicedelegate/netservicedidstop(_:).md) to the delegate. If no addresses resolve during the timeout period, the service sends [`netService(_:didNotResolve:)`](netservicedelegate/netservice(_:didnotresolve:).md) to the delegate.

## Parameters

- `timeout`: The maximum number of seconds to attempt a resolve. A value of 0.0 indicates no timeout and a resolve process of indefinite duration.

## See Also

- [var addresses: [Data]?](netservice/addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
- [func publish()](netservice/publish.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](netservice/publish(options:).md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve()](netservice/resolve.md)
  Starts a resolve process for the service.
- [var port: Int](netservice/port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](netservice/startmonitoring.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](netservice/stop.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](netservice/stopmonitoring.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/resolve(withtimeout:))*