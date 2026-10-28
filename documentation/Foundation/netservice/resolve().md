# resolve()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Starts a resolve process for the service.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`resolve(withTimeout:)`](./resolve%28withtimeout%29.md) instead.

## Declaration

```swift
func resolve()
```

```objc
- (void) resolve;
```

## Discussion

Attempts to determine at least one address for the service. This method returns immediately, with success or failure indicated by the callbacks to the delegate.

In OS X v10.4, this method calls [`resolve(withTimeout:)`](./resolve%28withtimeout%29.md) with a timeout value of `5`.

## See Also

### Related Documentation
- [var addresses: [Data]?](./addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
### Using Network Services
- [func publish()](./publish%28%29.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](./publish%28options%29.md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve(withTimeout: TimeInterval)](./resolve%28withtimeout%29.md)
  Starts a resolve process of a finite duration for the service.
- [var port: Int](./port.md)
  The port on which the service is listening for connections.
- [func startMonitoring()](./startmonitoring%28%29.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](./stop%28%29.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](./stopmonitoring%28%29.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/resolve())*