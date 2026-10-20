# port

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The port on which the service is listening for connections.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.5+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
var port: Int { get }
```

```objc
@property (readonly) NSInteger port;
```

#### Discussion

If the object was initialized by calling [`init(domain:type:name:port:)`](./init%28domain,type,name,port%29.md) (whether by your code or by a browser object), then the value was set when the object was first initialized.

If the object was initialized by calling [`init(domain:type:name:)`](./init%28domain,type,name%29.md), the value of this property is not valid (`-1`) until after the service has successfully been resolved (when `addresses` is non-`nil`).

> **Backward Compatibility Note**:  This became a property in OS X v10.9 and iOS 7, but the underlying getter method (`port`) has been available since this class was first introduced.

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
- [func startMonitoring()](./startmonitoring%28%29.md)
  Starts the monitoring of TXT-record updates for the receiver.
- [func stop()](./stop%28%29.md)
  Halts a currently running attempt to publish or resolve a service.
- [func stopMonitoring()](./stopmonitoring%28%29.md)
  Stops the monitoring of TXT-record updates for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/port)*