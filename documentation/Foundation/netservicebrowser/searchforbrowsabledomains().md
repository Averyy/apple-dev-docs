# searchForBrowsableDomains()

**Framework**: Foundation  
**Kind**: method

Initiates a search for domains visible to the host. This method returns immediately.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func searchForBrowsableDomains()
```

#### Discussion

The delegate receives a [`netServiceBrowser(_:didFindDomain:moreComing:)`](netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:).md) message for each domain discovered.

## See Also

- [func searchForRegistrationDomains()](netservicebrowser/searchforregistrationdomains.md)
  Initiates a search for domains in which the host may register services.
- [func searchForServices(ofType: String, inDomain: String)](netservicebrowser/searchforservices(oftype:indomain:).md)
  Starts a search for services of a particular type within a specific domain.
- [func stop()](netservicebrowser/stop.md)
  Halts a currently running search or resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/searchforbrowsabledomains())*