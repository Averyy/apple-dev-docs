# netServiceBrowser(_:didFind:moreComing:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the sender found a service.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didFind service: NetService, moreComing: Bool)
```

```objc
- (void) netServiceBrowser:(NSNetServiceBrowser *) browser didFindService:(NSNetService *) service moreComing:(BOOL) moreComing;
```

#### Discussion

The delegate uses this message to compile a list of available services. It should wait until `moreServicesComing` is [`false`](../../Swift/false.md) to do a bulk update of user interface elements.

##### Special Considerations

If the delegate chooses to resolve `netService`, it should retain `netService` and set itself as that service’s delegate. The delegate should, therefore, release that service when it receives the [`netServiceDidResolveAddress(_:)`](../netservicedelegate/netservicedidresolveaddress%28_%29.md) or [`netService(_:didNotResolve:)`](../netservicedelegate/netservice%28_,didnotresolve%29.md) delegate messages of the  [`NetService`](../netservice.md) class.

## Parameters

- `browser`: Sender of this delegate message.
- `service`: Network service found by `netServiceBrowser`. The delegate can use this object to connect to and use the service.
- `moreComing`: [`true`](../../Swift/true.md) when `netServiceBrowser` is waiting for additional services. [`false`](../../Swift/false.md) when there are no additional services.

## See Also

### Related Documentation
- [func searchForServices(ofType: String, inDomain: String)](../netservicebrowser/searchforservices%28oftype,indomain%29.md)
  Starts a search for services of a particular type within a specific domain.
### Using Network Service Browsers
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](./netservicebrowser%28_,didfinddomain,morecoming%29.md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didRemoveDomain: String, moreComing: Bool)](./netservicebrowser%28_,didremovedomain,morecoming%29.md)
  Tells the delegate the a domain has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didRemove: NetService, moreComing: Bool)](./netservicebrowser%28_,didremove,morecoming%29.md)
  Tells the delegate a service has disappeared or has become unavailable.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](./netservicebrowserwillsearch%28_%29.md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](./netservicebrowser%28_,didnotsearch%29.md)
  Tells the delegate that a search was not successful.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](./netservicebrowserdidstopsearch%28_%29.md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:))*