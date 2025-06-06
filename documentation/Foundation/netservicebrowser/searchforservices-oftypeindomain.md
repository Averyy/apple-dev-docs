# searchForServices(ofType:inDomain:)

**Framework**: Foundation  
**Kind**: method

Starts a search for services of a particular type within a specific domain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func searchForServices(ofType type: String, inDomain domainString: String)
```

#### Discussion

This method returns immediately, sending a [`netServiceBrowserWillSearch(_:)`](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md) message to the delegate if the network was ready to initiate the search.The delegate receives subsequent [`netServiceBrowser(_:didFind:moreComing:)`](netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:).md) messages for each service discovered.

The `serviceType` argument must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, rather than hosts, make sure to prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “`_http._tcp.`”. Note that the period character at the end is required.

The `domainName` argument can be an explicit domain name, the generic local domain `@"local."` (note trailing period, which indicates an absolute name), or the empty string (`@""`), which indicates the default registration domains. Usually, you pass in an empty string. Note that it is acceptable to use an empty string for the `domainName` argument when publishing or browsing a service, but do not rely on this for resolution.

## Parameters

- `type`: Type of the service to search for.
- `domainString`: Domain name in which to perform the search.

## See Also

- [func netServiceBrowser(NetServiceBrowser, didFind: NetService, moreComing: Bool)](netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:).md)
  Tells the delegate the sender found a service.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserwillsearch(_:).md)
  Tells the delegate that a search is commencing.
- [func searchForBrowsableDomains()](netservicebrowser/searchforbrowsabledomains.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [func searchForRegistrationDomains()](netservicebrowser/searchforregistrationdomains.md)
  Initiates a search for domains in which the host may register services.
- [func stop()](netservicebrowser/stop.md)
  Halts a currently running search or resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/searchforservices(oftype:indomain:))*