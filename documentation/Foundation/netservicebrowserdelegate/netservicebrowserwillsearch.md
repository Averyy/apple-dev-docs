# netServiceBrowserWillSearch(_:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that a search is commencing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowserWillSearch(_ browser: NetServiceBrowser)
```

#### Discussion

This message is sent to the delegate only if the underlying network layer is ready to begin a search. The delegate can use this notification to prepare its data structures to receive data.

## Parameters

- `browser`: Sender of this delegate message.

## See Also

- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didRemoveDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremovedomain:morecoming:).md)
  Tells the delegate the a domain has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didFind: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:).md)
  Tells the delegate the sender found a service.
- [func netServiceBrowser(NetServiceBrowser, didRemove: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremove:morecoming:).md)
  Tells the delegate a service has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](netservicebrowserdelegate/netservicebrowser(_:didnotsearch:).md)
  Tells the delegate that a search was not successful.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserdidstopsearch(_:).md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowserwillsearch(_:))*