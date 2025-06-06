# netServiceDidStop(_:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that a [`publish()`](netservice/publish().md) or [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) request was stopped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceDidStop(_ sender: NetService)
```

## Parameters

- `sender`: The service that stopped.

## See Also

- [func netServiceWillPublish(NetService)](netservicedelegate/netservicewillpublish(_:).md)
  Notifies the delegate that the network is ready to publish the service.
- [func netService(NetService, didNotPublish: [String : NSNumber])](netservicedelegate/netservice(_:didnotpublish:).md)
  Notifies the delegate that a service could not be published.
- [func netServiceDidPublish(NetService)](netservicedelegate/netservicedidpublish(_:).md)
  Notifies the delegate that a service was successfully published.
- [func netServiceWillResolve(NetService)](netservicedelegate/netservicewillresolve(_:).md)
  Notifies the delegate that the network is ready to resolve the service.
- [func netService(NetService, didNotResolve: [String : NSNumber])](netservicedelegate/netservice(_:didnotresolve:).md)
  Informs the delegate that an error occurred during resolution of a given service.
- [func netServiceDidResolveAddress(NetService)](netservicedelegate/netservicedidresolveaddress(_:).md)
  Informs the delegate that the address for a given service was resolved.
- [func netService(NetService, didUpdateTXTRecord: Data)](netservicedelegate/netservice(_:didupdatetxtrecord:).md)
  Notifies the delegate that the TXT record for a given service has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate/netservicedidstop(_:))*