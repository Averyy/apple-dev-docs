# netService(_:didNotPublish:)

**Framework**: Foundation  
**Kind**: method

Notifies the delegate that a service could not be published.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netService(_ sender: NetService, didNotPublish errorDict: [String : NSNumber])
```

#### Discussion

This method may be called long after a [`netServiceWillPublish(_:)`](netservicedelegate/netservicewillpublish(_:).md) message has been delivered to the delegate.

## Parameters

- `sender`: The service that could not be published.
- `errorDict`: A dictionary containing information about the problem. The dictionary contains the keys   and  .

## See Also

- [func netServiceWillPublish(NetService)](netservicedelegate/netservicewillpublish(_:).md)
  Notifies the delegate that the network is ready to publish the service.
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
- [func netServiceDidStop(NetService)](netservicedelegate/netservicedidstop(_:).md)
  Informs the delegate that a [`publish()`](netservice/publish().md) or [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) request was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate/netservice(_:didnotpublish:))*