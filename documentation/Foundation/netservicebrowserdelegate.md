# NetServiceBrowserDelegate

**Framework**: Foundation  
**Kind**: protocol

The interface a net service browser uses to inform a delegate about the state of service discovery.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol NetServiceBrowserDelegate : NSObjectProtocol
```

#### Overview

Delegates of [`NetServiceBrowser`](netservicebrowser.md) instances optionally implement these methods.

## Topics

### Using Network Service Browsers
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
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserdidstopsearch(_:).md)
  Tells the delegate that a search was stopped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NetServiceBrowser](netservicebrowser.md)
  A network service browser that finds published services on a network using multicast DNS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate)*