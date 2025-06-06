# resolve()

**Framework**: Foundation  
**Kind**: method

Starts a resolve process for the service.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func resolve()
```

#### Discussion

Attempts to determine at least one address for the service. This method returns immediately, with success or failure indicated by the callbacks to the delegate.

In OS X v10.4, this method calls [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) with a timeout value of `5`.

## See Also

- [var addresses: [Data]?](netservice/addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
- [func publish()](netservice/publish.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](netservice/publish(options:).md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve(withTimeout: TimeInterval)](netservice/resolve(withtimeout:).md)
  Starts a resolve process of a finite duration for the service.
- [var port: Int](netservice/port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](netservice/startmonitoring.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](netservice/stop.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](netservice/stopmonitoring.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/resolve())*