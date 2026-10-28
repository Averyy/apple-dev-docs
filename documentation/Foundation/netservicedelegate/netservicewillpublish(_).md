# netServiceWillPublish(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the network is ready to publish the service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceWillPublish(_ sender: NetService)
```

```objc
- (void) netServiceWillPublish:(NSNetService *) sender;
```

## Discussion

Publication of the service proceeds asynchronously and may still generate a call to the delegate’s [`netService(_:didNotPublish:)`](./netservice%28_,didnotpublish%29.md) method if an error occurs.

## Parameters

- `sender`: The service that is ready to publish.

## See Also

### Related Documentation
- [Bonjour Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html#//apple_ref/doc/uid/10000119i)
- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html#//apple_ref/doc/uid/TP40002736)
### Using Network Services
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
- [func netService(NetService, didUpdateTXTRecord: Data)](./netservice%28_,didupdatetxtrecord%29.md)
  Notifies the delegate that the TXT record for a given service has been updated.
- [func netServiceDidStop(NetService)](./netservicedidstop%28_%29.md)
  Informs the delegate that a [`publish()`](../netservice/publish%28%29.md) or [`resolve(withTimeout:)`](../netservice/resolve%28withtimeout%29.md) request was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate/netservicewillpublish(_:))*