# searchForBrowsableDomains()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initiates a search for domains visible to the host. This method returns immediately.

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
func searchForBrowsableDomains()
```

```objc
- (void) searchForBrowsableDomains;
```

## Discussion

The delegate receives a [`netServiceBrowser(_:didFindDomain:moreComing:)`](../netservicebrowserdelegate/netservicebrowser%28_,didfinddomain,morecoming%29.md) message for each domain discovered.

## See Also

### Using Network Service Browsers
- [func searchForRegistrationDomains()](./searchforregistrationdomains%28%29.md)
  Initiates a search for domains in which the host may register services.
- [func searchForServices(ofType: String, inDomain: String)](./searchforservices%28oftype,indomain%29.md)
  Starts a search for services of a particular type within a specific domain.
- [func stop()](./stop%28%29.md)
  Halts a currently running search or resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/searchforbrowsabledomains())*