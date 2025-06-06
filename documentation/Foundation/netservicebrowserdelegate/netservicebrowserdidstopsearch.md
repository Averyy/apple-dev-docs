# netServiceBrowserDidStopSearch(_:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that a search was stopped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowserDidStopSearch(_ browser: NetServiceBrowser)
```

#### Discussion

When `netServiceBrowser` receives a [`stop()`](netservicebrowser/stop().md) message from its client, `netServiceBrowser` sends a `netServiceBrowserDidStopSearch:` message to its delegate. The delegate then performs any necessary cleanup.

## Parameters

- `browser`: Sender of this delegate message.

## See Also

- [func stop()](netservicebrowser/stop.md)
  Halts a currently running search or resolution.
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didRemoveDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremovedomain:morecoming:).md)
  Tells the delegate the a domain has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didFind: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:).md)
  Tells the delegate the sender found a service.
- [func netServiceBrowser(NetServiceBrowser, didRemove: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didremove:morecoming:).md)
  Tells the delegate a service has disappeared or has become unavailable.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](netservicebrowserdelegate/netservicebrowser(_:didnotsearch:).md)
  Tells the delegate that a search was not successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowserdidstopsearch(_:))*