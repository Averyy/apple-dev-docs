# port

**Framework**: Foundation  
**Kind**: property

The port on which the service is listening for connections.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var port: Int { get }
```

#### Discussion

If the object was initialized by calling [`init(domain:type:name:port:)`](netservice/init(domain:type:name:port:).md) (whether by your code or by a browser object), then the value was set when the object was first initialized.

If the object was initialized by calling [`init(domain:type:name:)`](netservice/init(domain:type:name:).md), the value of this property is not valid (`-1`) until after the service has successfully been resolved (when `addresses` is non-`nil`).

> **Note**:  This became a property in OS X v10.9 and iOS 7, but the underlying getter method (`port`) has been available since this class was first introduced.

## See Also

- [func publish()](netservice/publish.md)
  Attempts to advertise the receiver’s on the network.
- [func publish(options: NetService.Options)](netservice/publish(options:).md)
  Attempts to advertise the receiver on the network, with the given options.
- [func resolve()](netservice/resolve.md)
  Starts a resolve process for the service.
- [func resolve(withTimeout: TimeInterval)](netservice/resolve(withtimeout:).md)
  Starts a resolve process of a finite duration for the service.
- [func startMonitoring()](netservice/startmonitoring.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](netservice/stop.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](netservice/stopmonitoring.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/port)*