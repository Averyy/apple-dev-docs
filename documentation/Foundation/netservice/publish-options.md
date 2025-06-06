# publish(options:)

**Framework**: Foundation  
**Kind**: method

Attempts to advertise the receiver on the network, with the given options.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func publish(options: NetService.Options = [])
```

#### Discussion

This method returns immediately, with success or failure indicated by the callbacks to the delegate.

## Parameters

- `options`: Options for the receiver. The supported options are described in  .

## See Also

- [func publish()](netservice/publish.md)
  Attempts to advertise the receiver’s on the network.
- [func resolve()](netservice/resolve.md)
  Starts a resolve process for the service.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/publish(options:))*