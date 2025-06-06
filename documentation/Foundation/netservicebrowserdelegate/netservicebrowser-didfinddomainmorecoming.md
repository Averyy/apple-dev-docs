# netServiceBrowser(_:didFindDomain:moreComing:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate the sender found a domain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didFindDomain domainString: String, moreComing: Bool)
```

#### Discussion

The delegate uses this message to compile a list of available domains. It should wait until `moreDomainsComing` is [`false`](https://developer.apple.com/documentation/swift/false) to do a bulk update of user interface elements.

## Parameters

- `browser`: Sender of this delegate message.
- `domainString`: Name of the domain found by  .
- `moreComing`:   when   is waiting for additional domains.   when there are no additional domains.

## See Also

- [func searchForBrowsableDomains()](netservicebrowser/searchforbrowsabledomains.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [Bonjour Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html#//apple_ref/doc/uid/10000119i)
- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html#//apple_ref/doc/uid/TP40002736)
- [func searchForRegistrationDomains()](netservicebrowser/searchforregistrationdomains.md)
  Initiates a search for domains in which the host may register services.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:))*