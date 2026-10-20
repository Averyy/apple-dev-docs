# publish(options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to advertise the receiver on the network, with the given options.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.5+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
func publish(options: NetService.Options = [])
```

```objc
- (void) publishWithOptions:(NSNetServiceOptions) options;
```

#### Discussion

This method returns immediately, with success or failure indicated by the callbacks to the delegate.

## Parameters

- `options`: Options for the receiver. The supported options are described in [`NetService.Options`](./options.md).

## See Also

### Using Network Services
- [func publish()](./publish%28%29.md)
  Attempts to advertise the receiver’s on the network.
- [func resolve()](./resolve%28%29.md)
  Starts a resolve process for the service.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/publish(options:))*