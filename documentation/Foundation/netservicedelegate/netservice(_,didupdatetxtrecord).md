# netService(_:didUpdateTXTRecord:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the TXT record for a given service has been updated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netService(_ sender: NetService, didUpdateTXTRecord data: Data)
```

```objc
- (void) netService:(NSNetService *) sender didUpdateTXTRecordData:(NSData *) data;
```

## Parameters

- `sender`: The service whose TXT record was updated.
- `data`: The new TXT record.

## See Also

### Related Documentation
- [func startMonitoring()](../netservice/startmonitoring%28%29.md)
  Starts the monitoring of TXT-record updates for the receiver.
### Using Network Services
- [func netServiceWillPublish(NetService)](./netservicewillpublish%28_%29.md)
  Notifies the delegate that the network is ready to publish the service.
- [func netService(NetService, didNotPublish: [String : NSNumber])](./netservice%28_,didnotpublish%29.md)
  Notifies the delegate that a service could not be published.
- [func netServiceDidPublish(NetService)](./netservicedidpublish%28_%29.md)
  Notifies the delegate that a service was successfully published.
- [func netServiceWillResolve(NetService)](./netservicewillresolve%28_%29.md)
  Notifies the delegate that the network is ready to resolve the service.
- [func netService(NetService, didNotResolve: [String : NSNumber])](./netservice%28_,didnotresolve%29.md)
  Informs the delegate that an error occurred during resolution of a given service.
- [func netServiceDidResolveAddress(NetService)](./netservicedidresolveaddress%28_%29.md)
  Informs the delegate that the address for a given service was resolved.
- [func netServiceDidStop(NetService)](./netservicedidstop%28_%29.md)
  Informs the delegate that a [`publish()`](../netservice/publish%28%29.md) or [`resolve(withTimeout:)`](../netservice/resolve%28withtimeout%29.md) request was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate/netservice(_:didupdatetxtrecord:))*