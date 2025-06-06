# netServiceDidResolveAddress(_:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that the address for a given service was resolved.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceDidResolveAddress(_ sender: NetService)
```

#### Discussion

The delegate can use the [`addresses`](netservice/addresses.md) method to retrieve the service’s address. If the delegate needs only one address, it can stop the resolution process using [`stop()`](netservice/stop().md). Otherwise, the resolution will continue until the timeout specified in [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) is reached.

## Parameters

- `sender`: The service that was resolved.

## See Also

- [var addresses: [Data]?](netservice/addresses.md)
  A read-only array containing `NSData` objects, each of which contains a socket address for the service.
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
- [func netService(NetService, didUpdateTXTRecord: Data)](netservicedelegate/netservice(_:didupdatetxtrecord:).md)
  Notifies the delegate that the TXT record for a given service has been updated.
- [func netServiceDidStop(NetService)](netservicedelegate/netservicedidstop(_:).md)
  Informs the delegate that a [`publish()`](netservice/publish().md) or [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) request was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate/netservicedidresolveaddress(_:))*