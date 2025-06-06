# startMonitoring()

**Framework**: Foundation  
**Kind**: method

Starts the monitoring of TXT-record updates for the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startMonitoring()
```

#### Discussion

The delegate must implement [`netService(_:didUpdateTXTRecord:)`](netservicedelegate/netservice(_:didupdatetxtrecord:).md), which is called when the TXT record for the receiver is updated.

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
- [func stop()](netservice/stop.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](netservice/stopmonitoring.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/startmonitoring())*