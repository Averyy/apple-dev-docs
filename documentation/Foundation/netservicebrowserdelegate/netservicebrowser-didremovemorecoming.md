# netServiceBrowser(_:didRemove:moreComing:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate a service has disappeared or has become unavailable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didRemove service: NetService, moreComing: Bool)
```

#### Discussion

The delegate uses this message to compile a list of unavailable services. It should wait until `moreServicesComing` is [`false`](https://developer.apple.com/documentation/swift/false) to do a bulk update of user interface elements.

## Parameters

- `browser`: Sender of this delegate message.
- `service`: Network service that has become unavailable.
- `moreComing`:   when   is waiting for additional services.   when there are no additional services.

## See Also

- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didRemoveDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremovedomain:morecoming:).md)
  Tells the delegate the a domain has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didFind: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:).md)
  Tells the delegate the sender found a service.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](netservicebrowserdelegate/netservicebrowser(_:didnotsearch:).md)
  Tells the delegate that a search was not successful.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserdidstopsearch(_:).md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didremove:morecoming:))*