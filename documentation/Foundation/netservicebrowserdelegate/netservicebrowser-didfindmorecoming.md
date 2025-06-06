# netServiceBrowser(_:didFind:moreComing:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

The delegate uses this message to compile a list of available services. It should wait until `moreServicesComing` is [`false`](https://developer.apple.com/documentation/swift/false) to do a bulk update of user interface elements.

##### Special Considerations

If the delegate chooses to resolve `netService`, it should retain `netService` and set itself as that service’s delegate. The delegate should, therefore, release that service when it receives the [`netServiceDidResolveAddress(_:)`](netservicedelegate/netservicedidresolveaddress(_:).md) or [`netService(_:didNotResolve:)`](netservicedelegate/netservice(_:didnotresolve:).md) delegate messages of the  [`NetService`](netservice.md) class.

## Parameters

- `browser`: Sender of this delegate message.
- `service`: Network service found by  . The delegate can use this object to connect to and use the service.
- `moreComing`:   when   is waiting for additional services.   when there are no additional services.

## See Also

- [func searchForServices(ofType: String, inDomain: String)](netservicebrowser/searchforservices(oftype:indomain:).md)
  Starts a search for services of a particular type within a specific domain.
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didRemoveDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremovedomain:morecoming:).md)
  Tells the delegate the a domain has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didRemove: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremove:morecoming:).md)
  Tells the delegate a service has disappeared or has become unavailable.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](netservicebrowserdelegate/netservicebrowser(_:didnotsearch:).md)
  Tells the delegate that a search was not successful.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserdidstopsearch(_:).md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:))*