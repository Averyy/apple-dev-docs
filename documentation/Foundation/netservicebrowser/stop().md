# stop()

**Framework**: Foundation  
**Kind**: method

Halts a currently running search or resolution.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

#### Discussion

This method sends a [`netServiceBrowserDidStopSearch(_:)`](netservicebrowserdelegate/netservicebrowserdidstopsearch(_:).md) message to the delegate and causes the browser to discard any pending search results.

## See Also

- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](netservicebrowserdelegate/netservicebrowserdidstopsearch(_:).md)
  Tells the delegate that a search was stopped.
- [func searchForBrowsableDomains()](netservicebrowser/searchforbrowsabledomains.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [func searchForRegistrationDomains()](netservicebrowser/searchforregistrationdomains.md)
  Initiates a search for domains in which the host may register services.
- [func searchForServices(ofType: String, inDomain: String)](netservicebrowser/searchforservices(oftype:indomain:).md)
  Starts a search for services of a particular type within a specific domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/stop())*