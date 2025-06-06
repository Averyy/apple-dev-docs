# searchForRegistrationDomains()

**Framework**: Foundation  
**Kind**: method

Initiates a search for domains in which the host may register services.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func searchForRegistrationDomains()
```

#### Discussion

This method returns immediately, sending a [`netServiceBrowserWillSearch(_:)`](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md) message to the delegate if the network was ready to initiate the search. The delegate receives a subsequent [`netServiceBrowser(_:didFindDomain:moreComing:)`](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md) message for each domain discovered.

Most network service browser clients do not have to use this method—it is sufficient to publish a service with the empty string, which registers it in any available registration domains automatically.

## See Also

- [func netServiceBrowserWillSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md)
  Tells the delegate the sender found a domain.
- [func searchForBrowsableDomains()](netservicebrowser/searchforbrowsabledomains.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [func searchForServices(ofType: String, inDomain: String)](netservicebrowser/searchforservices(oftype:indomain:).md)
  Starts a search for services of a particular type within a specific domain.
- [func stop()](netservicebrowser/stop.md)
  Halts a currently running search or resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/searchforregistrationdomains())*