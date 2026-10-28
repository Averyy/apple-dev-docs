# stop()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Halts a currently running search or resolution.

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
func stop()
```

```objc
- (void) stop;
```

## Discussion

This method sends a [`netServiceBrowserDidStopSearch(_:)`](../netservicebrowserdelegate/netservicebrowserdidstopsearch%28_%29.md) message to the delegate and causes the browser to discard any pending search results.

## See Also

### Related Documentation
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](../netservicebrowserdelegate/netservicebrowserdidstopsearch%28_%29.md)
  Tells the delegate that a search was stopped.
### Using Network Service Browsers
- [func searchForBrowsableDomains()](./searchforbrowsabledomains%28%29.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [func searchForRegistrationDomains()](./searchforregistrationdomains%28%29.md)
  Initiates a search for domains in which the host may register services.
- [func searchForServices(ofType: String, inDomain: String)](./searchforservices%28oftype,indomain%29.md)
  Starts a search for services of a particular type within a specific domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/stop())*