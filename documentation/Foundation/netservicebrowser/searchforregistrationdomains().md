# searchForRegistrationDomains()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initiates a search for domains in which the host may register services.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_browser_t in Network framework instead

## Declaration

```swift
func searchForRegistrationDomains()
```

```objc
- (void) searchForRegistrationDomains;
```

#### Discussion

This method returns immediately, sending a [`netServiceBrowserWillSearch(_:)`](../netservicebrowserdelegate/netservicebrowserwillsearch%28_%29.md) message to the delegate if the network was ready to initiate the search. The delegate receives a subsequent [`netServiceBrowser(_:didFindDomain:moreComing:)`](../netservicebrowserdelegate/netservicebrowser%28_,didfinddomain,morecoming%29.md) message for each domain discovered.

Most network service browser clients do not have to use this method—it is sufficient to publish a service with the empty string, which registers it in any available registration domains automatically.

## See Also

### Related Documentation
- [func netServiceBrowserWillSearch(NetServiceBrowser)](../netservicebrowserdelegate/netservicebrowserwillsearch%28_%29.md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](../netservicebrowserdelegate/netservicebrowser%28_,didfinddomain,morecoming%29.md)
  Tells the delegate the sender found a domain.
### Using Network Service Browsers
- [func searchForBrowsableDomains()](./searchforbrowsabledomains%28%29.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [func searchForServices(ofType: String, inDomain: String)](./searchforservices%28oftype,indomain%29.md)
  Starts a search for services of a particular type within a specific domain.
- [func stop()](./stop%28%29.md)
  Halts a currently running search or resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/searchforregistrationdomains())*